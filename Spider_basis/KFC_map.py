# -*- coding:UTF-8 -*-

import requests
import json

if __name__ == "__main__":
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    param = {

        'cname':'',
        'pid':'',
        'keyword': '深圳',
        'pageIndex': '1',
        'pageSize': '100'
    }
    response = requests.get(url=url, params=param, headers=header)

    page_text = response.text
    with open('./KFC.json', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('Successfully!!!')

