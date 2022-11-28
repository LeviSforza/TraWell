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
    dates = []
    for ride in rides:
        if parameter == 'date':
            ride_date = ride.find_elements(By.TAG_NAME, 'h4')[0]
            date = datetime.datetime.strptime(ride_date.text, "%d.%m.%Y").date()
        elif parameter == 'duration':
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[0]
            date = datetime.datetime.strptime(ride_duration.text, "%Hh %M min").time()
        elif parameter == 'price':
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[2]
            date = float(ride_duration.text[:-2])
        else:
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[1]
            date = ride_duration.text[0]
        dates.append(date)

    if order == 'decreasing':
        assert dates == sorted(dates, reverse=True)
    else:
        assert dates == sorted(dates)

