**Get started.**

This is a Gradio space running on CPUs. Upload at least the `app.py` and `requirements.txt` files that comply with the Gradio and Python programming specifications. Then the space automatically triggers image building and runs Gradio. See the demo below:

**Clone this repository:**

```bash
git clone [git_https_url]
cd [repo_name]
```

**Create app.py:**

```bash
cat > app.py << EOF
import gradio as gr
def greet(name):
    return "Hello" + name
app = gr.Interface(fn=greet, inputs="text", outputs="text")
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
