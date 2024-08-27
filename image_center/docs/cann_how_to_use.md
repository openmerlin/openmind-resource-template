## 镜像tag规则
CANN镜像tag遵循下面的格式：

 - cann:<os_name>-python<python_version>-cann<cann_version>

可在tag页签选择您需要的镜像版本。

## 运行前准备

运行前需要安装好昇腾的固件与驱动，在[固件与驱动页面](https://www.hiascend.com/hardware/firmware-drivers/community?product=4&model=32&cann=8.0.RC1.beta1&driver=1.0.RC1.alpha)选择对应的CANN版本，选择Atlas 800I A2 推理服务器或Atlas 800T A2 训练服务器，下载并安装。

## 验证

CANN容器运行成功后，在容器中执行`npu-smi info`命令，若输出信息中包含`Device`字段，则表示CANN容器运行成功。
