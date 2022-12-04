import datetime
import logging
from time import sleep

from behave import *
from models.search import Search
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am logged in TraWell as private passenger')
def step_impl(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)
    try:
        login_button = WebDriverWait(context.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button-desktop')))
        login_button.click()
        context.driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys("anna@sowa.com")
        context.driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys("correct_pass")
        context.driver.find_element(By.CSS_SELECTOR, 'input[type=submit][name=login]').click()
    except Exception:
        logging.warn('User already logged in')


@given(u'I found rides from "{city_from}" to "{city_to}"')
def step_impl(context, city_from, city_to):
    input_field = context.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="From"]')
    input_field.send_keys(city_from[:4])
    sleep(2)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith(city_from[:4]):
            e.click()
            break

    input_field = context.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="To"]')
    input_field.send_keys(city_to[:4])
    sleep(2)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith(city_to[:4]):
            e.click()
            break

    context.driver.find_element(By.CSS_SELECTOR, '#find-button').click()


@when(u'I click on found ride')
def step_impl(context):
    context.driver.find_elements(By.CSS_SELECTOR, 'div[class*="css-l0b0zb"]')[0].click()


@when(u'I click on second found ride')
def step_impl(context):
    context.driver.find_elements(By.CSS_SELECTOR, 'div[class*="css-l0b0zb"]')[1].click()


@when(u'I click on "Book ride" button')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div > div > div > div.MuiBox-root.css-vyse20 > div.MuiBox-root.css-1xicefp > button'))).click()


@when(u'I click "Yes" to confirm booking')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#medium-primary-button').click()


@then(u'I should see "{title}" popup info')
def step_impl(context, title):
    sleep(1)
    modal = context.driver.find_element(By.CSS_SELECTOR, ' #modal>div.MuiBox-root.css-19o6g10')
    assert title in modal.text


@when(u'I set number of seats to "2"')
def step_impl(context):
    seats_selector = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="button"]')))
    seats_selector.click()
    sleep(2)

    seats = context.driver.find_elements(By.CSS_SELECTOR, f'li[role="option"]')
    seats[1].click()
