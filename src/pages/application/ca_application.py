from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base import BasePage
from src.element import BtnFormsChooseTrip, ScnFormsTravelSeason


class RegistrationFormsCA(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # ELEMENTS
        self.btn_choose_trip = BtnFormsChooseTrip(self)
        self.scn_travel_season = ScnFormsTravelSeason(self)

    def verify_page_loaded(self):
        try:
            self.scn_travel_season.locate()
        except Exception:
            raise Exception("failed to verify page loaded")
