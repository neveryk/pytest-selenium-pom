from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from testcase.conftest import data
from page.login_page import Login
from chrome_options.options import options

class Test_all():

    def setup_class (self):
        self.driver=webdriver.Chrome(options = options())
        self.lp=Login(self.driver)

    def teardown_class (self):
        self.driver.close()

    @pytest.mark.parametrize("username,userpwd,type",data["test_login"])
    def test_1(self,username,userpwd,type):
        self.driver.get('http://192.168.10.167:88/login')
        self.lp.login(username,userpwd)
        sleep(2)



