Download this [module].

```bash
git lfs install
git clone [git_https_url]
```
To bypass downloading LFS-based large files and retain only the LFS pointers, add `GIT_LFS_SKIP_SMUDGE=1:` before the `git clone` command.
```bash
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone [git_https_url]
```