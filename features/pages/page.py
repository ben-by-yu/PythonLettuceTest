from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nose.tools import assert_equal, assert_true

class BasePage(object):
    def __init__(self, browser):
        self.driver = browser

    def navigate(self, url):
        self.driver.get(url)

    def verify_page(self, page_title):
        print "==========================================="
        print self.driver.title
        return assert_equal(self.driver.title, page_title)

    def quit_driver(self):
        self.driver.close()

class SearchPage(BasePage):
    def input_search_text(self, search_text):
        self.driver.find_element(By.XPATH, '//*[@id="lst-ib"]').send_keys(search_text)

    def click_submit(self):
        self.driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]').click()

class LoginPage(BasePage):
    def input_login_passwd(self, mailAddress, passwd):
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/nav/div/div/div/a').click()

        mail_address_box = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]')))
        mail_address_box.clear()
        mail_address_box.send_keys(mailAddress)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()

        passwd_box = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]')))
        passwd_box.clear()
        passwd_box.send_keys(passwd)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()