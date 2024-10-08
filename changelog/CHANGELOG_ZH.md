# 更新日志


## 1.3.0版本 - 2024-09-27

### 新板块
#### 🌟 比赛板块

比赛板块汇聚了高校AI大赛的赛题介绍、报名、赛程安排等比赛功能。
- 比赛详情：支持查看举办的比赛的介绍、详细规则。
- 比赛报名：支持用户报名参加比赛。

快来[这里](https://aic.modelers.cn/)看看当前火热举办的大赛吧！

### 新特性
#### ✨ 组织板块
- 在组织聚合页面新增“我的组织”快速入口。

#### ✨ 体验空间板块
- 镜像选择：创建体验空间时，支持选择基础镜像的openmind版本。
- 封面生成app：官方体验空间-[封面生成app](https://modelers.cn/spaces/space-official-infra/space-cover-generator)上线，可以根据提示词生成个性化封面。

#### ✨ 文件托管板块
- commit记录查看：支持查看文件的commit历史记录，便于版本控制。

#### ✨ 镜像中心板块
- 新版本发布：openMind 0.8版本镜像已发布，欢迎前往镜像中心下载使用。
### bug修复
#### 🐛 第三方账号登录
- 修复第三方账号注册问题：从第三方账号进行注册时，进行信息完善时报错：手机号已被使用，导致无法登录，目前此问题已得到了解决。

### 改进
####  🛠 空间离线体验
- 新增了镜像大小和模型权重文件大小的显示，帮助用户更好地管理离线空间。



## 1.2.0版本 - 2024-09-14

### 新板块
#### 🌟 社区动态版块
您可以在社区动态板块了解魔乐社区的最新咨询。

快来[这里](https://modelers.cn/updates)看看社区有哪些新动态吧！

### 新特性
#### ✨ 数据集板块
- 新增数据集BOM的实验性支持，支持展示数据集名称、供应商等基本信息。
#### ✨ 模型库板块
- 新增模型BOM的实验性支持，支持展示模型依赖的基础模型、依赖的数据集、软件等信息，以提升模型透明度，可重复构建性。

## 1.1.0版本 - 2024-09-02
### 新特性
#### ✨ 模型库板块
- 模型可用性测试：支持模型可用性测试的暂停功能。

## 1.0.0版本 - 2024-08-28
🎉 Hello, World! 

魔乐社区1.0.0版本正式上线，您可以访问[体验地图](https://modelers.cn/roadmaps)，了解社区提供的整体能力。
### 新板块
#### 🌟 模型库版块
模型库汇集了大量用于机器学习任务的模型，您可以在这里下载最新、最流行的模型，也可以创建自己的模型。
- 模型总览：支持通过任务、框架等标签快速筛选模型，支持通过模型专区看到更多精选模型。
- 基础功能：支持添加介绍、文件、讨论区等，帮助您全方位展示您的模型。
- 模型上传与下载：支持Git（含LFS）、Hub Client等场景方式上传、下载模型。
- 模型可用性测试：支持通过[模型可用性测试](https://modelers.cn/docs/zh/community/models/verifying_models.html)验证模型在昇腾算力上的运行情况。

快来[这里](https://modelers.cn/models)看看社区有哪些模型，并尝试[创建](https://modelers.cn/models/new)一个新的模型吧！

#### 🌟 数据集版块
数据集汇集了多领域的数据集，可用于翻译、语音识别和图像分类等任务，您可以在这里下载最新、最流行的数据集，也可以创建自己的数据集。
- 数据集总览：支持通过任务、条目数、领域等标签快速筛选数据集。
- 基础功能：支持添加介绍、文件、讨论区等，帮助您全方位展示您的数据集。
- 数据集上传与下载：支持Git（含LFS）、Hub Client等场景方式上传、下载数据集。

快来[这里](https://modelers.cn/datasets)看看社区有哪些数据集，并尝试[创建](https://modelers.cn/datasets/new)一个新的数据集吧！

#### 🌟 体验空间板块
体验空间是演示应用程序的一站式平台，汇集了多种类型的AI应用，您可以自行构建体验空间，展示研究成果，也可以使用其他用户贡献的应用程序，和更多用户一起体验、探索、学习和互动。
- 体验空间总览：支持通过任务、算力资源、收藏量等标签快速筛选体验空间，支持展示精选空间。
- 基础功能：支持添加介绍、文件、讨论区等，帮助您全方位展示您的体验空间。
- 部署与配置：支持部署[Gradio](https://modelers.cn/docs/zh/community/spaces/deploying_spaces/deploying_a_gradio_space.html)，[Static](https://modelers.cn/docs/zh/community/spaces/deploying_spaces/deploying_a_static_space.html)，[Application](https://modelers.cn/docs/zh/community/spaces/deploying_spaces/deploying_a_application_space.html)体验空间，支持[配置](https://modelers.cn/docs/zh/community/spaces/advanced_functions/dependencies_applicable_to_spaces.html)体验空间规格，当前支持CPU、NPU两种算力资源，支持PyTorch、MindSpore两种基础环境。
- 使用：作支持通过在线和离线体验两种方式[使用](https://modelers.cn/docs/zh/community/spaces/using_spaces.html)体验空间。

快来[这里](https://modelers.cn/spaces)看看社区有哪些体验空间，并尝试[创建](https://modelers.cn/spaces/new)一个新的体验空间吧！
#### 🌟 讨论区板块
讨论区鼓励社区成员就相关内容进行讨论，分享观点、提出问题和解决问题。
- 基础功能：支持在某个模型/数据集/体验空间的讨论区中反馈问题，解答问题提和同步信息

快去你感兴趣的模型、数据集、体验空间下分享你的观点吧！

#### 🌟 组织板块
组织帮助用户根据实际需求对不同账号进行分组管理，能够有效地集中管理用户所拥有的各类数据集、模型库及体验空间。
- 组织总览：支持通过企业、学校、机构等标签快速筛选组织。
- 基础功能：支持创建、加入或退出组织，通过介绍、体验空间、模型、数据集来全方位展示您的组织。
- 组织管理：组织管理员可以集中管理数据集、模型库和体验空间，组织管理员可灵活设置成员权限，确保资源安全，组织管理员可邀请用户加入。
- 组织认证：组织管理员可以对组织进行认证。

快来[这里](https://modelers.cn/organizations)看看社区有哪些组织，并尝试[创建](https://modelers.cn/organizations/new)一个组织吧！


#### 🌟 镜像中心板块

镜像中心开放了可用于CPU、NPU算力资源的CANN、Pytorch、MindSpore、openMind的基础镜像。
- 基础功能：提供各领域对应的基础镜像和详细介绍，支持通过docker pull方式拉取镜像。

快来[这里](https://modelers.cn/images)查看你感兴趣的镜像吧！

#### 🌟 个人账号板块
个人账号板块提供用户账号注册、登录、管理的相关功能。
- 账号注册：支持通过手机号、[GitHub](https://github.com/)、[Gitee](https://gitee.com/)进行注册。
- 账号登录：支持通过手机号、[GitHub](https://github.com/)、[Gitee](https://gitee.com/)以及密码进行登录。
- 个人中心：支持在个人中心进行账号管理（如上传自定义头像、更新签名、绑定邮箱、账号注销），个人动态查看等。

快去你的个人中心更新一次个性签名吧！