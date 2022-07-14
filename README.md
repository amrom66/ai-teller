# ai-teller

人工智能算命程序

## 原理解释

根据输入的信息，生日、星座、性别、年龄等信息，经过算命程序，生成算命结果。
输入维度：生日、星座、性别、年龄
输出维度：最终寿命 重大事件 幸福指数

## 开发教程

- 准备python3环境
- cd ~  && mkdir code && cd code
- `git clone git@github.com:linjinbao666/ai-teller.git`
- 启用项目虚拟环境 `source ./venv/bin/activate`
- git checkout -b dev ##dev建议换成自己唯一的分支名
- 开始开发
- 开发结束后使用`git push origin dev`提交代码

## 使用流程

- web页面 用户输入自己姓名 性别 年龄
- 后台随机生成输出
- 反馈到页面
