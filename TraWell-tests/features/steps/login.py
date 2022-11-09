from behave import *


@given("I am on the login page")
def step_impl():
    raise NotImplementedError(u'STEP: Given I am on the login page')


@given("the field 'Email' is empty")
def step_impl():
    raise NotImplementedError(u'STEP: And the field \'Email\' is empty')


@given("the field 'Password' is empty")
def step_impl():
    raise NotImplementedError(u'STEP: And the field \'Password\' is empty')


@when("I click on 'SIGN IN'")
def step_impl():
    raise NotImplementedError(u'STEP: When I click on \'SIGN IN\'')


@then("I should see prompt 'Invalid username or password.'")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should see prompt \'Invalid username or password.\'')


@when("I type 'olga@tokarczuk.com' in 'Email'")
def step_impl():
    raise NotImplementedError(u'STEP: When I type \'olga@tokarczuk.com\' in \'Email\'')


@given("I type 'wrong_pass' in 'Password'")
def step_impl():
    raise NotImplementedError(u'STEP: And I type \'wrong_pass\' in \'Password\'')


@given("I have users:")
def step_impl():
    raise NotImplementedError(u'STEP: Given I have users')


@given("I type 'correct_pass' in 'Password'")
def step_impl():
    raise NotImplementedError(u'STEP: And I type \'correct_pass\' in \'Password\'')


@then("I should be on the users home page")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should be on the users home page')


@given("I shouldn't see 'LOGIN' button")
def step_impl():
    raise NotImplementedError(u'STEP: And I shouldn\'t see \'LOGIN\' button')
