# encoding: utf-8
import requests

def netcheck(url):
    try:
        r = requests.get(url, timeout = 1)
        status_code = r.status_code
        return status_code
    except Exception as e:
        return e

if __name__ == "__main__":
    with open("url.txt") as f:     #url.txt存放url地址,一个url占一行
        try:
            for line in f:
                status = netcheck(line.strip()) # strip() to remove blankspace or line break
                if status == 200:
                    print(line.strip() + ': successful')
                    with open('webjieguo.txt', 'a') as f1:      #需要在当前文件夹下创建url.txt和jieguo.txt，jieguo保存脚本执行后返回状态码200的url
                        f1.write(line)
                else:
                    print(line+': unsuccessful')
        except Exception as e:
            print ("e")