**Get started.**

This is a Gradio space running on Ascend NPUs. Upload at least the `app.py` and `requirements.txt` files that comply with the Gradio and Python programming specifications. Then the space automatically triggers image building and runs Gradio. See the demo below:

**Clone this repository:**

```bash
git clone [link]
cd [repo_name]
```

**Create app.py:**

```bash
cat > app.py << EOF
import gradio as gr
import mindspore as ms
def add(num1, num2):
    num1 = ms.Tensor(num1)
    num2 = ms.Tensor(num2)
    result = num1 + num2
    return int(result)
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
