对于cpu镜像，可以直接运行：

```bash
docker run --name torch -it --rm registry.modelers.cn/base_image/mindspore:openeuler-python3.8-mindspore2.3.0rc1 bash
```

对于昇腾NPU镜像，需要先安装昇腾NPU驱动，然后运行：
```bash
docker run \
    --name mindspore \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -ti registry.modelers.cn/base_image/mindspore:latest bash
```

本命令的`mindspore:latest`镜像包含的是`mindspore2.3.0rc1`版本。
