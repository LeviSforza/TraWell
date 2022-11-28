import datetime
from time import sleep

from behave import *
from models.search import Search
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'I found interesting me rides')
def step_impl(context):
    context.driver.get('http://localhost:5173/')
    context.driver.implicitly_wait(4)
    context.search = Search()

    # city from
    input_field = context.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/input')
    input_field.send_keys("Kato")
    sleep(2)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith("Kato"):
            e.click()
            break

    # city to
    input_field = context.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div/div/div[1]/div[1]/div[2]/div/div/input')
    input_field.send_keys("Wroc")
    sleep(2)
    elems = context.driver.find_elements(By.CSS_SELECTOR, "li")
    for e in elems:
        if e.text.startswith("Wroc"):
            e.click()
            break

    context.driver.find_element(By.CSS_SELECTOR, '#find-button').click()


@when(u'I input "{data}" into Start {field_type} field')
def step_impl(context, data, field_type):
    if field_type == 'Date':
        input_field = context.driver.find_element(By.XPATH, '//*[@id="desktop-wrapper"]/div[2]/div/input')
        context.search.date = data
    else:
        input_field = context.driver.find_element(By.XPATH, '//*[@id="desktop-wrapper"]/div[3]/div/input')
        context.search.time = data
    ActionChains(context.driver).click(input_field).key_down(Keys.CONTROL).send_keys(
        "a").key_up(Keys.CONTROL).send_keys(data).perform()


@then(u'I should see only rides with later start date')
def step_impl(context):
    container = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]')
    try:
        rides = container.find_elements_by_css_selector("div[class*=css-l0b0zb")
        for ride in rides:
            ride_params = ride.find_elements(By.TAG_NAME, 'h4')

            date_ride = datetime.datetime.strptime(ride_params[0].text, "%d.%m.%Y").date()
            date_filter = datetime.datetime.strptime(context.search.date, "%d.%m.%Y").date()
            assert date_ride >= date_filter
    except Exception:
        assert False


@then(u'I should see only rides with later start time')
def step_impl(context):
    container = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]')
    try:
        rides = container.find_elements_by_css_selector("div[class*=css-l0b0zb")
        for ride in rides:
            ride_params = ride.find_elements(By.TAG_NAME, 'h4')

            time_ride = datetime.datetime.strptime(ride_params[1].text, "%H:%M").time()
            time_filter = datetime.datetime.strptime(context.search.time, "%H:%M").time()
            assert time_ride >= time_filter
    except Exception:
        assert False


@when(u'I input {price} as {trend} price')
def step_impl(context, price, trend):
    wrapper = context.driver.find_element(By.XPATH, '//*[@id="desktop-wrapper"]/div[5]')
    inputs = wrapper.find_elements(By.TAG_NAME, 'input')

    if trend == 'min':
        input_field = inputs[0]
        context.search.price_min = float(price)
    else:
        input_field = inputs[1]
        context.search.price_max = float(price)
    input_field.send_keys(price)
    sleep(4)


@then(u'I should see only rides with {trend} price')
def step_impl(context, trend):
    container = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]')
    try:
        rides = container.find_elements_by_css_selector("div[class*=css-l0b0zb")
        for ride in rides:
            price = ride.find_elements(By.CSS_SELECTOR, '*>h5>span')[1]
            price = float(price.text[:-2])
            if context.search.price_min is not None:
                assert price >= context.search.price_min
            else:
                assert price <= context.search.price_max
    except Exception:
        assert False


@when(u'I click on 3 stars')
def step_impl(context):
    star = context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[3]/div[1]/div[4]/div/span/label[3]')
    star.click()
    sleep(4)


@then(u'I should see only rides from drivers with {stars} stars and more')
def step_impl(context, stars):
    container = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]')
    try:
        rides = container.find_elements_by_css_selector("div[class*=css-l0b0zb")
        for ride in rides:
            ride_params = ride.find_elements(By.TAG_NAME, 'h4')
            user_stars = float(ride_params[5].text)
            assert user_stars >= float(stars)
    except Exception:
        assert False
