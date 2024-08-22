**快速上手**

这是一个基于昇腾NPU的gradio类型体验空间，您需要至少上传`app.py`和`requirements.txt`两个文件。当文件内容符合gradio和python编程规范后，空间会自动触发镜像构建，并运行gradio服务。下面是一个简单的demo：

**克隆本仓库：**

```bash
git clone [git_https_url]
cd [repo_name]
```

**创建app.py:**

```bash
cat > app.py << EOF
import torch
import gradio as gr
from openmind import AutoModelForCausalLM, AutoTokenizer


def load_model():
    # 设置推理使用的卡
    # set the device of inference
    device = 'npu:0'
    
    # 设置模型名称
    # set the model name
    model_path = "TeleAI/TeleChat-7B-pt"
    
    # 初始化分词器和模型
	# initial the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).to(device)
    return model, tokenizer

def chat(content, history):
    # 保存历史消息
    # save chat history
    if isinstance(history, list):
        list_history = history
        history = []
    for h in list_history:
        question, response = h
        history.append({"role": "user", "content": question})
        history.append({"role": "bot", "content": response})
        
    # 调用模型推理接口
 	# model inference
    response, history = model.chat(tokenizer, question=content, history=history)
    return response

if __name__ == "__main__":
    # 获得模型和分词器
    # get model and tokenizer
    model, tokenizer = load_model()
    
    # 调用`gradio`的ChatInterface接口，设置描述和示例
    # call the ChatInterface of gradio, set the description and examples
    gr.ChatInterface(chat,
                    title="Telechat_7B 对话",
                    description="星辰语义大模型TeleChat是由中国电信人工智能科技有限公司研发训练的大语言模型，采用1.5万亿 Tokens中英文高质量语料进行训练。",
                    examples=['解释一下“温故而知新', '请制定一份杭州一日游计划']
                 ).launch(debug=True)
EOF
```

**创建requirements.txt**

```bash
cat > requirements.txt << EOF
gradio==4.27.0
accelerate==0.28.0
transformers==4.38.0
sentencepiece==0.1.98
einops==0.8.0
EOF
```

**上传文件**

git push并使用用户名和[令牌](/my/tokens)完成推送:

```bash
git add .
git commit -m "space init"
git branch -M main
git push -u origin main
```
