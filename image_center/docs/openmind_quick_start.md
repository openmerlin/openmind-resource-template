如果只有CPU，可以直接运行

```bash
docker run --name openmind -it registry.modelers.cn/base_image/openmind:openeuler-python3.9-pytorch2.1.0-openmind0.8.0 bash
```

如果有NPU设备，需要先安装昇腾NPU驱动，然后运行：
```bash
docker run \
    --name openmind \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -ti registry.modelers.cn/base_image/openmind:latest bash
```

`openmind:latest`镜像指向同时安装MindSpore和PyTorch的最新openMind的NPU镜像，对应软件版本为`openmind0.8.0`和`cann8.0.rc2.beta1`。
