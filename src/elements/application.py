from selenium.webdriver.common.by import By

from src.elements.base_element import BasePageElement


class ChooseTripButton(BasePageElement):
    """Registration forms 'Choose Trip' CTA"""

    locator = (By.CSS_SELECTOR, "button[data-qa-id='action-GetStarted-button']")


class TravelSeasonSection(BasePageElement):
    """Registration forms 'Travel season' section"""

    locator = (By.CSS_SELECTOR, "#FORM-GetStarted")
