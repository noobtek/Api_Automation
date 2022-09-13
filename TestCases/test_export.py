import time

from PageObjects.LoginPage import LoginPage
from PageObjects.SalesOrder import SalesOrder

class Test_003_export():

    def test_export_excel(self, setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        lp.click_login()
        self.salesorder = SalesOrder(self.driver)
        self.salesorder.click_sales()
        self.salesorder.click_orders()
        self.salesorder.select_checkbox()
        self.salesorder.click_export()
        self.salesorder.select_export_excel()
