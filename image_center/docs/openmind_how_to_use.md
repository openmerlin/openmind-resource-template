## 镜像tag规则
openMind镜像tag遵循下面的格式：

CPU镜像：

 - openmind:<os_name>-python<python_version>-pytorch<pytorch_version>-openmind<openmind_version>

 - openmind:<os_name>-python<python_version>-mindspore<mindspore_version>-openmind<openmind_version>

NPU镜像：

 - openmind:<os_name>-python<python_version>-cann<cann_version>-pytorch<pytorch_version>-openmind<openmind_version>

 - openmind:<os_name>-python<python_version>-cann<cann_version>-mindspore<mindspore_version>-openmind<openmind_version>

 - openmind:<os_name>-python<python_version>-cann<cann_version>-pytorch<pytorch_version>-mindspore<mindspore_version>-openmind<openmind_version>

`openmind:latest`镜像指向同时安装MindSpore和PyTorch的最新openMind的NPU镜像，即tag为`openeuler-python3.9-cann8.0.rc2.beta1-pytorch2.1.0-mindspore2.3.1-openmind0.8.0`的openMind镜像。

可在tag页签选择您需要的镜像版本。

## 运行前准备

如果要使用NPU镜像，运行前需要安装好昇腾的固件与驱动，在[固件与驱动页面](https://www.hiascend.com/hardware/firmware-drivers/community?product=4&model=32&cann=8.0.RC1.beta1&driver=1.0.RC1.alpha)根据镜像tag中的`<cann_version>`选择对应的CANN版本，(大小写可能不一致，比如`8.0.rc1.beta1`对应`8.0.RC1.beta1`)，选择Atlas 800I A2 推理服务器或Atlas 800T A2 训练服务器，下载并安装。

## 验证

openMind容器运行成功后，在容器中执行命令：
```bash
python -c "from openmind import pipeline;classifier = pipeline("sentiment-analysis");classifier("Welcome to the openMind library!")"
```
若输出信息类似`[{'label': 'POSITIVE', 'score': 0.999705970287323}]`，则表示openMind容器运行成功。
