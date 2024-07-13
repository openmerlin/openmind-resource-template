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
import gradio as gr
import torch
import torch_npu
def add(num1, num2):
    num1 = torch.tensor(num1).npu()
    num2 = torch.tensor(num2).npu()
    result = num1 + num2
    print(result)
    return result.cpu().item()
app = gr.Interface(
    add,
    ["number", "number"],
    "number",
)
app.launch()
EOF
```

**Create requirements.txt:**

```bash
cat > requirements.txt << EOF
gradio
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
