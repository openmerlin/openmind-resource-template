首先激活lfs：
```bash
git lfs install
```

克隆本仓库：

```bash
git clone [link]
```

本地文件更新后，可使用以下命令完成推送：
```bash
git add .
git commit -m "commit message"
git branch -M main
git push -u origin main
```

推送时需要使用用户名及令牌，[点此创建令牌](/my/tokens)。当存在大文件时，git push需等待一段时间完成。