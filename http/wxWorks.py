#!/usr/local/bin/python3

import urllib.request
import json

global apiURL

apiURL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4f404e94-be02-4da6-aa30-75c18926a60f"

def sendMessage(text = "", debug = False):

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Chrome"
    }
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": text
        }
    }
    print("地址 : {}".format(apiURL))
    print("内容 : {}".format(json.dumps(data)))

    if(debug == True):
        
        print("请求 : 开始 ...")
        req = urllib.request.Request(apiURL, data=bytes(json.dumps(data), 'utf8'), headers=headers)
        res = urllib.request.urlopen(req)
        
        if res.status == 200:
            resp = res.read()
            print (resp.decode('utf-8'))
        else:
            print (res.status, res.reason)
    else:
        print("请求 : 取消 ...")