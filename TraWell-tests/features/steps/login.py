from time import sleep

from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I am on the login page")
def i_am_on_the_login_page(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)
    login_btn = context.driver.find_element(By.XPATH, '/html/body/div/div/div/header/div/div/nav[1]/div/button')
    # # login_btn = context.driver.find_element_by_css_selector('#root>div>div>header>div>div>nav.css-paq9ft>div>button')
    # login_btn.click()
    # sleep(4)
    # context.driver.wait(4)

    print("Element is visible? " + str(login_btn.is_displayed()))

    button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div/div/header/div/div/nav")))
    button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div/div/header/div/div/nav[1]/div/button")))
    button.click()
    # ActionChains(context.driver).click(login_btn).perform()


@given("the field 'Email' is empty")
def the_field_email_is_empty(context):
    context.driver.implicitly_wait(2)
    email_field = context.driver.find_element_by_id('username')
    assert email_field.is_empty()


@given("the field 'Password' is empty")
def the_field_password_is_empty(context):
    context.driver.implicitly_wait(2)
    password_field = context.driver.find_element_by_id('password')
    assert password_field.is_empty()


@when("I click on 'SIGN IN'")
def i_click_on_sign_in(context):
    context.driver.find_element_by_xpath('//*[@id="kc-login"]').click()


@then("I should see prompt 'Invalid username or password.'")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should see prompt \'Invalid username or password.\'')


@when("I type '{email}' in 'Email'")
def step_impl(context, email):
    context.driver.find_element_by_id('username').send_keys(email)


@given("I type '{password}' in 'Password'")
def step_impl(context, password):
    context.driver.find_element_by_id('password').send_keys(password)


@given("I have users:")
def step_impl(context):
    for row in context.table:
        context.model.add_user(row["name"], deparment=row["department"])
    raise NotImplementedError(u'STEP: Given I have users')


@then("I should be on the users home page")
def i_should_be_on_the_users_home_page(context):
    raise NotImplementedError(u'STEP: Then I should be on the users home page')


@given("I shouldn't see 'LOGIN' button")
def i_shouldnt_see_login_button(context):
    raise NotImplementedError(u'STEP: And I shouldn\'t see \'LOGIN\' button')
