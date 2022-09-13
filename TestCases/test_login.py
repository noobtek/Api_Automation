import pytest
from selenium import webdriver
from Configuration.config import ConstantData
from PageObjects.LoginPage import LoginPage


class Test_001_Login:

    def test_homepage_title(self, setup):   # setup will return a driver and we stored it in a variable
        self.driver = setup
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True

        else:
            self.driver.save_screenshot(".//ScreenShots//" + "test_homepage_title.png")

            assert False

    def test_login(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        ''' as soon as LoginPage object is created, constructor will be automatically invoked
            and it is expecting driver as an argument, so we will pass driver here
            '''
        self.lp.set_username(ConstantData.USERNAME)
        self.lp.set_password(ConstantData.PASSWORD)
        self.lp.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True

        else:
            self.driver.save_screenshot(".//ScreenShots//" + "test_login.png")

            assert False



