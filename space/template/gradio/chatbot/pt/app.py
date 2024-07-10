import torch
from openmind import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
import gradio as gr


tokenizer = AutoTokenizer.from_pretrained(
    "openmind/baichuan2_7b_chat_pt", use_fast=False, trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    "openmind/baichuan2_7b_chat_pt",
    device_map="npu:0",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
)
model.generation_config = GenerationConfig.from_pretrained(
    "openmind/baichuan2_7b_chat_pt"
)


def generate_response(input_text):
    messages = [{"role": "user", "content": input_text}]
    response = model.chat(tokenizer, messages)
    return response


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
