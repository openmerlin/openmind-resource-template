1. If the repository needs to manage LFS files, you need to install GIT LFS. You can view the [official documentation](https://git-lfs.com/) or use the following method to install:

    + apt/deb: `sudo apt-get install git-lfs`
    + yum/rpm: `sudo yum install git-lfs`

    After the installation is complete, use `git lfs install` to activate GIT LFS for the current user. This command only needs to be executed once for each user.

2. Clone this repository:

    ```bash
    git clone [git_https_url]
    ```

3. Enter the repository, update the files in the repository, and use GIT LFS to track large files, which can be a certain type or a specific file name. The example is as follows:

    ```bash
    git lfs track "test.jsonl"  # Track test.jsonl file
    git lfs track "lfs/*"  # Track all files under the lfs directory
    ```

    > Files of 100MB and above must be managed using GIT LFS. The repository tracks common large files by default, including `*.bin, *.safetensors, *.parquet`, etc. For details, see the .gitattributes file. These file types do not need to be tracked manually.

4. Push files:

    ```bash
    git add .
    git commit -m 'commit message'
    git push
    ```

**Note**：

When cloning a private repository and pushing a commit, the command line will prompt you to enter your account password. You need to enter an access token in the password field. You can click [Create a token] (/my/tokens). If the repository involves lfs files, multiple verifications may be required.

```
Username for 'https://telecom.openmind.cn': username
Password for 'https://username@telecom.openmind.cn': access token
```
