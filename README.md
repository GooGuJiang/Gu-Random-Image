# Gu-Random-Image (咕谷的图片随机服务😊) 

**⚠️本仓库文档未完善**

这是一个获取 `Github 仓库列表` 通过 **jsDelivr** 输出的随机图片服务

例:
[![随机图片](https://rimg.gumoe.cc)]()

# 💁‍♀️ 怎么部署?

部署分2种方式:
- Railway 无需服务器 (国内需反代理或者走 Cloudflare)
- 部署到自己服务器

## 部署到 Railway


1. 👇点击下面按钮部署本项目到 Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new?template=https://github.com/GooGuJiang/Gu-Random-Image)

2. 转到你 `Github` 下被 `Railway` 配置好的仓库，编辑 `settings.yml` 以配置变量

**请严格使用 YAML 的书写规范进行配置**

| 名称 | 描述 | 类型 | 举例 |
| ------- | ------- | ------- | ------- |
| railway_how | 是否部署在 Railway | bool | true |
| Github_User | Github 用户名 | str | GooguJiang |
| Github_Wh | Github 仓库地址| str | gu_img |
| GitHub_dz | Github 仓库内图片文件夹 | str | img |
| Cltoken | 清除缓存时的 Token | str | |

P.S. 当系统变量没得时候会自动读取配置文件补充/**请务必设置 Cltoken 避免被滥用**

3. 设置域名: 在你的 `Railway` 项目找到 `Development` -> `Domains` -> `Add Custom Domain`, 跟着步骤即可设置自定义域名

4. 访问

未完善, 待补充....

## 部署到 自己服务器

1. 确保 `python` 的版本为 3.x

2. 将本仓库 `clone` 到本地:

```bash
$ git clone https://github.com/GooGuJiang/Gu-Random-Image.git
```

3. 安装所需库

```bash
$ pip install -r requirements.txt
```

4. 配置 settings.yml

5. 启动服务器

```bash
$ python3 main.py
```

具体教程可前往我的博客:
[整了个无服务器随机图片服务](https://gmoe.cc/49.html)

# API 接口
## 获取随机图片
| 方式 | 路径 | 参数 | 返回 |
| ------- | ------- | ------- | ------- |
| GET | `/` |  | img |

## 获取图片列表
| 方式 | 路径 | 参数 | 返回 |
| ------- | ------- | ------- | ------- |
| GET | `/json` |  | json |

## 清除缓存
| 方式 | 路径 | 参数 | 返回 |
| ------- | ------- | ------- | ------- |
| GET | `/clear?token={cltoken}` | token=你的 Cltoken | json |
