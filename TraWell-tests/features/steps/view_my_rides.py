from time import sleep

from behave import *
from models.ride import RideDetails
from selenium.webdriver.common.by import By


@when(u'I click on "{tab_name}" tab')
def step_impl(context, tab_name):
    context.ride = RideDetails()
    tabs = context.driver.find_elements(By.CSS_SELECTOR, 'button[role="tab"]')
    if tab_name == "RECURRENT AS DRIVER":
        tab = tabs[1]
    elif tab_name == "SINGULAR AS PASSENGER":
        tab = tabs[2]
    else:
        tab = tabs[0]
    tab.click()


@then(u'I should see only my recurrent rides')
def step_impl(context):
    rides = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*=css-109v0wb]')
    for ride in rides:
        ride_type = ride.find_elements(By.TAG_NAME, 'h4')[0].text
        assert ride_type == 'recurrent'


@then(u'I have option to edit, delete and view details of each ride')
def step_impl(context):
    rides = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*=css-109v0wb]')
    for ride in rides:
        buttons = ride.find_elements(By.TAG_NAME, 'button')
        assert len(buttons) == 3
        assert buttons[0].text == 'EDIT'
        assert buttons[1].text == 'DELETE'
        assert buttons[2].text == 'DETAILS'


@then(u'I should see my rides as passenger with option to view details of each ride')
def step_impl(context):
    rides = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*=css-109v0wb]')
    for ride in rides:
        buttons = ride.find_elements(By.TAG_NAME, 'button')
        assert len(buttons) == 1
        assert buttons[0].text == 'DETAILS'


@when(u'I click "DETAILS" button of first ride')
def step_impl(context):
    ride = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*=css-109v0wb]')[0]
    ride_data = ride.find_elements(By.TAG_NAME, 'h4')

    context.ride.city_from = ride_data[3].text
    context.ride.city_to = ride_data[5].text
    context.ride.date = ride_data[1].text
    context.ride.start_time = ride_data[2].text
    context.ride.end_time = ride_data[4].text

    details_btn = ride.find_elements(By.TAG_NAME, 'button')[0]
    details_btn.click()


@then(u'I should see details of the ride')
def step_impl(context):
    sleep(1)
    ride_data = context.driver.find_elements(By.CSS_SELECTOR, 'h4[class]')
    assert context.ride.start_time == ride_data[0].text
    assert context.ride.end_time == ride_data[2].text

    ride_data = context.driver.find_elements(By.CSS_SELECTOR, 'h3[class]')
    assert context.ride.city_from == ride_data[2].text
    assert context.ride.city_to == ride_data[3].text
    assert context.ride.date == ride_data[0].text
