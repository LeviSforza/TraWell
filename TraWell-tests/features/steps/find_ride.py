from behave import *
from models.search import Search
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'I am on TraWell homepage')
def step_impl(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)
    context.search = Search()


@when(u'I click on "FIND" button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#find-button').click()


@when(u'I input "{content}" as starting place')
def step_impl(context, content):
    input_field = context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/input')
    input_field.send_keys(content[:4])
    context.driver.implicitly_wait(4)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith(content[:4]):
            e.click()
            context.search.city_form = content
            break


@when(u'I input "{content}" as destination')
def step_impl(context, content):
    input_field = context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[1]/div[1]/div[2]/div/div/input')
    input_field.send_keys(content[:4])
    context.driver.implicitly_wait(4)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith(content[:4]):
            e.click()
            context.search.city_to = content
            break


@when(u'I input "{date}" as date of the ride')
def step_impl(context, date):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#desktop-date-picker-textfield')
    ActionChains(context.driver).click(input_field).key_down(Keys.CONTROL).send_keys(
        "a").key_up(Keys.CONTROL).send_keys(date).perform()
    context.search.date = date


@when(u'I input "{time}" as time of the ride')
def step_impl(context, time):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#time-picker')
    ActionChains(context.driver).click(input_field).key_down(Keys.CONTROL).send_keys(
        "a").key_up(Keys.CONTROL).send_keys(time).perform()
    context.search.time = time


@when(u'I input "{number}" as amount of passengers')
def step_impl(context, number):
    input_field = context.driver.find_element(By.CSS_SELECTOR, '#amount-of-people-input')
    input_field.clear()
    ActionChains(context.driver).click(input_field).key_down(Keys.BACKSPACE).key_up(
        Keys.BACKSPACE).send_keys(number).perform()


@then(u'I should see summary of search parameters')
def step_impl(context):
    city_from = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[1]/div[1]/h4').text
    city_to = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[1]/div[2]/h4').text

    assert city_from == context.search.city_form
    assert city_to == context.search.city_to

    if context.search.date is not None:
        date = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/h5').text
        assert date == context.search.date
    if context.search.time is not None:
        time = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/h5[2]').text
        assert time == context.search.time


@then(u'rides consistent with search')
def step_impl(context):
    container = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]')
    try:
        rides = container.find_elements_by_css_selector("div[class*=css-l0b0zb")
        for ride in rides:
            assert context.search.city_form in ride.text
            assert context.search.city_to in ride.text
    except Exception:
        assert False


@then(u'I should see "{message}" message')
def step_impl(context, message):
    message_h = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]/div/div/h5')
    assert message == message_h.text


@then(u'I should see error "{error}"')
def step_impl(context, error):
    assert error in context.driver.page_source

