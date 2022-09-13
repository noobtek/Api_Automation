import time

from Configuration.config import ConstantData
from PageObjects.LoginPage import LoginPage
from PageObjects.CustomerPage import CustomerPage
from TestData.CustomerData import CustomerData


class Test_002_Customer():

    def test_addcustomer(self, setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        lp.click_login()
        self.cp = CustomerPage(self.driver)
        time.sleep(2)
        self.cp.click_customer()
        time.sleep(2)
        self.cp.click_addnew()
        time.sleep(2)
        self.cp.click_customer_info()
        time.sleep(2)
        self.cp.set_email(CustomerData.EMAIL)
        time.sleep(2)
        self.cp.set_password(CustomerData.PASSWORD)
        time.sleep(2)
        self.cp.set_first_name(CustomerData.FIRST_NAME)
        time.sleep(2)
        self.cp.set_last_name(CustomerData.LAST_NAME)
        time.sleep(2)
        self.cp.select_radio_button()
        time.sleep(2)
        self.cp.is_tax_exempt()
        time.sleep(2)
        self.cp.admin_comment(CustomerData.ADMIN_COMMENT)
        time.sleep(2)
        self.cp.click_save()
        time.sleep(2)











