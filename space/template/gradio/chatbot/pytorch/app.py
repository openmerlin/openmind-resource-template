import os

os.environ["OPENMIND_HUB_ENDPOINT"] = "https://telecom.openmind.cn/"
import gradio as gr
from openmind import AutoModelForCausalLM, AutoTokenizer
import torch


def load_model():
    device = "npu:0"
    model_path = "openmind/baichuan2_7b_chat_pt"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(device)
    return model, tokenizer


def chat(content, history):
    if isinstance(history, list):
        history = []
    messages = [{"role": "user", "content": content}]
    response = model.chat(tokenizer, messages)
    history.append(messages)
    history.append({"role": "bot", "content": response})
    return response


if __name__ == "__main__":
    model, tokenizer = load_model()
    gr.ChatInterface(
        chat,
        title="Baichuan2_7B 对话",
        description="Baichuan 2 是百川智能推出的新一代开源大语言模型，采用 2.6 万亿 Tokens 的高质量语料训练，在权威的中文和英文 benchmark \
上均取得同尺寸最好的效果。",
        examples=["解释一下“温故而知新", "请制定一份杭州一日游计划"],
    ).launch()
