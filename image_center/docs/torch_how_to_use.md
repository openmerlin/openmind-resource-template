## 镜像tag规则
PyTorch镜像tag遵循下面的格式：

NPU镜像：

 - pytorch:<os_name>-python<python_version>-cann<cann_version>-pytorch<pytorch_version>

可在tag页签选择您需要的镜像版本。

## 运行前准备

如果要使用NPU镜像，运行前需要安装好昇腾的固件与驱动，在[固件与驱动页面](https://www.hiascend.com/hardware/firmware-drivers/community?product=4&model=32&cann=8.0.RC1.beta1&driver=1.0.RC1.alpha)根据镜像tag中的`<cann_version>`选择对应的CANN版本，(大小写可能不一致，比如`8.0.rc1.beta1`对应`8.0.RC1.beta1`)，选择Atlas 800I A2 推理服务器或Atlas 800T A2 训练服务器，下载并安装。

## 验证

PyTorch容器运行成功后，在容器中执行命令：

```bash
python -c "import torch;x = torch.rand(5, 3);print(x)"
```

若输出信息类似:

```
tensor([[0.3380, 0.3845, 0.3217],
        [0.8337, 0.9050, 0.2650],
        [0.2979, 0.7141, 0.9069],
        [0.1449, 0.1132, 0.1375],
        [0.4675, 0.3947, 0.1426]])
```

则表示Pytorch容器运行成功。
