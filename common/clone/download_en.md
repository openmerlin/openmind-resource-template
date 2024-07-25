Download this [module]:

```bash
git lfs install
git clone [git_https_url]
```

If you want to skip downloading large LFS files (keep only LFS pointers), please add `GIT_LFS_SKIP_SMUDGE=1` before the git clone command:

```bash
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone [git_https_url]
```

When cloning a private repository and pushing submissions, the command line will prompt you to enter your account password. You need to enter an access token in the password field. You can click [Create a token] (/my/tokens). If the repository involves lfs files, multiple verifications may be required.

```
Username for 'https://telecom.openmind.cn': username
Password for 'https://username@telecom.openmind.cn': access token
```