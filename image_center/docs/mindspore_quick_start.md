对于cpu镜像，可以直接运行

```bash
docker run --name torch -it --rm registry.modelers.cn/base_image/mindspore:openeuler-python3.8-mindspore2.3.0rc1 bash
```

mindspore:latest是mindspore2.3.0rc1版本的npu镜像，运行前需要安装好固件与驱动，在[固件与驱动页面](https://www.hiascend.com/hardware/firmware-drivers/community?product=4&model=32&cann=8.0.RC1.beta1&driver=1.0.RC1.alpha)选择CANN版本8.0.RC1.beta1，选择Atlas 800I A2 推理服务器或Atlas 800T A2 训练服务器，下载并安装，成功后运行下面的命令。

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
    -ti registry.modelers.cn/base_image/mindspore bash
```