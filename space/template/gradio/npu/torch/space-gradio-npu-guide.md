**快速上手**

这是一个基于昇腾NPU的gradio类型体验空间，您需要至少上传`app.py`和`requirements.txt`两个文件。当文件内容符合gradio和python编程规范后，空间会自动触发镜像构建，并运行gradio服务。下面是一个简单的demo：

**克隆本仓库：**

```bash
git clone [link]
cd [repo_name]
```

**创建app.py:**

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
