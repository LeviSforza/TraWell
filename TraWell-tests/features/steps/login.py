import os
from pathlib import Path

from behave import *
from dotenv import load_dotenv
from keycloak import KeycloakAdmin
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dotenv_path = Path("TraWell-tests/features/.env")
load_dotenv(dotenv_path=dotenv_path)


@given("I am on the login page")
def i_am_on_the_login_page(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)

    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button-desktop')))
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
    error_msg = context.driver.find_element(By.CSS_SELECTOR, '#input-error')
    assert error_msg.text == message


@when("I type '{email}' in 'Email'")
def i_type_email_in_email(context, email):
    context.driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys(email)


@when("I type '{password}' in 'Password'")
def i_type_password_in_password(context, password):
    context.driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys(password)


@given("I have users")
def i_have_users(context):
    keycloak_admin = KeycloakAdmin(server_url='http://localhost:8403/auth/',
                                   username=os.getenv("ADMIN_USERNAME"),
                                   password=os.getenv("ADMIN_PASSWORD"),
                                   realm_name=os.getenv("REALM"),
                                   verify=True)

    for row in context.table:
        # Get user ID from username
        user_id_keycloak = keycloak_admin.get_user_id(row["email"])

        if user_id_keycloak is None:
            assert False

        # Get User
        user = keycloak_admin.get_user(user_id_keycloak)

        assert user['firstName'] == row["firstName"]
        assert user['lastName'] == row["lastName"]
        assert user['email'] == row["email"]


@then("I should be on the users home page")
def i_should_be_on_the_users_home_page(context):
    assert context.driver.current_url == 'http://localhost:5173/'


@then("I shouldn't see 'LOGIN' button in navigation bar")
def i_shouldnt_see_login_button(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#icon-settings-desktop')))
    except NoSuchElementException:
        assert False
    assert True
