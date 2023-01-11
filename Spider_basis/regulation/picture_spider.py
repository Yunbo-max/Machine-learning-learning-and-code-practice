 # -*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Arms_of_the_Cambridge_City_Council.svg/1024px-Arms_of_the_Cambridge_City_Council.svg.png'
    img_data = requests.get(url=url).content

    with open('./photo.jpg','wb')as fp:
        fp.write(img_data)



<img class="BDE_Image" pic_type="1" width="377" height="367" src="http://tiebapic.baidu.com/forum/w%3D580/sign=34862974463b5bb5bed720f606d1d523/ccf357b5c9ea15ce2a61c8d6f3003af33887b2ae.jpg?tbpicau=2022-09-23-05_8aa5bfa6f4c9c0fadbc8b67ca543e84b" size="137420">