在一个已安装好昇腾驱动的Linux环境中执行下面的命令，运行并进入CANN容器：

```bash
docker run \
    --name cann \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -ti registry.modelers.cn/base_image/cann:latest bash
```

本命令所使用的`cann:latest`镜像的CANN版本为`8.0.RC1.beta1`。
