from time import sleep

from behave import *
from models.counter import Counter
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on pending requests view')
def step_impl(context):
    context.driver.get('http://localhost:5173/pending-requests/1')
    context.driver.implicitly_wait(4)
    context.counter = Counter()
    pending_requests = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*="css-5olqn5"]')
    context.counter.count = len(pending_requests)


@when(u'I click on "Accept" button')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class*="accept-medium-button"]'))).click()


@when(u'I click on confirmation')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#medium-primary-button'))).click()


@then(u'I shouldn\'t see request on pending page anymore')
def step_impl(context):
    sleep(2)
    pending_requests = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*="css-5olqn5"]')
    assert len(pending_requests) + 1 == context.counter.count


@when(u'I click on "Decline" button')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class*="decline-medium-button"]'))).click()


@when(u'I click on "Okay" button to close popup')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#medium-primary-button'))).click()
