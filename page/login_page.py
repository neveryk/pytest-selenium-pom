from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class Login(BaseAction):

    username=(By.XPATH,'//*[@id="login"]/div[3]/div/form/div[1]/div/div/input')
    password=(By.XPATH,'//*[@id="login"]/div[3]/div/form/div[2]/div/div/input')
    click_login=(By.XPATH,'//*[@id="login"]/div[3]/div/form/div[3]/div/div')
    login_error="//span[text()='管理员']"
    login_url_success='home'

    def login(self,username,password):
        username_ele=self.get_element(*self.username)
        self.input_text(username_ele,username)
        password_ele=self.get_element(*self.password)
        self.input_text(password_ele,password)

        submit_ele=self.get_element(*self.click_login)
        self.click(submit_ele)

    def login_url_check(self):
        self.url_matches(self.login_url_success)

    def login_message_chech(self):
        self.get_text(self.login_error)
