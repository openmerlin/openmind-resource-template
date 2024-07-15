Enable Git LFS:
```bash
git lfs install
```

Clone this repository:

```bash
git clone [git_https_url]
```

After a local file is updated, run the following commands to push the file:
```bash
git add .
git commit -m "commit message"
git branch -M main
git push -u origin main
```

File push requires a username and token. [Create a token](/my/tokens). For large files, git push may take a long time to complete.