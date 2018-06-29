import re

import requests as req
# print(r.statu;s_code)
# for i in r.history:
#     print(i.url)
#     print(i.status_code)

def get_html(url):

    r = req.get(url)
    try:
        if r.status_code ==200:
            return r.text
    except:
        print("error")
    print(type(r))
    # print(r.text)
    return r.text



def get_url(html):
    # q = re.compile('a href=(.+?)">', re.S)
    q = re.compile(r'(?<=href=\").*?(?=\")', re.S)
    a = re.findall(q, html)
    print(len(a))

    return a


if __name__ == "__main__":
    res = get_html("https://www.douban.com/")
    res_url = get_url(res)
    print(res_url)
    dict1 = {}
    for i,j in enumerate(res_url):
        dict1[i] = j
    print(dict1)

