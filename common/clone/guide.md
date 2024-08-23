1. 若仓库需要管理LFS文件，则需安装git-lfs，可查看[官方文档](https://git-lfs.com/)进行安装。

2. 克隆本仓库：

    ```bash
    git clone [git_https_url]
    ```

3. 进入仓库，更新仓库内文件，并使用git-lfs追踪大型文件，可以是某一类型，也可以是具体的文件名。示例如下：

    ```bash
    git lfs track "test.jsonl"  # 追踪test.jsonl文件
    git lfs track "lfs/*"  # 追踪lfs目录下的所有文件
    ```

    > 100MB及以上的文件必须使用git-lfs管理。仓库默认已追踪常见的大型文件，包括`*.bin、*.safetensors、*.parquet`等，具体可查看.gitattributes文件，这些文件类型无需再手动追踪。
    > 5G及以上的文件无法使用git上传，请使用工具链上传，详阅[《上传文档》](/docs/zh/openmind-hub-client/basic_tutorial/upload.html)。

4. 推送文件：

    ```bash
    git add .
    git commit -m 'commit message'
    git push
    ```

更多上传和下载方式，可阅读 openMind Hub Client[《快速入门》](/docs/zh/openmind-hub-client/quick_start.html)。
