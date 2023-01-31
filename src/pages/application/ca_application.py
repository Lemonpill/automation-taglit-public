from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base import BasePage
from src.elements.application import ChooseTripButton, TravelSeasonSection


class RegistrationFormsCA(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # ELEMENTS
        self.btn_choose_trip = ChooseTripButton(driver)
        self.div_travel_season = TravelSeasonSection(driver)

    def verify_page_loaded(self):
        try:
            self.div_travel_season.locate()
        except Exception:
            raise Exception("failed to verify page loaded")
