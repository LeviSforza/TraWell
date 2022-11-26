import datetime
import os
from pathlib import Path
from time import sleep

from behave import *
from dotenv import load_dotenv
from keycloak import KeycloakAdmin
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from models.search import Search


@given(u'I chosen "My rides" from navigation bar')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#my-rides-desktop').click()


@when(u'I input "Czastary" as place from')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input "Czastary" as place from')


@then(u'I should see only rides from "Czastary"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see only rides from "Czastary"')


@when(u'I input "Wroclaw" as place to')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input "Wroclaw" as place to')


@then(u'I should see only rides to "Wrocław"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see only rides to "Wrocław"')
