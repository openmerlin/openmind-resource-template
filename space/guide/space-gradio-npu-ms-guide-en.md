**Get started.**

This is a Gradio space running on Ascend NPUs. Upload at least the `app.py` and `requirements.txt` files that comply with the Gradio and Python programming specifications. Then the space automatically triggers image building and runs Gradio. See the demo below:

**Clone this repository:**

```bash
git clone [git_https_url]
cd [repo_name]
```

**Create app.py:**

```bash
cat > app.py << EOF
import argparse
import time
from threading import Thread
import mdtex2html
import mindspore as ms
import gradio as gr

from mindformers import TextIteratorStreamer, logger
from mindformers.tools.utils import str2bool
from openmind import AutoModelForCausalLM, AutoTokenizer

# 设置模型名称
# set the model name
REPO_ID = "openmind/baichuan2_7b_chat_ms"

def get_model_and_tokenizer():
    # 初始化分词器和模型
    # initial the tokenizer and model
    """Get model and tokenizer instance"""
    model = AutoModelForCausalLM.from_pretrained(REPO_ID,
                                      trust_remote_code=True,
                                      use_past=True)
    tokenizer = AutoTokenizer.from_pretrained(REPO_ID)
    return model, tokenizer

# 设置运行模式和推理使用的卡
# set the device of inference
ms.set_context(mode=ms.GRAPH_MODE, device_target="Ascend", device_id=0)

# 配置模型推理参数
# set the configs of model inference
model, tokenizer = get_model_and_tokenizer()
config = model.config

# 预先构建网络
# pre-build the network
logger.info("***********************预热中****************************")
logger.info(f"model type: {type(model)}")
sample_input = tokenizer("hello")
sample_output = model.generate(sample_input["input_ids"], max_length=10)
logger.info("***********************预热结束****************************")

class Chatbot(gr.Chatbot):
    # 聊天机器人
    # Chatbot with overrode postprocess method

    def postprocess(self, y):
        # 后处理
        # postprocess
        if y is None:
            return []
        for i, (message, response) in enumerate(y):
            y[i] = (
                None if message is None else mdtex2html.convert(message),
                None if response is None else mdtex2html.convert(response),
            )
        return y


def parse_text(text):
    # 文本转换为HTML格式
    # copy from https://github.com/GaiZhenbiao/ChuanhuChatGPT
    lines = text.split("\n")
    lines = [line for line in lines if line != ""]
    count = 0
    for i, line in enumerate(lines):
        if "```" in line:
            count += 1
            items = line.split('`')
            if count % 2 == 1:
                lines[i] = f'<pre><code class="language-{items[-1]}">'
            else:
                lines[i] = f'<br></code></pre>'
        else:
            if i > 0:
                if count % 2 == 1:
                    line = line.replace("`", r"\`")
                    line = line.replace("<", "&lt;")
                    line = line.replace(">", "&gt;")
                    line = line.replace(" ", "&nbsp;")
                    line = line.replace("*", "&ast;")
                    line = line.replace("_", "&lowbar;")
                    line = line.replace("-", "&#45;")
                    line = line.replace(".", "&#46;")
                    line = line.replace("!", "&#33;")
                    line = line.replace("(", "&#40;")
                    line = line.replace(")", "&#41;")
                    line = line.replace("$", "&#36;")
                lines[i] = "<br>" + line
    text = "".join(lines)
    return text


def build_prompt(inputs, prompt):
    # 构建提示词
    # Build prompt for inputs
    if prompt == "":
        return inputs
    if prompt.find("{}") != -1:
        return prompt.format(inputs)
    raise gr.Error("The prompt is invalid! Please make sure your prompt contains placeholder '{}' to replace user "
                   "input.")


def build_multi_round(inputs, history, prompt):
    # 构建多轮对话提示词
    # Build multi-round prompt for inputs
    prev_rounds = ""
    for i, (query, response) in enumerate(history):
        prev_rounds += build_prompt(query, prompt)
        prev_rounds += response
    return prev_rounds + inputs


def generate(**kwargs):
    # 配置模型推理参数
    # generate function with timer and exception catcher
    gen_model = kwargs.pop("model")
    try:
        start_time = time.time()
        gen_model.generate(**kwargs)
        end_time = time.time()
        logger.info("Total time: %.2f s", (end_time-start_time))

    # pylint: disable=W0703
    except Exception as e:
        logger.error(repr(e))


def predict(inputs, bot, history):
    # 推理过程
    # predict
    streamer = TextIteratorStreamer(tokenizer=tokenizer, skip_prompt=True, skip_special_tokens=True)

    logger.info("Received user input: %s", inputs)
    bot.append((parse_text(inputs), ""))

    prompt = "<reserved_106>{}<reserved_107>"
    prompted_input = build_prompt(inputs, prompt)
    logger.info("Prompt: %s", prompt)
    logger.info("User input after prompted: %s", prompted_input)

    round_prompted_input = build_multi_round(prompted_input, history, prompt)
    logger.info("User input after multi-round prompted: %s", round_prompted_input)

    input_tokens = tokenizer(round_prompted_input)
    generation_kwargs = dict(model=model,
                             input_ids=input_tokens["input_ids"],
                             streamer=streamer,
                             do_sample=True,
                             top_k=5,
                             top_p=0.85,
                             temperature=1.0,
                             repetition_penalty=1.0,
                             max_length=512)
    thread = Thread(target=generate, kwargs=generation_kwargs)
    thread.start()

    interval_time = 0.
    output = ""
    for response in streamer:
        if response == "<ERROR>":
            raise gr.Error("An error occurred! Please make sure all the settings are correct!")
        output += response
        new_history = history + [(prompted_input, output)]

        bot[-1] = (parse_text(inputs), parse_text(output))

        interval_start = time.time()
        yield bot, new_history
        interval_end = time.time()
        interval_time = interval_time + interval_end - interval_start

    logger.info("Generate output: %s", output)
    logger.info("Web communication time: %.2f s", interval_time)


def reset_user_input():
    # 重置用户输入
    # reset user input
    return gr.update(value='')


def reset_state():
    # 状态复位
    # reset state
    return [], []

# 构建聊天Web演示
# Build Chat Web Demo
with gr.Blocks() as demo:
    gr.HTML(f"""<h1 align="center">Chat Web Demo powered by MindFormers</h1>""")
    with gr.Row():
        with gr.Column(scale=10):
            with gr.Group():
                chatbot = gr.Chatbot(label=fr"Chatbot baichuan2")
                user_input = gr.Textbox(show_label=False, placeholder="Ask something...", lines=5)
            with gr.Row():
                with gr.Column(scale=6):
                    submit_btn = gr.Button("Submit", variant="primary")
                with gr.Column(scale=6):
                    empty_btn = gr.Button("Clear")

    chat_history = gr.State([])

    submit_btn.click(predict,
                     [user_input, chatbot, chat_history],
                     [chatbot, chat_history],
                     show_progress=True)
    submit_btn.click(reset_user_input, [], [user_input])

    empty_btn.click(reset_state, outputs=[chatbot, chat_history], show_progress=True)

demo.queue().launch()
EOF
```

**Create requirements.txt:**

```bash
cat > requirements.txt << EOF
mdtex2html
EOF
```

**Upload file.**

Run the **git push** command and use the username and [Token](/my/tokens) to complete the push.

```bash
git add .
git commit -m "space init"
git branch -M main
git push -u origin main
```
