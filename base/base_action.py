import os
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from common.logger import logger
from selenium.webdriver.support import expected_conditions as EC
import allure
BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
IMG_PATH=os.path.join(BASE_PATH,"img")
if not os.path.exists(IMG_PATH):
    os.mkdir(IMG_PATH)
class BaseAction:

    def __init__(self,driver):
        self.driver=driver

    def save_screenshot(self):
        img_name=os.path.join(IMG_PATH,"{}.png".format("截图"+time.strftime("%Y%m%d%H%M%S")))
        try:
            self.driver.save_screenshot(img_name)
            allure.attach.file(img_name,"用例成功截图",allure.attachment_type.PNG)
            logger.info('截图成功,文件名:{}'.format(img_name))
        except:
            allure.attach (img_name, "用例失败截图", allure.attachment_type.PNG)
            logger.error('截图失败,文件名:{}'.format(img_name))

    def get_element(self,by,value,doc=""):
        """
        定位元素
        :param by:  定位方式
        :param value: 定位的表达式
        :param doc: 提示的模块信息
        :return:  返回定位的元素, 如果没有找到, 则抛出异常
        """
        try:
            ele= self.driver.find_element(by,value)
            logger.info("模块:{},获取元素成功, 定位类型{},定位表达式:{}".format(doc,by,value))
            return ele
        except:
            logger.error("模块:{},获取元素失败, 定位类型{},定位表达式:{}".format(doc,by,value))
            self.save_screenshot()

    def get_elements (self, by, value, doc = ""):
        """
        获取所有的元素 如果没有则返回一个空列表
        :param by: 定位方式
        :param value: 定位表达式
        :param doc:  说明文档
        :return: 返回一个定位的列表集合,如果没有定位元素, 返回一个空列表
        """
        try:
            ele = self.driver.find_elements (by, value)
            logger.info ("模块:{},获取元素成功, 定位类型{},定位表达式:{}".format (doc, by, value))
            return ele
        except:
            logger.error ("模块:{},获取元素失败, 定位类型{},定位表达式:{}".format (doc, by, value))
            self.save_screenshot ()

    def wait_ele_presence(self,locator, timeout=10, doc=""):
        """判断元素是否存在"""
        try:
            ele= WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            logger.info(f"{doc}等待元素成功,定位方式{locator}")
            return ele
        except:
            logger.error(f"{doc}等待元素失败,定位方式{locator}")
            self.save_screenshot()

    def wait_ele_all_presence(self, locator, timeout=10, doc=""):
        """
        等待获取元素
        :param locator: 元组, 包括元素定位方式, 元素定位的表达式
        :param timeout: 等待超时时间 默认为10s
        :param doc: 说明文档
        :return:返回定位的元素列表, 如果没有, 返回一个空列表
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            logger.info(f"{doc}等待元素成功,定位方式{locator}")
            return ele
        except:
            logger.error(f"{doc}等待元素失败,定位方式{locator}")
            self.save_screenshot()

    def wait_ele_visible(self, locator, timeout=10, doc=""):
        """
        等待元素可见
        :param locator: 元组  (定位方式, 定位表达式)
        :param timeout: 超时时间 默认为10s
        :param doc: 说明文档
        :return: 返回找到的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logger.info(f"{doc}:元素定位成功,定位方式:{locator}")
            return ele
        except:
            self.save_screenshot()
            logger.error("{}-元素不存在:{}".format(doc, locator))

    def clear(self,ele):
        try:
            ele.clear()
            logger.info("清除元素成功!")
        except:
            self.save_screenshot()
            logger.error("清除元素失败！")

    def execute_js(self,js):
        try:
            self.driver.execute_script (js)
            logger.info (f"执行js脚本成功:{js}")
        except:
            logger.error (f"执行js脚本失败:{js}")
            self.save_screenshot ()

    def sleep(self,seconds=1):
        time.sleep(seconds)
        logger.info('强制等待{}秒'.format(seconds))

    def input_text(self,ele,text):
        try:
            self.clear(ele)
            ele.send_keys(text)
            logger.info("清除数据成功，输入文本{}".format(text))
        except:
            self.save_screenshot()
            logger.error("输入内容失败，输入文本{}".format(text))

    def get_text(self,ele):
        try:
            data=ele.text()
            return data
        except:
            logger.error("获取元素内容失败")
            self.save_screenshot()

    def get_attribute(self,ele,name):
        try:
            value=ele.get_attribute(name)
            logger.info ("获取属性成功")
            return value
        except:
            logger.error ("获取属性失败")
            self.save_screenshot()

    def click(self,ele):
        try:
            ele.click()
            logger.info("以点击元素")
        except:
            logger.error('点击元素失败')
            self.save_screenshot()

    def quit(self):
        self.driver.quit()
        logger.info('退出浏览器成功')

    def url_matches(self, url, timeout=10, doc="url路径匹配"):
        """
        等待页面的请求的路径匹配
        :param url: 期望的url路径
        :param timeout: 超时时间 默认10s
        :param doc: 说明文档
        :return: 没有返回
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            logger.info(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
        except:
            logger.error(f"{doc}:页面路径:{self.driver.current_url}, 匹配路径:{url}")
            self.save_screenshot()
            raise

    def implicitly_wait(self):
        self.driver.implicitly_wait (10)
        logger.info('显示等待10秒')