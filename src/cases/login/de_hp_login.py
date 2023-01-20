import os
import time
import csv
import unittest
import logging

from lxml import html
from selenium.webdriver.chrome.webdriver import WebDriver

from src.config import Config as cfg
from src.pages.homepage.de_homepage import HomepageDE
from src.pages.application.de_application import RegistrationFormsDE
from src.reporter import Reporter
from src.mailbox import Mailbox
from src.helpers import extract_otp


logger = logging.getLogger(__name__)


class DEHomeLoginChrome(unittest.TestCase):
    """ Germany - Homepage - Login with valid email (Chrome) """

    def setUp(self) -> None:
        self.name = "DEHomeLoginChrome"
        self.driver = WebDriver("C:\BrowserDrivers\chromedriver.exe")
        self.page = HomepageDE(self.driver)

        self.reporter = Reporter(self.driver, self.page.iso, self.name)
        self.get_mailbox()

    def get_mailbox(self) -> None:
        self.test_email = None

        if os.path.exists(self.reporter.userspath):
            with open(self.reporter.userspath, "r", newline="") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if r["Country"] == self.page.iso:
                        self.test_email = r["Email"]
        else:
            self.fail("failed to read users file")

        if not self.test_email:
            self.fail("failed to find test email")

        self.mailbox = Mailbox(self.test_email)

    def get_email_otp(self) -> str:
        """ Check for OTP code email every 5 seconds\n
            Returns OTP or fails test case
        """

        # Limit to 5 attempts
        for _ in range(5):

            if not self.mailbox.has_new_messages():
                time.sleep(5)
                continue

            last_msg = self.mailbox.get_last_message()
            
            try:
                # Extract HTML from email
                tree = html.fromstring(last_msg["htmlBody"])

                # Extract text content from HTML
                text = tree.text_content()

                # Extract OTP from text content
                code = extract_otp(text)
            except Exception:
                self.fail("failed to extract otp")

            if not code.isnumeric():
                self.fail(f"unexpected otp: {code}") 

            return code

        self.fail("did not receive otp")

    def test_valid_login(self) -> None:

        logger.info(f"{self.name}.test_valid_login started")

        self.driver.maximize_window()
        step_n = 0

        # Open homepage
        step_n += 1
        step = "open homepage"

        try:
            self.page.open()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Verify title
        step_n += 1
        step = "verify title"

        try:
            self.page.verify_title()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Accept cookies
        step_n += 1
        step = "accept cookies"

        try:
            self.page.accept_cookies()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Open login popup
        step_n += 1
        step = "open login modal"

        try:
            self.page.open_login_popup()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Open login tab
        step_n += 1
        step = "open login tab"

        try:
            self.page.open_login_tab()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Fill login email
        step_n += 1
        step = "fill login email"

        try:
            self.page.fill_login_email(self.mailbox.email)
        except Exception:
            self.reporter.write(step_n, step, self.mailbox.email, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Submit login email
        step_n += 1
        step = "submit login email"

        try:
            self.page.submit_login()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Get login OTP
        step_n += 1
        step = "get login otp"

        try:
            code = self.get_email_otp()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Fill login OTP
        step_n += 1
        step = "fill login otp"

        try:
            self.page.fill_login_otp(code)
        except Exception:
            self.reporter.write(step_n, step, code, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)


        # Landing in registration forms
        reg_forms = RegistrationFormsDE(self.driver)


        # Verify choose a trip shown
        step_n += 1
        step = "verify regforms cta"

        try:
            reg_forms.verify_page_loaded()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.SCREENSHOT_WAIT)
        self.reporter.write(step_n, step)

        logger.info(f"{self.name}.test_valid_login finished")

    def tearDown(self) -> None:
        self.driver.quit()