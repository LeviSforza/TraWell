from time import sleep

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on profile page of the user I want to rate')
def step_impl(context):
    context.driver.get('http://localhost:5173/profile/3/1')
    context.driver.implicitly_wait(4)


@when(u'I click on "Add review" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-review').click()
    sleep(2)


@when(u'I click on "Add" button')
def step_impl(context):
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element(By.CSS_SELECTOR, '#add-comment-button'))
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, '#add-comment-button').click()


@when(u'I set rating as {number} stars')
def step_impl(context, number):
    child = (2 * int(number)) - 1
    context.driver.find_element(By.CSS_SELECTOR, f'#rating-stars-picker > label:nth-child({child})').click()


@then(u'I should see "{message}" popup')
def step_impl(context, message):
    modal_title = context.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/h4').text
    assert modal_title == message


@when(u'I choose ride from list')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#dropdown-select-ride'))).click()
    sleep(2)

    rides = context.driver.find_elements(By.CSS_SELECTOR, f'li[role="option"]')
    rides[1].click()


@when(u'I add description')
def step_impl(context):
    tick_btn = context.driver.find_element(By.CSS_SELECTOR, "#description-switch-button")
    sleep(2)
    tick_btn.click()

    input_field = context.driver.find_element(By.CSS_SELECTOR, "#description")
    input_field.send_keys('Super person to travel with')
