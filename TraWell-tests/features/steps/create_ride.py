import logging
from time import sleep

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given(u'I am logged in TraWell as private user')
def step_impl(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)
    try:
        login_button = WebDriverWait(context.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#login-button-desktop')))
        login_button.click()
        context.driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys("olga@tokarczuk.com")
        context.driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys("correct_pass")
        context.driver.find_element(By.CSS_SELECTOR, 'input[type=submit][name=login]').click()
    except Exception:
        logging.warn('User already logged in')


@when(u'I chosen "Post a ride" from navigation bar')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#post-a-ride-desktop').click()


@when(u'I click on "SINGULAR" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-singular-ride-button').click()


@when(u'I input "{content}" as City from')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#place-from-autocomplete')
    input_field.send_keys(content[:4])
    sleep(2)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith(content[:4]):
            e.click()
            break


@when(u'I input "{content}" as City to')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#place-to-autocomplete')
    input_field.send_keys(content[:4])
    sleep(2)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith(content[:4]):
            e.click()
            break


@when(u'I input "{content}" as Start date of the ride')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#desktop-date-picker-textfield')
    input_field.send_keys(content)


@when(u'I input "{content}" as Start date')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#start-date-selector')
    input_field.send_keys(content)


@when(u'I input "{content}" as Start time of the ride')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#time-picker')
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(content)


@when(u'I input "{content}" as Start time')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#start-time-selector')
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(content)


@when(u'I input "{content}" hours as duration of ride')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#hours')
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(content)


@when(u'I input "{content}" hours as duration')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#duration-hours-selector')
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(content)


@when(u'I input "{content}" as Price')
def step_impl(context, content):
    input_field = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/div/input')
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(content)


@when(u'I input "{content}" as amount of people')
def step_impl(context, content):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#amount-of-people-input')
    input_field.clear()
    input_field.send_keys(content)


@when(u'I input "{content}" as Price for the ride')
def step_impl(context, content):
    input_field = context.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[4]/div[2]/div/div/input')
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.send_keys(content)


@when(u'I choose first vehicle from list')
def step_impl(context):
    context.driver.execute_script("arguments[0].scrollIntoView();",
                                  context.driver.find_element(By.CSS_SELECTOR, '#exact-place-to'))
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#choose-vehicle-dropdown')
    sleep(4)
    input_field.click()
    menu = context.driver.find_element(By.CSS_SELECTOR, '#menu-')
    menu.find_elements(By.TAG_NAME, 'li')[0].click()


@when(u'I click on "ADD RIDE" button')
def step_impl(context):
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element(By.CSS_SELECTOR, "#add-singular-ride"))
    element = context.driver.find_element(By.CSS_SELECTOR, "#add-singular-ride")
    sleep(2)
    element.click()


@when(u'I click on recurrent "ADD RIDE" button')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "#add-ride-button")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(2)
    element.click()


@then(u'I should see "{title}" modal')
def step_impl(context, title):
    assert context.driver.find_element(By.XPATH, '//*[@id="modal"]/div[3]/h4').text == title


@when(u'I click on "OKAY" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#medium-primary-button").click()


@then(u'I should be on home page')
def step_impl(context):
    assert context.driver.current_url == "http://localhost:5173/"
    assert context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/h2').text == 'Find a ride'


@when(u'I input "{place}" as Exact place from')
def step_impl(context, place):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#exact-place-from')
    input_field.send_keys(place)


@when(u'I input "{place}" as Exact place to')
def step_impl(context, place):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#exact-place-to')
    input_field.send_keys(place)


@when(u'I input "{minutes}" minutes as additional duration of ride')
def step_impl(context, minutes):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#minutes')
    input_field.send_keys(minutes)


@when(u'I input "{minutes}" minutes as additional duration')
def step_impl(context, minutes):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#duration-minutes-selector')
    input_field.send_keys(minutes)


@when(u'I input "{date}" as End date of the ride')
def step_impl(context, date):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#end-date-selector')
    input_field.send_keys(date)


@when(u'I input "{number}" as Frequence')
def step_impl(context, number):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#frequence-input')
    input_field.clear()
    input_field.send_keys(number)


@when(u'I choose "{frequency}" as Frequency type')
def step_impl(context, frequency):
    input_field = context.driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')[1]
    context.driver.execute_script("arguments[0].scrollIntoView();", input_field)
    sleep(2)
    input_field.click()

    selectors = context.driver.find_elements(By.CSS_SELECTOR, '#frequence-type-selector')
    if frequency == 'Hourly':
        selectors[0].click()
    if frequency == 'Daily':
        selectors[1].click()
    if frequency == 'Weekly':
        selectors[2].click()
    if frequency == 'Monthly':
        selectors[3].click()


@given(u'I chosen "Post a ride" from navigation bar')
def step_impl(context):
    post_ride_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#post-a-ride-desktop')))
    post_ride_button.click()


@then(u'I should see error message "{message}"')
def step_impl(context, message):
    error_message = context.driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div > h4')
    assert error_message.text == message


@when(u'I click on "RECURRENT" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-recurrent-ride-button').click()
