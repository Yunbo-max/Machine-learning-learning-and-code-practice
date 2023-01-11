import requests
import re
import os

if __name__ == "__main__":
    # if not os.path.exists('./wiki'):
    #     os.mkdir('./wiki')
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    url = 'https://en.wikipedia.org/wiki/Cambridge'

    page_text = requests.get(url=url,headers=header).text

    with open('./web', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    ex = '<img alt=.*?src="(.*?)" decoding=.*?'
    img_src_list = re.findall(ex,page_text,re.S)
    print(img_src_list)
    for src in img_src_list:

        src = 'https:'+src
        img_data = requests.get(url=src,headers=header).content
        img_name = src.split('/')[-1]
        imPath = './wiki/'+img_name

        with open(imPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name,'Successfully!!!')




# <img alt="King's College Chapel, seen from the Backs" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/KingsCollegeChapelWest.jpg/250px-KingsCollegeChapelWest.jpg" decoding="async" width="250" height="187" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/KingsCollegeChapelWest.jpg/375px-KingsCollegeChapelWest.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b4/KingsCollegeChapelWest.jpg/500px-KingsCollegeChapelWest.jpg 2x" data-file-width="1025" data-file-height="768">