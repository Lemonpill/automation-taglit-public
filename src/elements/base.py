from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.config import Config as cfg


class BasePageElement(object):
    """Base class containing actions
    for page elements (fill, click, etc.)
    """

    def __init__(self, page) -> None:
        self.page = page

    def locate(self):
        try:
            el = WebDriverWait(self.page.driver, cfg.LOCATE_TIMEOUT).until(
                EC.visibility_of_element_located(self.locator)
            )
        except Exception:
            raise Exception("failed to locate element")

        return el

    def select(self, value):
        # Locate element
        e = self.locate()

        # Send new value
        try:
            e.send_keys(value)
        except Exception:
            raise Exception("failed to fill in value")

    def fill(self, value):
        # Locate element
        e = self.locate()

        # Empty element and send value
        try:
            e.clear()
            e.send_keys(value)
        except Exception:
            raise Exception("failed to fill in value")

    def click(self):
        # Locate element
        e = self.locate()

        # Click element
        try:
            e.click()
        except Exception:
            raise Exception("failed to fill in value")