import os

os.environ["OPENMIND_HUB_ENDPOINT"] = "https://telecom.openmind.cn"
import gradio as gr
from openmind import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
import torch


def load_model():
    device = "npu:0"
    model_path = "TeleAI/TeleChat-7B-pt"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(device)
    return model, tokenizer


def chat(content, history):
    _history = []
    _history.append([content, ""])
    if isinstance(history, list):
        list_history = history
        history = []
    for h in list_history:
        question, response = h
        history.append({"role": "user", "content": question})
        history.append({"role": "bot", "content": response})
    streamer = model.chat(tokenizer, question=content, history=history, stream=True)
    for new_text in streamer:
        _history[-1][1] += new_text[0]
        yield _history[-1][1]


if __name__ == "__main__":
    model, tokenizer = load_model()
    gr.ChatInterface(
        chat,
        title="Telechat_7B 对话",
        description="星辰语义大模型TeleChat是由中电信人工智能科技有限公司研发训练的大语言模型，采用1.5万亿 Tokens中英文高质量语料进行训练。",
        examples=["解释一下“温故而知新", "请制定一份杭州一日游计划"],
    ).launch(debug=True)
