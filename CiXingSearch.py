import sys, getopt
import time
import urllib

import requests
import mysql.connector

header = {}
header[
    "authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjU0NjMsImVtYWwiOiJkZW1vQGdpdGh1Yi5jb20iLCJleHAiOjE2NjcwOTg3NzYsImlzcyI6Im1hZ25ldGFyOjE4ODAxNGM5In0.YAcB0aVc-OQWxrgMjbuUY8JWIsidBTR5mXXlJGAqEzw"
header["accept"] = "application/json"
header["accept-encoding"] = "gzip, deflate, br"
header["sec-ch-ua"] = '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"'
header[
    "user-agent"] = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"


def loadSensitiveWords() :
    return  ["1024", "性吧", "草榴"]

sensitiveWords =loadSensitiveWords()

def haveNoSensitiveWord(id):
    id = urllib.parse.quote(id)
    url = "https://test.api.cixing.io/v1/magnetic/fileList?id={}"
    f = url.format(id)
    print(f)
    r = requests.get(f, headers=header)
    print(r)
    if r.status_code != 200:
        return False
    json = r.json()
    print(json)
    for file in json["data"]:
        for word in sensitiveWords:
            if word in file["path"][0]:
                return False
    return True


def searchCiXing(keyWord):
    searchUrl = "https://test.api.cixing.io/v1/magnetic/search?model=precise&page=1&query={}"
    finalUrl = searchUrl.format(keyWord)
    print("构建的url为:", finalUrl)

    start = time.time()
    queryResult = requests.get(finalUrl, headers=header)
    end = time.time()
    print("耗时：{}s".format(end - start))
    print("code = ", queryResult.status_code)
    json = queryResult.json()
    print("响应为", json)

    l = json["data"]["list"]
    size = len(l)
    if size == 0:
        print("没有查询到磁力链接")
        return
    filtered = list(filter(lambda data: data["files"] <= 1, l))
    if (len(filtered) > 0):
        print("选取第一个只有一个文件的磁力", filtered[0])
        return (keyWord, filtered[0]["hash"])

    filtered = list(filter(lambda data: (data["files"] > 1 or haveNoSensitiveWord(data["id"])), l))
    filtered = list(filter(lambda data: (data["length"] > 1006190178), filtered))
    file = filtered[0]
    print(file)
    return (keyWord, file["hash"])


def alreadyHaveMagnet(banggao):
    coon = getMysqlConnect()



def loopGetMagnet(prefix, start, end):

    print("start = ",start)
    print("end = ",end)
    successGetId = []
    failedIds = []
    for a in range(int(start), int(end)):
        banggao = "{}-{:0>3d}".format(prefix, a)
        print("构建的番号为：", banggao)
        # if alreadyHaveMagnet(banggao):
        #     continue
        v = None
        try:
            v = searchCiXing(banggao)
        except Exception as e:

            failedIds.append(banggao)
            print(e)
        if v is not None:
            successGetId.append(v)
    coon = getMysqlConnect()
    cursor = coon.cursor()
    for a,h in successGetId:
        print("番号{}对应的磁力为：{}".format(a,h))
        cursor.execute("insert into id_hash_map (fanhao,hash)values(%s,%s)",[a,"magnet:?xt=urn:btih:" +h])
        print("row is ",cursor.rowcount)
    coon.commit()
def getMysqlConnect():
    return mysql.connector.connect(user='dbadmin', password='Pwd1234!', database='av_id_magnet')


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:s:e:", ["prefix=", "start=", "end=="])
    except getopt.GetoptError:
        print('''
        搜索注意按标准书写番号
        ''')
        sys.exit(2)

    prefix = 'snis'
    start = 1
    end = 999
    for opt, arg in opts:
        if opt == '-h':
            print('''
            ''')
            sys.exit(2)
        elif opt in ("-p", "--prefix"):
            prefix = arg
        elif opt in ("-s", "--start"):
            start = arg
        elif opt in ("-e", "--end"):
            end = arg

    print("prefix = {},start = {},end = {}".format(prefix, start, end))

    loopGetMagnet(prefix, start, end)
