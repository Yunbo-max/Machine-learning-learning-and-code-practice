# -*- coding:UTF-8 -*-

import requests
import json

if __name__ == "__main__":
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {

        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':'',
    }
    id_list = []

    json_ids = requests.post(url=url, data=data, headers=header).json()

    for item in json_ids['list']:
        id_list.append(item['ID'])

    print(id_list)
    # fileName = word + '.json'
    #
    # fp = open(fileName, 'w', encoding='utf-8')
    # json.dump(dic_obj, fp=fp, ensure_ascii=False)
    #
    # print('Successfully!!!')