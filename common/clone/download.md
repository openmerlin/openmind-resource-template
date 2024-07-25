下载该[module]：

```bash
git lfs install
git clone [git_https_url]
```

如果您想跳过LFS大文件的下载（只保留LFS指针），请在git clone命令前添加`GIT_LFS_SKIP_SMUDGE=1`：

```bash
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone [git_https_url]
```

克隆私仓以及推送提交时，命令行会出现输入账号密码的提示，其中password处需要输入访问令牌，可以点此[创建令牌](/my/tokens)。若仓库涉及lfs文件，则可能需要多次验证。

```
Username for 'https://telecom.openmind.cn': username
Password for 'https://username@telecom.openmind.cn':访问令牌
```
