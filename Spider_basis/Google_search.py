# -*- coding:UTF-8 -*-

import requests

if __name__ == "__main__":
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    url = 'https://www.google.com/search?'
    kw = input('enter the retrieve word: ')
    param = {
        'query':kw
    }
    response = requests.get(url=url,params=param,headers=header)

    page_text = response.text
    fileName = kw+'.html'

    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName,'Successfully!!!')