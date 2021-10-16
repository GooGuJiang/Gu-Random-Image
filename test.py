import os
import time
import json
import requests
import yaml
import urllib.parse

def now_time():
    # 获得当前天
    now = int(time.time())
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%d", timeArray)
    return otherStyleTime

def re_loadyml(name): #读取配置文件
    with open('./set.yml', 'r',encoding='utf-8') as f:
            bottok = yaml.load(f.read(),Loader=yaml.FullLoader)
            return bottok[name]

def fileTime(file):
    return time.strftime("%d",time.localtime(os.path.getmtime(file)))#获取创建天数

def main_json():
    try:
        if os.path.isfile('./github.json') == False: #检测文件是否存在
            jsonfile = open('./github.json','w')
            jsonfile.close()
            url="https://api.github.com/repos/"+str(re_loadyml('Github_User'))+"/"+str(re_loadyml('Github_Wh'))+"/contents/"+str(re_loadyml('GitHub_dz'))
            res = requests.get(url)
            uesr_text = json.loads(res.text)
            ok_json = eval(json.dumps(uesr_text))
            jsonload = ''
            fout = open('./github.json', 'a', encoding='utf8')
            fout.write("[")
            for i in range(0, len(ok_json)):
                img_name = urllib.parse.quote(ok_json[i]["name"])
                data = {
                'name' : img_name
                }
                if i != len(ok_json)-1:
                    fout.write(str(json.dumps(data))+",")
                else:
                    fout.write(str(json.dumps(data)))

            fout.write("]")
            fout.close()
        else:
            if fileTime('./github.json') != now_time(): #检测文件是否过期
                print("文件过期开始更新")
                os.remove("./github.json")
                json_newfile = open('./github.json','w')
                json_newfile.close()
                
                url="https://api.github.com/repos/"+str(re_loadyml('Github_User'))+"/"+str(re_loadyml('Github_Wh'))+"/contents/"+str(re_loadyml('GitHub_dz'))
                res = requests.get(url)
                uesr_text = json.loads(res.text)
                ok_json = eval(json.dumps(uesr_text))
                img_name = []
                jsonload = ''
                fout = open('./github.json', 'a', encoding='utf8')
                fout.write("[")
                for i in range(0, len(ok_json)):
                    img_name = urllib.parse.quote(ok_json[i]["name"])
                    data = {
                    'name' : img_name
                    }
                    if i != len(ok_json)-1:
                        fout.write(str(json.dumps(data))+",")
                    else:
                        fout.write(str(json.dumps(data)))
                
                fout.write("]")
                fout.close()

                print(jsonload)
                

            else:
                print("文件未过期")
        return True
    except:
        return False

import random 
main_json()

with open('./github.json', 'r',encoding='utf-8') as lb:
    img_list = lb.read()

ok_img_list = json.loads(img_list)
print(ok_img_list[random.randint(0,len(ok_img_list))]["name"])  