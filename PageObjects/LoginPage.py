"""Page Object Class for Login Page """


class LoginPage:
    username_text_box_id = "Email"
    password_text_box_id = "Password"
    login_button_xpath = r"//button[text()='Log in']"
    logout_button_xpath = r"//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_id(self.username_text_box_id).clear()
        self.driver.find_element_by_id(self.username_text_box_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_text_box_id).clear()
        self.driver.find_element_by_id(self.password_text_box_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()



