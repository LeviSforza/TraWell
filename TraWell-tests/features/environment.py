from selenium import webdriver  # or any custom webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    context.driver = webdriver.Chrome(executable_path=r'.\drivers\chromedriver.exe', options=options)
    # context.driver.get(".//drivers//chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)


def after_all(context):
    # cleanup after tests run
    # context.driver.quit()
    pass



# def before_feature(context, feature):
#     context.driver = webdriver.Chrome()
#     context.driver.get("drivers/chromedriver.exe")
#     context.driver.implicitly_wait(2)
#
#
# def after_feature(context, feature):
#     context.driver.quit()

# https://testuj.pl/blog/test-automatyczny-bdd-w-selenium-z-wykorzystaniem-python-i-behave-instrukcja-krok-po-kroku/
