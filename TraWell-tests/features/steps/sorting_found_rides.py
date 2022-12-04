import datetime

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click on "Sort by" filed')
def step_impl(context):
    sort_by = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#simple-select')))
    sort_by.click()


@when(u'I click on "Date: {order} first"')
def step_impl(context, order):
    minus = '-' if order == 'highest' else ''
    sort_value = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{minus}start_date"]')))
    sort_value.click()


@when(u'I click on "Duration: {order} first"')
def step_impl(context, order):
    minus = '-' if order == 'highest' else ''
    sort_value = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{minus}duration"]')))
    sort_value.click()


@when(u'I click on "Price: {order} first"')
def step_impl(context, order):
    minus = '-' if order == 'highest' else ''
    sort_value = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{minus}price"]')))
    sort_value.click()


@when(u'I click on "Available seats: {order} first"')
def step_impl(context, order):
    minus = '-' if order == 'highest' else ''
    sort_value = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-value="{minus}available_seats"]')))
    sort_value.click()


@then(u'I should see rides sorted by {parameter} - {order}')
def step_impl(context, parameter, order):
    rides = context.driver.find_elements(By.CSS_SELECTOR, "div[class*=css-l0b0zb]")
    rides_params = []
    for ride in rides:
        if parameter == 'date':
            ride_elem = ride.find_elements(By.TAG_NAME, 'h4')[0]
            param = datetime.datetime.strptime(ride_elem.text, "%d.%m.%Y").date()
        elif parameter == 'duration':
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[0]
            hours = ride_duration.text.split("h")[0]
            minutes = ride_duration.text.split(" ")[1]
            print(f'hours: {hours} and minutes: {minutes}')
            param = int(hours) * 60 + int(minutes)
        elif parameter == 'price':
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[2]
            param = float(ride_duration.text[:-2])
        else:
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[1]
            param = ride_duration.text[0]
        rides_params.append(param)

    if order == 'decreasing':
        assert rides_params == sorted(rides_params, reverse=True)
    else:
        assert rides_params == sorted(rides_params)

