from behave import *


@when(u'I click on \'Register\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on \'Register\'')


@then(u'I should see \'Register\' form')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see \'Register\' form')


@given(u'I am on register page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on register page')


@then(
    u'I should see \'Please specify this field.\' under: \'Email\', \'First Name\', \'Last Name\', \'Account Type\', '
    u'\'Date of birth\'')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I should see \'Please specify this field.\' under: \'Email\', \'First Name\', \'Last Name\', '
        u'\'Account Type\', \'Date of birth\'')


@when(u'I type \'anna\' in \'Email\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'anna\' in \'Email\'')


@then(u'I should see \'Invalid email address.\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see \'Invalid email address.\'')


@when(u'I type \'123\' in \'Password\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'123\' in \'Password\'')


@when(u'I type \'abc\' in \'Confirm Password\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'abc\' in \'Confirm Password\'')


@then(u'I should see \'Password confirmation doesn\'t match.\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see \'Password confirmation doesn\'t match.\'')


@when(u'I type \'dd.09.rrrr\' in \'Date of birth\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'dd.09.rrrr\' in \'Date of birth\'')


@then(u'I should stay on register page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should stay on register page')


@then(u'my mouse should be focused on \'Date of birth\' field')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then my mouse should be focused on \'Date of birth\' field')


@when(u'I type \'rand_string\' in \'Facebook\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'rand_string\' in \'Facebook\'')


@then(u'my mouse should be focused on \'Facebook\' field')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then my mouse should be focused on \'Facebook\' field')


@when(u'I type \'rand_string\' in \'Instagram\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'rand_string\' in \'Instagram\'')


@then(u'my mouse should be focused on \'Instagram\' field')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then my mouse should be focused on \'Instagram\' field')


@when(u'I type \'anna@mak.com\' in \'Email\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'anna@mak.com\' in \'Email\'')


@when(u'I type \'Anna\' in \'First Name\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'Anna\' in \'First Name\'')


@when(u'I type \'Mak\' in \'Last Name\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'Mak\' in \'Last Name\'')


@when(u'I type \'good_pass\' in \'Password\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'good_pass\' in \'Password\'')


@when(u'I type \'good_pass\' in \'Confirm Password\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'good_pass\' in \'Confirm Password\'')


@when(u'I input \'Private User\' in \'Account Type\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input \'Private User\' in \'Account Type\'')


@when(u'I input \'01.01.1999\' in \'Date of birth\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input \'01.01.1999\' in \'Date of birth\'')


@then(u'I should see prompt \'Email Verification\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see prompt \'Email Verification\'')


# @when(u'I type \'wrong_pass\' in \'Password\'')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I type \'wrong_pass\' in \'Password\'')
#

@given(u'I have users')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have users')


@when(u'I type \'correct_pass\' in \'Password\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type \'correct_pass\' in \'Password\'')


@then(u'I shouldn\'t see \'LOGIN\' button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I shouldn\'t see \'LOGIN\' button')
