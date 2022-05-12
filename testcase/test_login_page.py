from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from testcase.conftest import data
from page.login_page import Login
from page.login import Login
from page.search import search

class Test_all():

    def setup_class (self):
        self.driver=webdriver.Chrome()
        self.lp=Login(self.driver)
        self.se=search(self.driver)

    def teardown_class (self):
        self.driver.close()

    @pytest.mark.parametrize("username,userpwd",data["test_login"])
    def test_1(self,username,userpwd):
        self.driver.get('http://192.168.10.167:88/login')
        self.lp.login(username,userpwd)
        sleep(2)



