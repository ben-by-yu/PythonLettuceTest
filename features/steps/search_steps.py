from lettuce import world, step
from selenium.webdriver.common.by import By

google_url = "https://www.google.com"
outlook_url = "https://www.outlook.com"


@step('I am on google web page')
def step_impl(step):
    world.search_page.navigate(google_url)
    world.search_page.verify_page("Google")

@step('I input master chief')
def step_impl(step):
    world.search_page.input_search_text("Master Chief")

@step('I click submit')
def step_impl(step):
    world.search_page.click_submit()

@step('I should see the search result of master chief')
def step_impl(step):
    # world.search_page.verify_page("Master Chief - Google Search")
    world.search_page.verify_page("Master Chief - Google Search")
    # world.search_page.quit_driver()

@step('I input Halo')
def step_impl(step):
    world.search_page.input_search_text("halo")

@step('I should see the search result of Halo')
def step_impl(step):
    world.search_page.verify_page("halo - Google Search")
    # world.search_page.quit_driver()

@step('I am on outlook web page')
def step_impl(step):
    world.login_page.navigate(outlook_url)
    world.login_page.verify_page("Outlook.com - Microsoft free personal email")

@step('I input login and password')
def step_impl(step):
    # print step.hashes
    # for login_info in step.hashes
    login_info = step.hashes[0]
    world.login_page.input_login_passwd(login_info['login'], login_info['password'])
    # world.login_page.input_login_passwd(, mail_passwd)

@step('I should see inbox')
def step_impl(step):
    # world.login_page.verify_page("Outlook")
    print "==========================================="
    # print world.driver.title

