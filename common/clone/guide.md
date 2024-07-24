1. 若仓库需要管理LFS文件，则需安装GIT LFS，可查看[官方文档](https://git-lfs.com/)或使用如下方式进行安装：

    + apt/deb: `sudo apt-get install git-lfs`
    + yum/rpm: `sudo yum install git-lfs`

    安装完成后使用`git lfs install`为当前用户激活GIT LFS，此命令每个用户只需执行一次。

2. 克隆本仓库：

    ```bash
    git clone [git_https_url]
    ```

3. 进入仓库，更新仓库内文件，并使用GIT LFS追踪大型文件，可以是某一类型，也可以是具体的文件名。示例如下：

    ```bash
    git lfs track "test.jsonl"  # 追踪test.jsonl文件
    git lfs track "lfs/*"  # 追踪lfs目录下的所有文件
    ```

    > 100MB及以上的文件必须使用GIT LFS管理。仓库默认已追踪常见的大型文件，包括`*.bin、*.safetensors、*.parquet`等，具体可查看.gitattributes文件，这些文件类型无需再手动追踪。

4. 推送文件：

    ```bash
    git add .
    git commit -m 'commit message'
    git push
    ```

克隆私仓以及推送提交时，命令行会出现如下账号密码验证步骤，其中password为访问令牌，[点此创建令牌](/my/tokens)。若仓库涉及lfs文件，则可能需要多次验证。

```
Username for 'https://telecom.openmind.cn': username
Password for 'https://username@telecom.openmind.cn':访问令牌
```
