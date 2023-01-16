from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.basepage import BasePage
from src.element import BtnFormsChooseTrip


class RegistrationFormsSU(BasePage):
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # ELEMENTS
        self.btn_choose_trip = BtnFormsChooseTrip(self)

    def verify_page_loaded(self):
        try:
            self.btn_choose_trip.wait_until_visible()
        except Exception:
            raise Exception("failed to verify page loaded")