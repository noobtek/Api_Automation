import time


class SalesOrder:
    sales_select_box_xpath = "//i[@class = 'nav-icon fas fa-shopping-cart']"
    select_orders = "//i[@class = 'nav-icon fas fa-shopping-cart']/../..//p[contains(text(), ' Orders')]"
    list_of_check_box = "//input[@type = 'checkbox']"
    export_select_box = "//button[@class = 'btn btn-success dropdown-toggle dropdown-icon']"
    export_excel = "//button[@name = 'exportexcel-all']"

    def __init__(self, driver):
        self.driver = driver

    def click_sales(self):
        self.driver.find_element_by_xpath(self.sales_select_box_xpath).click()
        time.sleep(2)

    def click_orders(self):
        self.driver.find_element_by_xpath(self.select_orders).click()
        time.sleep(2)

    def select_checkbox(self):
        self.driver.find_element_by_xpath(self.list_of_check_box).click()
        time.sleep(2)

    def click_export(self):
        self.driver.find_element_by_xpath(self.export_select_box).click()
        time.sleep(2)

    def select_export_excel(self):
        self.driver.find_element_by_xpath(self.export_excel).click()
        time.sleep(2)











