openmind-resource-template openmind使用的模型 数据集 体验空间相关的readme。 体验空间的对应的模版。

- 体验空间
    space app 相关的template 目录结构 必须要跟前台参数一一对应 比如gradio下chatbot 对应 gradio/chatbot目录 一律小写

~~~
.
├── dataset                                  ## 数据集相关模版 owner: xxx
│   ├── clone                                ## 数据集下载数据集相关模版 owner: xxx 
│   └── openmind                             ## 数据集use inf dataset owner: xxx
├── model                                    ## 模型相关模版 owner: xxx
│   ├── clone                                ## 模型下载相关模版 owner: xxx
│   └── openmind                             ## 模型use in openMind owner: xxx
└── space                                    ## 体验空间相关模版 owner: xxx
    ├── clone                                ## 体验空间下载源码模版 owner: xxx
    └── template                             ## 体验空间相关模版 owner: xxx
        ├── gradio                           ## Gradio相关模版 owner: xxx
        │   ├── chatbot                      ## chatbot owner: xxx
        │   ├── cpu                          ## cpu owner: xxx
        │   └── npu                          ## npu owner: xxx
        │       ├── mindspore
        │       └── torch
        └── static                           ## static 相关模版 owner: xxx
            └── cpu                          ## cpu owner: xxx

 ~~~