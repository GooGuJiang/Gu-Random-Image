from flask import Flask, jsonify, redirect, abort, request
import os
import requests
import json
import time
import random
import yaml
import urllib.parse

def now_time():
    # 获得当前天
    now = int(time.time())
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%d", timeArray)
    return otherStyleTime

def re_loadyml(name): # 读取配置文件
    with open('./settings.yml', 'r', encoding='utf-8') as f:
            bottok = yaml.load(f.read(), Loader=yaml.FullLoader)
            if bottok['railway_how']:
                return os.getenv(name, default=bottok[name])
            else:
                return bottok[name]

def fileTime(file):
    return time.strftime("%d",time.localtime(os.path.getmtime(file))) # 获取创建天数

def main_json():
    try:
        if not os.path.isfile('./github.json'): # 检测文件是否存在
            jsonfile = open('./github.json', 'w')
            jsonfile.close()
            url = 'https://api.github.com/repos/{github_user}/{github_wh}/contents/{github_dz}'.format(
                github_user=str(re_loadyml('Github_User')),
                github_wh=str(re_loadyml('Github_Wh')),
                github_dz=str(re_loadyml('GitHub_dz'))
            )
            res = requests.get(url)
            uesr_text = json.loads(res.text)
            ok_json = eval(json.dumps(uesr_text))
            jsonload = ''
            fout = open('./github.json', 'a', encoding='utf8')
            fout.write('[')
            for i in range(0, len(ok_json)):
                img_name = urllib.parse.quote(ok_json[i]["name"])
                data = {
                'name' : img_name
                }
                if i != len(ok_json)-1:
                    fout.write(str(json.dumps(data))+",")
                else:
                    fout.write(str(json.dumps(data)))

            fout.write(']')
            fout.close()
        else:
            if fileTime('./github.json') != now_time(): # 检测文件是否过期
                print('文件过期开始更新')
                os.remove(./github.json')
                json_newfile = open('./github.json','w')
                json_newfile.close()
                
                url = 'https://api.github.com/repos/{github_user}/{github_wh}/contents/{github_dz}'.format(
                    github_user=str(re_loadyml('Github_User')),
                    github_wh=str(re_loadyml('Github_Wh')),
                    github_dz=str(re_loadyml('GitHub_dz'))
                )
                res = requests.get(url)
                uesr_text = json.loads(res.text)
                ok_json = eval(json.dumps(uesr_text))
                img_name = []
                jsonload = ''
                fout = open('./github.json', 'a', encoding='utf8')
                fout.write('[')
                for i in range(0, len(ok_json)):
                    img_name = urllib.parse.quote(ok_json[i]['name'])
                    data = {
                    'name' : img_name
                    }
                    if i != len(ok_json)-1:
                        fout.write(str(json.dumps(data))+",")
                    else:
                        fout.write(str(json.dumps(data)))
                
                fout.write(']')
                fout.close()

                print(jsonload)
                

            else:
                pass
        return True
    except:
        return False

# 主程序↓


app = Flask(__name__)


@app.route('/')
def index():
    if main_json() == True:
        with open('./github.json', 'r',encoding='utf-8') as lb:
            img_list = lb.read()

        ok_img_list = json.loads(img_list)
        rsp = redirect('#')
        rsp.headers['Location'] = 'https://cdn.jsdelivr.net/gh/{github_user}/{github_wh}/{github_dz}/{name}'.format(
                    github_user=str(re_loadyml('Github_User')),
                    github_wh=str(re_loadyml('Github_Wh')),
                    github_dz=str(re_loadyml('GitHub_dz')),
                    name=ok_img_list[random.randint(0, len(ok_img_list))]['name']
                )
        return rsp
    else:   
        return abort(400, '处理出错了惹~')

@app.route('/json')
def imgjson():
    with open('./github.json', 'r',encoding='utf-8') as lb:
            img_list = lb.read()
    ok_img_list = json.loads(img_list)
    return jsonify({'img_list': ok_img_list, 'img_num': len(ok_img_list)})

@app.route('/clear',methods=['GET', 'POST'])
def guimg():
    try:
        if request.method == 'GET':
            gettoken=request.args.get('token', default=None) # 参数不存在时默认 None
            if gettoken is not None:
                # return re_loadyml('Cltoken')
                if gettoken == re_loadyml("Cltoken"):
                    try:
                        if os.path.isfile('./github.json'):
                            os.remove("./github.json")
                            main_json()
                            return jsonify({"state": 'OK',"error": "None"})
                        else:
                            main_json()
                    except:
                        return jsonify({'state': 'Error', 'error': '清除失败'})
                else:
                    return jsonify({'Error': 'OK', 'error': 'Token 不正确哦~'})
            else:
                return jsonify({'state': 'Error', 'error': '缺少 Token 无法清除缓存'})
        else:
            return abort(400, 'Does not support POST requests')
    except Exception as oo:
        return jsonify({'state': 'Error', 'error': '运行出错了惹...'})

if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
