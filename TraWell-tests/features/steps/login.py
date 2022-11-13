from behave import *


@given("I am on the login page")
def i_am_on_the_login_page(context):
    context.driver.get('http://localhost:5674/home')
    context.driver.find_element_by_css_selector('input.loginButton').click()


@given("the field 'Email' is empty")
def the_field_email_is_empty(context):
    email_field = context.driver.find_element_by_id('f_login')
    assert email_field.is_empty()


@given("the field 'Password' is empty")
def the_field_password_is_empty(context):
    raise NotImplementedError(u'STEP: And the field \'Password\' is empty')


@when("I click on 'SIGN IN'")
def i_click_on_sign_in(context):
    context.driver.find_element_by_css_selector('input.loginButton').click()


@then("I should see prompt 'Invalid username or password.'")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should see prompt \'Invalid username or password.\'')


@when("I type '{email}' in 'Email'")
def step_impl(context, email):
    context.driver.find_element_by_id('f_login').send_keys(email)


@given("I type '{password}' in 'Password'")
def step_impl(context, password):
    context.driver.find_element_by_id('f_password').send_keys(password)


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
