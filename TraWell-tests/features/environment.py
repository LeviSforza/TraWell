import behave_webdriver
from selenium import webdriver # or any custom webdriver
from behave_webdriver.driver import BehaveDriverMixin
from seleniumrequests import RequestMixin # or your own mixin

class BehaveRequestDriver(BehaveDriverMixin, RequestMixin, webdriver.Chrome):
    pass

# def before_all(context):
#     context.behave_driver = behave_webdriver.Chrome()

# def after_all(context):
#     # cleanup after tests run
#     context.behave_driver.quit()

def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(2)

    
def after_feature(context, feature):
    context.driver.quit()

# https://testuj.pl/blog/test-automatyczny-bdd-w-selenium-z-wykorzystaniem-python-i-behave-instrukcja-krok-po-kroku/
