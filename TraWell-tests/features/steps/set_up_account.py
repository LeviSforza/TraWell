from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('I click on "Register"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#kc-registration > span > a').click()


@then('I should see {title} form')
def step_impl(context, title):
    form_title = context.driver.find_element(By.CSS_SELECTOR, '#kc-page-title')
    assert form_title.text == title


@given('I am on register page')
def step_impl(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)

    navbar = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/div/header/div/div')))
    login_button = navbar.find_elements(By.XPATH, ".//*")[10]
    login_button.click()
    context.driver.find_element(By.CSS_SELECTOR, '#kc-registration > span > a').click()


@when('I click on "Register" button')
def step_impl(context):
    register_button = context.driver.find_element(By.CSS_SELECTOR, "input[value=Register]")
    register_button.click()


@then(u'I should see "{message}" under "Email"')
def step_impl(context, message):
    email = context.driver.find_element(By.CSS_SELECTOR, "#input-error-email")
    assert email.text == message


@then(u'I should see "{message}" under "Password"')
def step_impl(context, message):
    password = context.driver.find_element(By.CSS_SELECTOR, "#input-error-password")
    assert password.text == message


@then(u'I should see "{message}" under "First Name", "Last Name", "Account Type", "Date of birth"')
def step_impl(context, message):
    firstName = context.driver.find_element(By.CSS_SELECTOR, "#input-error-firstName")
    assert firstName.text == message
    lastName = context.driver.find_element(By.CSS_SELECTOR, "#input-error-lastName")
    assert lastName.text == message
    date_of_birth = context.driver.find_element(By.CSS_SELECTOR, "#input-error-date_of_birth")
    assert date_of_birth.text == message
    user_type = context.driver.find_element(By.CSS_SELECTOR, "#input-error-user_type")
    assert user_type.text == message


@then(u'I should see "{message}" under "Confirm password"')
def step_impl(context, message):
    email = context.driver.find_element(By.CSS_SELECTOR, "#input-error-password-confirm")
    assert email.text == message


@when('I type "{data}" in {field_name} field')
def step_impl(context, data, field_name):
    formatted_field_name = field_name.lower().replace(' ', '_')
    input_field = context.driver.find_element(By.CSS_SELECTOR, "#{}".format(formatted_field_name))
    input_field.send_keys(data)


@then(u'I should stay on register page')
def step_impl(context):
    assert context.driver.current_url.startswith("http://localhost:8403/auth/realms/TraWell/login-actions/registration")


@then(u'my mouse should be focused on {field_name} field')
def step_impl(context, field_name):
    formatted_field_name = field_name.lower().replace(' ', '_')
    input_field = context.driver.find_element(By.CSS_SELECTOR, "#{}".format(formatted_field_name))

    assert input_field == context.driver.switch_to.active_element


@when(u'I input "{firstName}" in First Name field')
def step_impl(context, firstName):
    input_field = context.driver.find_element(By.CSS_SELECTOR, "#firstName")
    input_field.send_keys(firstName)


@when(u'I input "{lastName}" in Last Name field')
def step_impl(context, lastName):
    input_field = context.driver.find_element(By.CSS_SELECTOR, "#lastName")
    input_field.send_keys(lastName)

