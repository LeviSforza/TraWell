import datetime

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@then(u'I should see my rides sorted by {parameter} {order}')
def step_impl(context, parameter, order):
    rides = context.driver.find_elements(By.CSS_SELECTOR, "div[class*=css-109v0wb]")
    rides_params = []
    for ride in rides:
        if parameter == 'date':
            ride_elem = ride.find_elements(By.TAG_NAME, 'h4')[1]
            param = datetime.datetime.strptime(ride_elem.text, "%d.%m.%Y").date()
        elif parameter == 'duration':
            ride_duration = ride.find_elements(By.TAG_NAME, 'span')[0]
            param = datetime.datetime.strptime(ride_duration.text, "%Hh %M min").time()
        else:
            assert False
        rides_params.append(param)

    if order == 'decreasing':
        assert rides_params == sorted(rides_params, reverse=True)
    else:
        assert rides_params == sorted(rides_params)
