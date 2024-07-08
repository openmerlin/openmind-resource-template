Download dataset.

```bash
git lfs install
git clone [link]
```



To skip downloading LFS-based large files and retain only the LFS pointers,

add `GIT_LFS_SKIP_SMUDGE=1:` before the git clone command:
```bash
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone [link]
```