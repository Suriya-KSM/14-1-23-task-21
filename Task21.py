# 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


class KSM:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)
            #getting cookies before login and displaying
            cookies_before = self.driver.get_cookies()
            print("Cookies before login : ", cookies_before)
            sleep(4)
            #logging in the website using credentials
            self.driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
            sleep(2)
            self.driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
            self.driver.find_element(by=By.ID, value= "login-button").click()
            sleep(4)
            #getting cookies after logging in and displaying
            cookies_after = self.driver.get_cookies()
            print("Cookies after login : ",cookies_after)

        except NoSuchElementException as selenium_error:
            print(selenium_error)
    def shutdown(self):
        sleep(3)
        self.driver.close()

URL = "https://www.saucedemo.com/"
Obj = KSM(URL)
Obj.login()
Obj.shutdown()