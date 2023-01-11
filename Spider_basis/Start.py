# -*- coding:UTF-8 -*-

import requests

if __name__ == "__main__":
    url = 'https://www.sogou.com'

    response = requests.get(url=url)

    page_text = response.text
    print(page_text)

    with open('./baidu.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
