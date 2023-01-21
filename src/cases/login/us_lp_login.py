import time
import unittest
import logging

from selenium.webdriver.chrome.webdriver import WebDriver

from src.config import Config as cfg
from src.pages.loginpage.us_loginpage import LoginpageUS
from src.pages.application.us_application import RegistrationFormsUS
from src.reporter import Reporter
from src.mailbox import Mailbox
from src.helpers import extract_otp, get_email_from_csv, extract_message_text


logger = logging.getLogger(__name__)


class USLoginLoginChrome(unittest.TestCase):
    """United States - Login page - Login with valid email (Chrome)"""

    def setUp(self) -> None:
        self.name = "USLoginLoginChrome"
        self.driver = WebDriver(cfg.CHROMEDRIVER_PATH)
        self.page = LoginpageUS(self.driver)

        self.reporter = Reporter(self.driver, self.page.iso, self.name)

        self.test_email = get_email_from_csv(
            path=self.reporter.userspath, iso=self.page.iso
        )

        if not self.test_email:
            self.fail("failed to get test email")

        self.mailbox = Mailbox(self.test_email)

    def test_valid_login(self) -> None:

        logger.info(f"{self.name}.test_valid_login started")

        self.driver.maximize_window()
        step_n = 0

        # Open login page
        step_n += 1
        step = "open login page"

        try:
            self.page.open()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Verify title
        step_n += 1
        step = "verify title"

        try:
            self.page.verify_title()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Accept cookies
        step_n += 1
        step = "accept cookies"

        try:
            self.page.accept_cookies()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Select email login
        step_n += 1
        step = "open email login"

        try:
            self.page.open_email_login()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY )
        self.reporter.write(step_n, step)

        # Fill login email
        step_n += 1
        step = "fill login email"

        email = self.mailbox.email

        try:
            self.page.fill_login_email(email)
        except Exception:
            self.reporter.write(step_n, step, email, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, email)

        # Submit login email
        step_n += 1
        step = "submit login email"

        try:
            self.page.submit_login()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Get login OTP
        step_n += 1
        step = "get login otp"

        message = None

        # Check for new messages every 5 seconds
        for _ in range(5):
            if self.mailbox.has_new_messages():
                message = self.mailbox.get_last_message()
                break
            time.sleep(5)

        try:
            # Extract message text
            text = extract_message_text(message)
            # Extract 5 digit code from text
            code = extract_otp(text)
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to extract otp")

        # Fill login OTP
        step_n += 1
        step = "fill login otp"

        try:
            self.page.fill_login_otp(code)
        except Exception:
            self.reporter.write(step_n, step, code, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, code)

        # Landing in registration forms
        reg_forms = RegistrationFormsUS(self.driver)

        # Verify regforms loaded
        step_n += 1
        step = "verify regforms loaded"

        try:
            reg_forms.verify_page_loaded()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        logger.info(f"{self.name}.test_valid_login finished")

    def tearDown(self) -> None:
        self.driver.quit()
