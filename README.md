# Gu-Random-Image (咕谷的图片随机服务😊) 
# 文档未完善

这是一个获取 Github 仓库列表通过 jsDelivr 输出的随机图片服务
例:
[![随机图片](https://rimg.gumoe.cc)]()

## 💁‍♀️ 怎么部署?

部署分2种方式:
- Railway 无需服务器(国内需反代理或者走Cloudflare)
- 部署到自己服务器

### 部署到 Railway
👇首先先点击下面按钮部署本项目到  Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new?template=https%3A%2F%2Fgithub.com%2Frailwayapp%2Fexamples%2Ftree%2Fmaster%2Fexamples%2Fflask)

#### 部署方式
- 设置变量

| 变量 | 作用 |
| ------- | ------- |
| railway_how | 是否部署在 Railway |
| Github_User | Github 用户名 |
| Github_Wh |Github 仓库地址|
| GitHub_dz | Github 仓库内图片文件夹 |
| Cltoken |清除缓存时的Token|

Ps: 当系统变量没得时候会自动读取配置文件补充/**Cltoken 请务必设置避免被滥用**
- 设置域名 
- 访问
待补充....

### 部署到 自己服务器
- 安装库 `pip install -r requirements.txt`
- 修改 set.yml
- 启动程序 `python3 main.py`

具体教程可前往我的博客:
https://gmoe.cc/49.html
