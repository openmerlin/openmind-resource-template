**快速上手**

这是一个基于CPU的gradio类型体验空间，您需要至少上传`app.py`和`requirements.txt`两个文件。当文件内容符合gradio和python编程规范后，空间会自动触发镜像构建，并运行gradio服务。下面是一个简单的demo：

**克隆本仓库：**

```bash
git clone [git_https_url]
cd [repo_name]
```

**创建app.py:**

```bash
cat > app.py << EOF
import gradio as gr
def greet(name):
    return "Hello " + name
app = gr.Interface(fn=greet, inputs="text", outputs="text")
app.launch()
EOF
```

**创建requirements.txt**

```bash
cat > requirements.txt << EOF
gradio
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
