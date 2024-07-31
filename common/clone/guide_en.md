1. If the repository needs to manage LFS files, you need to install git-lfs. You can view the [official documentation](https://git-lfs.com/) to install:

2. Clone this repository:

    ```bash
    git clone [git_https_url]
    ```

3. Enter the repository, update the files in the repository, and use git-lfs to track large files, which can be a certain type or a specific file name. The example is as follows:

    ```bash
    git lfs track "test.jsonl"  # Track test.jsonl file
    git lfs track "lfs/*"  # Track all files under the lfs directory
    ```

    > Files of 100MB and above must be managed using git-lfs. The repository tracks common large files by default, including `*.bin, *.safetensors, *.parquet`, etc. For details, see the .gitattributes file. These file types do not need to be tracked manually.
    > Files of 5G and above must be uploaded through tool chain, see [upload documentation](https://telecom.openmind.cn/docs/zh/openmind-hub-client/basic_tutorial/upload.html).

4. Push files:

    ```bash
    git add .
    git commit -m 'commit message'
    git push
    ```
