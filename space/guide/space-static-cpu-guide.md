**快速上手**

这是一个基于CPU的static类型体验空间，您需要至少上传文件`index.html`。当文件内容符合html规范后，空间会自动触发镜像构建，并运行nginx静态html服务。下面是一个简单的demo：

克隆本仓库：

```bash
git clone [git_https_url]
cd [repo_name]
```

**创建index.html:**

```bash
cat > index.html << EOF
<!DOCTYPE html>
<html>
    <head>
        <title>Example Demo</title>
    </head>
    <body>
        <p>This is an example of a simple HTML page with one paragraph.</p>
    </body>
</html>
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
