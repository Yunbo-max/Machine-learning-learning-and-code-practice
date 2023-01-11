# -*- coding:UTF-8 -*-

import requests
import json

if __name__ == "__main__":
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    # url = 'https://s.deepl.com/web/statistics'
    url = 'https://fanyi.baidu.com/sug'
    word = input('enter the retrieve word: ')
    data = {
        'kw':word
    }
    response = requests.post(url=url,data=data,headers=header)

    dic_obj = response.json()

    fileName = word+'.json'

    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('Successfully!!!')


