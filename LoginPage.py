#!__author__ = "yf"
"""
pycharm
"""
import requests
import json
import time

def isJsonString(_json):
    try:
        json_object = json.loads(_json)
        pass
    except ValueError as  e:
        return False;
    return True


def DoLogin(username, pswd):
    print(username, pswd)
    # 生成时间戳,time.time() is seconds
    timeStamp = str(int(time.time() * 1000))
    print(timeStamp)

    # 不知道前端加密方式，暂时先用抓取的url
    url = "https://passport.ablesky.com/login.do?ajax=true&jsonp=ablesky_1622165576257&isPopUp=false&j_username=hOCXjzep21lYuFupxUbuSg%253D%253D&j_password=d93591bdf7860e1e4ee2fca799911215&_acegi_save_account=on&_acegi_security_remember_me=on&_="
    url = url + timeStamp
    print(url)
    headers = {
        'Referer': 'https://www.ablesky.com/',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    print(url)
    response = requests.get(url= url, headers= headers)

    if response.status_code != 200:
        print(response.text)
        return False
    # text expample : ablesky_1622165576257({"ASUSS":"NTNFMERBRDAyODgxQkUwODg4ODM0OUQ2ODYyNUU1QTcucGFzc3BvcnQwbWQuYnAxLmFibGVza3kuY29tOjE5Mi4xNjguMjAyLjI0OjExMjExOjU3NzgwODM6YXN0ZXN0LWZ5OjE2MjIxNjkyOTUyMTc6WkdWaU16RTFZVEl6TURBNE9XSXdOamhsTXpZNU1USXlOekJqT0Rnd1kyRT0%3D","Authorization":"Bearer eyJhbGciOiJKV1QiLCJ0eXAiOiJIUzI1NiJ9.eyJleHAiOjE2MjIxNzY0OTUyMzcsImtleSI6IjU3NzgwODMifQ==.79169f7edc77692e0e04fd8ce087be507200dc4eaf2afc034528a942b97080ab","isBinded":true,"sS":"0","iI":false,"iP":false,"success":true});
    # 解析获取json串
    index_left = response.text.find('{')
    index_right = response.text.rfind('}')
    # 截取字符串str【left：right】，left下标开始（包括），right截止（不包括right下标的字符）
    text_json = response.text[index_left : index_right + 1]
    is_json = isJsonString(text_json)
    if is_json == False:
        return False

    return response.cookies
    pass

if __name__ == "__main__":
    DoLogin('astest-fy', '4321')