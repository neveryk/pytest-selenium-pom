import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_action import BaseAction
from page.login_page import Login

# class Test_all():
#     def test_1(self):

driver=webdriver.Chrome()

driver.get('http://192.168.10.167:88/login')
driver.maximize_window()

lo=Login(driver)
lo.login("adm","123")
# a=lo.login_url_check()
b=lo.login_message_chech()
# print(a)
print(b)
