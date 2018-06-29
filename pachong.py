import re
import random
import requests


def get_picture():
    url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=美女"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    res = requests.get(url, headers=headers)
    a = re.compile(r'img src="(.*?)"', re.M)
    result = re.findall(a, res.text)

    print(res.text)
    print(result)
    # print(type(res.content))
    # data - objurl = "http://imgsrc.baidu.com/imgad/pic/item/10dfa9ec8a136327701bf8109b8fa0ec08fac71a.jpg"
    return result


def find():
    str_search = input("请输入查找的类型：")
    word = str_search
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + word
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    res = requests.get(url, headers=headers)
    a = re.findall('"objURL":"(.*?)"', res.text, re.S)
    print(a)
    for i, j in enumerate(a):
        with open("/home/zhang/图片/" + str(i) + '.jpg', 'wb') as f:
            if j.startswith("http"):
                res = requests.get(j)
                f.write(res.content)
                print("正在下载。。。" + str(i) + "/" + str(len(a) - 1))


# def set(r):
#
#     for i, j in enumerate(r):
#
#         with open("/home/zhang/图片/" + str(i) + '.jpg', 'wb') as f:
#             if j.startswith("http"):
#                 res = requests.get(j)
#                 f.write(res.content)
#
#     return 0
def pachong():
    url = ""
    res = requests.get(url, stream=True)
    # 用流的方式来写入图片
    with open("1.jpg", "wb") as f:
        for i in res.iter_content(chunk_size=1024):
            f.write(i)


if __name__ == "__main__":
    # a = get_picture()
    # set(a)
    find()
