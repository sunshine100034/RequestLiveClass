#!__author__ = "yf"
"""
pycharm
"""
import LoginPage
import requests
import unittest
import ddt

@ddt.ddt
class PublicLiveClassPage(unittest.TestCase):
    def setUp(self):
        print('接口测试开始')
        pass

    def tearDown(self):
        print('接口测试结束')

    @ddt.file_data('PublishCourse_data.json')
    def testPublicLiveClass(self, **kwargs):
        print(kwargs)
        cookies = LoginPage.DoLogin('astest-fy', '4321')
        if cookies == False:
            return
        url = 'https://www.ablesky.com/liveCourse.do?action=saveOrUpdateLiveCourse&c_type=simple'
        headers = {
            'Referer': r'https://www.ablesky.com/liveCourseRedirect.do?action=toPostLiveCourse&organizationId=2249&id=337055&fromurl=https://www.ablesky.com/organizationAdminRedirect.do?action=toManageLiveCourse&organizationId=2249',
            'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }

        # data = {
        #     'liveCourseId': 337055,
        #     'transientuuid': '1c36b445-639b-4b6a-bfce-86ba46277e96',
        #     'title': r'一接口三aa+aa++一二三!@#$%^&*(<input value="input">',
        #     'lecturerId': 5778083,
        #     'organizationId': 2249,
        #     'classTimeJSONList': '{"list":[{"classTimeId":"193155","subHead":"标题长度没有限制么，应该是多少呢？yi一二三四五六七八九十！@#","date":"2021-05-25","startHour":"9","startMinute":"50","endHour":"23","endMinute":"59","classTimes":1,"discount":100}]}',
        #     'studentNumber': -5
        # }
        response = requests.post(url=url, headers=headers, cookies=cookies, data=kwargs)
        print(response.text)


if __name__ == "__main__":
    unittest.main()