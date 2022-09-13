from pytest import fixture
from selenium import webdriver
from Configuration.config import ConstantData
from time import sleep

'''why fixture, cause we have created driver in every test method, 
so to remove repetition we used fixture...
so to use this driver in other test cases we will call this fixture and it will return us a 
driver
'''


@fixture()
def setup():
    driver = webdriver.Chrome(executable_path=r'/Users/gauravchhimwal/Desktop/pythonProject/chromedriver')
    driver.get(ConstantData.BASEURL)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    print(" Closing Browser")
    driver.close()

