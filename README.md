# ai-teller

人工智能算命程序

## 原理解释

根据输入的信息，生日、星座、性别、年龄等信息，经过算命程序，生成算命结果。
输入维度：生日、星座、性别、年龄
输出维度：最终寿命 重大事件 幸福指数

## 功能列表

- 命令行CLI功能:
  - init: 初始化算命程序，生成算命数据库
  - config: 配置算命程序，设置算命数据库路径
  - server: 启动算命程序，后台运行web服务器
- web网页功能:
  - 人脸算命: 在线算命，调用摄像头，拍照，计算算命结果
  - 视频算命: 在线算命，调用视频，计算算命结果
  - 离线算命: 离线算命，用户输入参数，读取算命数据库，计算算命结果
  - 前途预测: 前途预测，预测人生大事

## 开发教程

- 准备python3环境
- cd ~ && mkdir code && cd code
- `git clone git@github.com:amrom66/ai-teller.git`
- python3 -m venv .venv
- 启用项目虚拟环境 `source .venv/bin/activate`
- export mybranch=dev-${RANDOM}
- git checkout -b ${mybranch}
- 开始开发
- 开发结束后使用`git push origin ${mybranch}`提交代码

### 注意事项

由于`main`分支和`dev`分支设置为保护分支，所以需要各自推送到各自的分支，然后通过pr合并到`dev`主分支。
`${mybranch}` 此处表示随机出来的一个名字，建议换成自己唯一的分支名

## CLI使用

- `python main.py server`启动web服务器

## 使用流程

- web页面 用户输入自己姓名 性别 年龄
- 后台随机生成输出
- 反馈到页面
