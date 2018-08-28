import os
from lettuce import before, after, world
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from features.pages.page import BasePage, SearchPage, LoginPage

@before.all
def open_google():
    # open_drivers()
    world.driver = webdriver.Firefox()
    prepare_page(world.driver)
    print "Openning webdriver."

@after.all
def close_google(self):
    if world.driver:
        print "This is the end."
        # world.driver.quit()

def open_drivers():
    world.driver = get_firefox()
    world.driver.set_page_load_timeout(10)
    world.driver.implicitly_wait(10)
    world.driver.maximize_window()

'''
def get_firefox():
    try:
        driver = webdriver.Firefox()
    except Exception:
        my_local_firefox_bin = os.environ.get('FIREFOX_BIN')
        firefox_binary = FirefoxBinary(my_local_firefox_bin)
        driver = webdriver.Firefox(firefox_binary = firefox_binary)
    return driver
'''

def prepare_page(driver):
    world.home_page = BasePage(driver)
    world.search_page = SearchPage(driver)
    world.login_page = LoginPage(driver)

'''
def close_drivers():
    if world.driver:
        world.driver.quit()
'''