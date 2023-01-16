from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    """ Base page object for implementing page-object model """
    
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver