import torch
import json
import argparse
import gradio as gr
import os

os.environ["OPENMIND_HUB_ENDPOINT"] = "https://telecom.openmind.cn/"

from chatways import SimpleChatBot

# Step 1. Configuration
CSS = """#chatbot {
    height: 60vh !important;
    display: flex;
    flex-direction: column-reverse;
}
"""

HEADER = """# Chat

This is a simple chat application that uses a language model to generate responses.
"""

OM_PARAMETERS = [
    ("temperature", 1.0, 0.0, 2.0, 0.01),
    ("top_k", 50, 0, 100, 1),
    ("top_p", 1.0, 0.0, 2.0, 0.01),
    ("max_new_tokens", 512, 0, 1024, 1),
]


# Step 2. Argument Parsing
def parse_args():
    parser = argparse.ArgumentParser(description="Simple Chat Application")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        default="127.0.0.1",
        help="Default address is 127.0.0.1",
    )
    parser.add_argument(
        "-p", "--port", type=int, default=7860, help="Default port is 7860"
    )
    parser.add_argument(
        "-le", "--llm-engine", type=str, default=None, help="The LLM engine to use"
    )
    parser.add_argument(
        "-lm", "--llm-model", type=str, default=None, help="The LLM model path"
    )
    parser.add_argument(
        "-lc",
        "--llm-model-config",
        type=object,
        default={"torch_dtype": torch.bfloat16, "device_map": "npu:0"},
        help="The LLM model configuration in JSON format",
    )
    return parser.parse_args()


args = parse_args()

# Step 3. Bot initialization
bot = SimpleChatBot(
    llm_config={
        "engine": "openmind",
        "model": "openmind/baichuan2_7b_chat_pt",
        "model_config": args.llm_model_config,
    }
)


# Step 4. Callbacks definition
def get_generation_config(components):
    if args.llm_engine == "openmind" or args.llm_engine is None:
        parameters = OM_PARAMETERS

    parameter_components = components[: int(len(components) / 2)]
    availabel_components = components[int(len(components) / 2) :]
    generation_config = {}
    for parameter, parameter_component, availabel_component in zip(
        parameters, parameter_components, availabel_components
    ):
        if availabel_component:
            parameter_component = None
        generation_config.update({parameter[0]: parameter_component})
    return generation_config


def respond(message, history, system_prompt, stream, *components):
    generation_config = get_generation_config(components)
    response = bot.chat(
        message=message,
        history=history,
        system_prompt=system_prompt,
        generation_config=generation_config,
        stream=stream,
    )
    history.append([message, ""])
    if stream:
        for chunk in response:
            if chunk is not None:
                history[-1][1] += chunk
                yield "", history
    else:
        history[-1][1] = response
        yield "", history


def clean_conversation():
    return "", []


def create_component(label, value, minimum, maximum, step):
    return gr.Slider(
        label=label,
        value=value,
        minimum=minimum,
        maximum=maximum,
        step=step,
        interactive=True,
    )


def enable_parameter_slider():
    return False


# Step 5. Gradio Interface
with gr.Blocks(css=CSS) as demo:
    gr.Markdown(HEADER)

    with gr.Row():
        system_prompt = gr.Textbox(
            placeholder="System Prompt", show_label=False, scale=9
        )
        stream_component = gr.Checkbox(
            value=True, label="Stream", interactive=True, scale=1
        )

    chatbot = gr.Chatbot(elem_id="chatbot", show_label=False, show_copy_button=True)

    with gr.Row():
        inputs = gr.Textbox(placeholder="Input", show_label=False, scale=8)
        clean_btn = gr.Button(scale=1, value="Clean", variant="stop")
        send_btn = gr.Button(scale=1, value="Send", variant="primary")

    with gr.Accordion("Parameters", open=False):
        if args.llm_engine == "openmind" or args.llm_engine is None:
            parameters = OM_PARAMETERS

        availabel_components = []
        parameter_components = []
        index = 0
        while index < len(parameters):
            with gr.Row():
                with gr.Column():
                    parameter_components.append(create_component(*parameters[index]))
                    availabel_components.append(
                        gr.Checkbox(label="Disable", value=True, interactive=True)
                    )
                    index += 1
                if index < len(parameters):
                    with gr.Column():
                        parameter_components.append(
                            create_component(*parameters[index])
                        )
                        availabel_components.append(
                            gr.Checkbox(label="Disable", value=True, interactive=True)
                        )
                        index += 1

    inputs.submit(
        respond,
        [
            inputs,
            chatbot,
            system_prompt,
            stream_component,
            *(parameter_components + availabel_components),
        ],
        [inputs, chatbot],
    )
    send_btn.click(
        respond,
        [
            inputs,
            chatbot,
            system_prompt,
            stream_component,
            *(parameter_components + availabel_components),
        ],
        [inputs, chatbot],
    )
    clean_btn.click(clean_conversation, outputs=[inputs, chatbot])

    for parameter_component, availabel_component in zip(
        parameter_components, availabel_components
    ):
        parameter_component.change(
            fn=enable_parameter_slider, outputs=availabel_component
        )

if __name__ == "__main__":
    demo.launch()
