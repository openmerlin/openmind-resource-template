如果有NPU设备，需要先安装昇腾NPU固件和驱动，然后运行：
```bash
docker run \
    --name pytorch \
    --device /dev/davinci0 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -ti registry.modelers.cn/base_image/pytorch:ubuntu-python3.8-cann8.0.rc1.beta1-pytorch2.2.0 bash
```
