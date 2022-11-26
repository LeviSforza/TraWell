import os
from pathlib import Path

from behave import *
from dotenv import load_dotenv
from keycloak import KeycloakAdmin
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click on "My profile" button in user menu')
def step_impl(context):
    open_setting_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#icon-settings-desktop')))
    open_setting_icon.click()
    context.driver.find_element(By.CSS_SELECTOR, '#my-profile-desktop-button').click()


@then(u'I should see my user profile')
def step_impl(context):
    assert context.driver.current_url.startswith('http://localhost:5173/profile/')

    user_name = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[1]/h3')
    assert user_name.text == 'Olga Tokarczuk'

