import time

from selenium.webdriver.common.by import By

from Base.base import Base
from Common import Resident_check_in
from Base.Mysqldb_test import Mysqldb_test

Common = Resident_check_in()
m = Mysqldb_test()


class Resident_check(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name=None, password=None):
        self.find_element(Common.user_name[0]).clear()
        self.find_element(Common.user_password[0]).clear()
        self.Operation(*Common.user_name, name)
        self.Operation(*Common.user_password, password)
        self.Operation(*Common.login)
        time.sleep(3)

    def int(self, parent_Community, Community, Floor, unit, FL, roomId):
        s1 = self.find_elements(Common.element1)
        for i in s1:
            if i.text == '人房信息':
                i.click()
        s2 = self.find_elements(Common.element2)
        for i in s2:
            if i.text == '居民信息管理':
                i.click()
        s3 = self.find_elements(Common.element3)
        for i in s3:
            if i.text == '居民入住登记':
                i.click()
        time.sleep(2)
        self.Operation(*Common.element4)
        s1 = self.find_elements(Common.element5)
        for i in s1:
            if parent_Community in i.text:
                i.click()
                break
        self.Operation(*Common.element6)
        s2 = self.find_elements(Common.element7)
        for i in s2:
            if Community in i.text:
                i.click()
                break
        self.Operation(*Common.element8)
        s3 = self.find_elements(Common.element9)
        for i in s3:
            if Floor in i.text:
                i.click()
                break
        self.Operation(*Common.element10)
        s4 = self.find_elements(Common.element11)
        for i in s4:
            if unit in i.text:
                i.click()
                break
        self.Operation(*Common.element12)
        s5 = self.find_elements(Common.element13)
        for i in s5:
            if FL in i.text:
                i.click()
                break
        time.sleep(2)
        s6 = self.find_elements(Common.element14)
        for i in s6:
            if roomId in i.text:
                i.click()
                break

    def submin(self):
        self.Operation(*Common.element15)

    def owner(self, name, idcard, number, num):
        time.sleep(3)
        self.find_element(Common.element16[0]).clear()
        self.Operation(*Common.element16, name)
        self.find_element(Common.element17[0]).clear()
        self.Operation(*Common.element17, idcard)
        self.find_element(Common.element18[0]).clear()
        self.Operation(*Common.element18, number)
        self.find_element(Common.element19[0]).clear()
        self.Operation(*Common.element19, num)

    def img(self, file1, file2, file3, x=None):
        time.sleep(2)
        self.Operation(*Common.element20, file1)
        time.sleep(2)
        self.Operation(*Common.element21, file2)
        for i in file3:
            time.sleep(1)
            self.find_element(Common.element22[0]).clear()
            time.sleep(2)
            self.Operation(*Common.element22, i)
        if x != None:
            for i in range(x):
                time.sleep(1)
                self.Operation(*Common.element23)
                self.Operation(*Common.element24)

    def cd_worker(self, number):
        try:
            self.Operation(*Common.element27)

        except:
            pass
        '''输入手机号进行校验'''
        time.sleep(1)
        self.Operation(*Common.element25, number)
        # time.sleep(1)
        self.Operation(*Common.element26)

    def up_worker(self, file_path):
        '''上传身份证头像'''
        # time.sleep(2)
        self.Operation(*Common.element28, file_path)

    def clickup(self):
        '''点击提交'''
        self.Operation(*Common.element29)

    def shengfz(self, file_path1=None, file_path2=None, type_cl='身份证'):
        time.sleep(1)
        try:
            els = self.find_elements(Common.element30)
            for i in els:
                i.click()
        except:
            pass

        '''选择证件类型自动上传图片'''
        els = self.find_elements(Common.element31)
        for i in els:
            if i.text == type_cl:
                i.click()
                break
        try:
            self.find_element(Common.element32[0]).clear()
        except:
            pass

        if file_path1 is not None:
            if type_cl == '身份证':
                self.Operation(*Common.element33, file_path1)
                self.Operation(*Common.element34, file_path2)
            else:
                self.Operation(*Common.element32, file_path1)
        return type_cl

    def selects_Political(self, type):
        self.Operation(*Common.element35)
        els = self.find_elements(Common.element36)
        for i in els:
            if i.text == type:
                i.click()
                break

    def job(self, text):
        self.Operation(*Common.element37, text)

    def setup_idcard(self, text, name):
        self.find_element(Common.element38[0]).clear()
        self.Operation(*Common.element38, text)
        self.find_element(Common.element39[0]).clear()
        self.Operation(*Common.element39, name)

    def select_Birthday(self, type_cl=None, year=None, mount=None, day=None):
        time.sleep(3)
        els = self.find_elements(Common.element31)
        for i in els:
            if i.text == type_cl:
                i.click()
                break
        time.sleep(3)
        self.Operation(*Common.element40)
        years = int(self.find_element(Common.element41).text[0:-2])
        # print(years)
        mounts = int(self.find_element(Common.element42).text[0:-2])
        if int(year) is not None:
            if int(year) < years:
                for i in range(years - int(year)):
                    self.Operation(*Common.element43)
            elif int(year) > years:
                for i in range(int(year) - years):
                    self.Operation(*Common.element44)
            else:
                pass
        if int(mount) is not None:
            if int(mount) < mounts:
                for i in range(mounts - int(mount)):
                    self.Operation(*Common.element45)
            elif int(mount) > mounts:
                for i in range(int(mount) - mounts):
                    self.Operation(*Common.element46)
            else:
                pass
        elp = self.find_elements(Common.element47)
        for i in elp:
            if i.text == day:
                # print(i.text)
                i.click()
                break
        return years

    def Relationship_type(self, type, text, file_path=None, bt='确定'):
        time.sleep(4)

        els = self.find_elements(Common.element48)
        for i in els:
            if i.text == type:
                i.click()
                break
        els2 = self.find_elements(Common.element49)
        for i in els2:
            if i.text == text:
                i.click()
                break
        if text == '租客':
            time.sleep(2)
            for c in file_path:
                if c :
                   self.Operation(*Common.element50, c)
                   self.find_element(Common.element50[0]).clear()
                else:
                    pass
        s = m.mysqldn_01(c='天坛社区', g='天坛小区', b='天坛东里', u='1单元', r='1402')
        time.sleep(10)
        self.clickup()
        if text == '租客' :
            if s[1] != 0 or s[0] == 0 and len(file_path) >= 2:
                t = self.find_elements(Common.element55[0])
                time.sleep(1)
                for i in t:
                    if i.text == bt:
                        i.click()
            else:
                pass

    def Issue_permissions(self, type, devse, num1=None, num2=None):
        s = self.find_elements(Common.element51)
        for i in type:
            for t in s:
                if i == t.text:
                    t.click()
                    if i in '身份证绑定':
                        self.Operation(*Common.element52, num1)
                    elif i in 'IC卡绑定':
                        self.Operation(*Common.element53, num2)
                    break
        p = self.find_elements(Common.element54)
        for c in devse:
            for e in p:
                if c in e.text:
                    # print(e.text)
                    time.sleep(5)
                    e.click()
                    break


if __name__ == '__main__':
    pass
    print(1 << 3)
