import datetime

from behave import *
from models.search import Search
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'I chosen "My rides" from navigation bar')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#my-rides-desktop').click()
    context.search = Search()


@when(u'I input "{date}" as Start Date field')
def step_impl(context, date):
    input_field = context.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="dd/mm/yyyy"]')
    ActionChains(context.driver).click(input_field).key_down(Keys.CONTROL).send_keys(
        "a").key_up(Keys.CONTROL).send_keys(date).perform()
    context.search.date = date


@then(u'I should see rides with later start date')
def step_impl(context):
    rides = context.driver.find_elements_by_css_selector("div[class*=css-109v0wb")
    for ride in rides:
        ride_params = ride.find_elements(By.TAG_NAME, 'h4')

        date_ride = datetime.datetime.strptime(ride_params[1].text, "%d.%m.%Y").date()
        date_filter = datetime.datetime.strptime(context.search.date, "%d.%m.%Y").date()
        assert date_ride >= date_filter

