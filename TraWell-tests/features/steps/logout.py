from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am logged in TraWell')
def step_impl(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)
    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button-desktop')))
    login_button.click()
    context.driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys("olga@tokarczuk.com")
    context.driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys("correct_pass")
    context.driver.find_element(By.CSS_SELECTOR, 'input[type=submit][name=login]').click()


@when(u'I click on "Log out" button in user menu')
def step_impl(context):
    open_setting_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#icon-settings-desktop')))
    open_setting_icon.click()
    context.driver.find_element(By.CSS_SELECTOR, '#logout-desktop-button').click()


@then(u'I should see "LOGIN" button in navigation bar')
def step_impl(context):
    try:
        navbar = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div/header/div/div')))
        login_button = navbar.find_elements(By.XPATH, ".//*")[10]
    except NoSuchElementException:
        assert False
    assert login_button.text == "LOGIN"


@then(u'I should be on the login page')
def step_impl(context):
    assert context.driver.current_url == 'http://localhost:5173/'
