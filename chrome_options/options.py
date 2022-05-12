import os.path

from selenium import webdriver
BASH_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DOWN_PATH=os.path.join(BASH_PATH,"download")

def options():
    prefs = {'profile.default_content_settings.popups': 0,
             'download.default_directory': str(DOWN_PATH)
             }
    option = webdriver.ChromeOptions()
    option.add_experimental_option('prefs', prefs)
    option.add_argument('--headless')
    option.add_argument('–start-maximized')

    return option
