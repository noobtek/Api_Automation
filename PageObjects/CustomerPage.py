"""Page Object Class for Customer Page """
import time


class CustomerPage:
    email_text_field_id = "Email"
    password_text_field_id = "Password"
    company_text_field_id = "Company"
    first_name_text_field_id = "FirstName"
    last_name_text_field_id = "LastName"
    gender_radio_button_id = "Gender_Male"
    tax_exempt_checkbox_id = "IsTaxExempt"
    customer_select_box_xpath = "//select[@id='SelectedCustomerRoleIds']/option"
    admin_comment_text_filed_xpath= "//textarea[@class='form-control']"
    customer_button_link_text = "Customers"
    save_button_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def click_customer(self):
    #     self.driver.find_element_by_xpath("//button[@class='button-1 login-button']").click()
        self.driver.find_element_by_xpath("//i[@class = 'nav-icon far fa-user']").click()

        self.driver.find_element_by_xpath("//i[@class = 'nav-icon far fa-user']/../..//p[contains(text(),' Customers')]").click()



    def click_addnew(self):
        self.driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()

    def click_customer_info(self):
        self.driver.find_element_by_xpath("//div[@class='card-title']").click()

    def set_email(self, email):
        self.driver.find_element_by_id(self.email_text_field_id).clear()

        self.driver.find_element_by_id(self.email_text_field_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_text_field_id).clear()

        self.driver.find_element_by_id(self.password_text_field_id).send_keys(password)

    def set_first_name(self, firstname):
        self.driver.find_element_by_id(self.first_name_text_field_id).send_keys(firstname)


    def set_last_name(self, lastname):
        self.driver.find_element_by_id(self.last_name_text_field_id).send_keys(lastname)


    def select_radio_button(self):
        self.driver.find_element_by_id(self.gender_radio_button_id).click()


    def is_tax_exempt(self):
        self.driver.find_element_by_id(self.tax_exempt_checkbox_id).click()


    def admin_comment(self, message):
        self.driver.find_element_by_xpath(self.admin_comment_text_filed_xpath).send_keys(message)


    def click_save(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()



