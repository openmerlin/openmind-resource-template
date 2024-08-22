import mindspore
from openmind import AutoModelForCausalLM, AutoTokenizer
import gradio as gr

mindspore.set_context(mode=0, device_id=0)

tokenizer = AutoTokenizer.from_pretrained(
    "Baichuan/Baichuan2_7b_chat_ms", trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    "Baichuan/Baichuan2_7b_chat_ms", trust_remote_code=True
)


def generate_response(input_text):
    inputs = tokenizer(input_text)["input_ids"]
    outputs = model.generate(inputs, max_new_tokens=512, do_sample=True, top_k=3)
    response = tokenizer.decode(
        outputs, skip_special_tokens=True, clean_up_tokenization_spaces=True
    )
    return response[0]


def clear_textbox():
    return "", ""


with gr.Blocks() as demo:
    gr.Markdown("# Chat with Model")

    with gr.Row():
        input_box = gr.Textbox(placeholder="input", show_label=False)
        output_box = gr.Textbox(
            placeholder="output", show_label=False, interactive=False
        )

    with gr.Row():
        send_btn = gr.Button(value="Send")
        clear_btn = gr.Button(value="Clear")

    send_btn.click(generate_response, inputs=input_box, outputs=output_box)
    clear_btn.click(clear_textbox, outputs=[input_box, output_box])

demo.launch()
