import os

from dotenv import load_dotenv
from keycloak import KeycloakAdmin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

keycloak_admin = KeycloakAdmin(server_url='http://localhost:8403/auth/',
                               username=os.getenv("ADMIN_USERNAME"),
                               password=os.getenv("ADMIN_PASSWORD"),
                               realm_name=os.getenv("REALM"),
                               verify=True)


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--window-size=2560,1440")

    context.driver = webdriver.Chrome(executable_path=r'.\drivers\chromedriver.exe', options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)

    # Add user and set password
    user_id_keycloak = keycloak_admin.get_user_id("olga@tokarczuk.com")
    if user_id_keycloak is None:
        new_user = keycloak_admin.create_user({
            "email": "olga@tokarczuk.com",
            "username": "olga@tokarczuk.com",
            "enabled": True,
            "emailVerified": True,
            "firstName": "Olga",
            "lastName": "Tokarczuk",
            "credentials": [{
                "value": "correct_pass",
                "type": "password",
            }],
            "attributes": {
                "user_type": "Private User",
                "date_of_birth": "1999-01-01",
                "facebook": "https://www.instagram.com/",
                "instagram": "https://www.instagram.com/"
            }
        })


def after_all(context):
    context.driver.delete_all_cookies()
    context.driver.quit()

    user_id_keycloak = keycloak_admin.get_user_id("olga@tokarczuk.com")
    if user_id_keycloak is not None:
        keycloak_admin.delete_user(user_id=user_id_keycloak)


def after_feature(context, feature):
    if feature.name == 'Creating account functionality':
        user_id_keycloak = keycloak_admin.get_user_id("anna@mak.com")
        if user_id_keycloak is not None:
            keycloak_admin.delete_user(user_id=user_id_keycloak)


def after_scenario(context, scenario):
    if scenario.name == "Login successfully" or scenario.name == 'View profile':
        print("Run After Each Scenario")
        navbar = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div/header/div/div')))
        # open menu
        navbar.find_elements(By.CSS_SELECTOR, 'button[aria-label="Open settings"]')[1].click()
        context.driver.find_elements(By.XPATH, '//*[@id="menu-appbar"]/div[3]/ul/a[4]/li')[2].click()
