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

    div_with_nav = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/div/header/div/div')))

    login_button = div_with_nav.find_elements_by_xpath(".//*")[10]
    login_button.click()


@given("the field 'Email' is empty")
def the_field_email_is_empty(context):
    context.driver.implicitly_wait(2)
    email_field = context.driver.find_element(By.CSS_SELECTOR, 'input[name=username]')
    email_field.clear()


@given("the field 'Password' is empty")
def the_field_password_is_empty(context):
    context.driver.implicitly_wait(2)
    password_field = context.driver.find_element(By.CSS_SELECTOR, 'input[name=password]')
    password_field.clear()


@when("I click on 'SIGN IN'")
def i_click_on_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input[type=submit][name=login]').click()


@then("I should see prompt '{message}'")
def i_should_see_prompt(context, message):
    error_msg = context.driver.find_element(By.XPATH, '//*[@id="input-error"]')
    assert error_msg.text == message


@when("I type '{email}' in 'Email'")
def i_type_email_in_email(context, email):
    context.driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys(email)


@when("I type '{password}' in 'Password'")
def i_type_password_in_password(context, password):
    context.driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys(password)


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
