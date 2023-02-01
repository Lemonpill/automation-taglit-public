import time
import unittest
import logging

from selenium.webdriver.chrome.webdriver import WebDriver

from src.config import Config as cfg
from src.pages import CanadaHomepage as Homepage, BaseApplication as Application
from src.reporter import Reporter
from src.mailbox import Mailbox


logger = logging.getLogger(__name__)


class SignupHomepageCanada(unittest.TestCase):
    """Canada - Homepage - Signup with valid details (Chrome)"""

    def setUp(self) -> None:
        self.name = "SignupHomepageCanada"
        self.driver = WebDriver(cfg.CHROMEDRIVER_PATH)
        self.page = Homepage(self.driver)

        self.reporter = Reporter(self.driver, self.page.iso, self.name)

    def test_valid_signup(self) -> None:

        logger.info(f"{self.name}.test_valid_signup started")

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

        # Open login popup
        step_n += 1
        step = "open login modal"

        try:
            self.page.open_login_popup()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Open signup tab
        step_n += 1
        step = "open signup tab"

        try:
            self.page.open_signup_tab()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Open email signup
        step_n += 1
        step = "open email signup"

        try:
            self.page.open_email_signup()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Fill in valid first name
        step_n += 1
        step = "fill first name"

        fname = "QA"

        try:
            self.page.fill_signup_first_name(fname)
        except Exception:
            self.reporter.write(step_n, step, fname, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, fname)

        # Fill in valid last name
        step_n += 1
        step = "fill last name"

        lname = "Tester"

        try:
            self.page.fill_signup_last_name(lname)
        except Exception:
            self.reporter.write(step_n, step, lname, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, lname)

        # Fill in valid date of birth
        step_n += 1
        step = "fill birth date"

        bdate = "01012000"

        try:
            self.page.fill_signup_birth_date(bdate)
        except Exception:
            self.reporter.write(step_n, step, bdate, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, bdate)

        # Generate email from 1secemail
        step_n += 1
        step = "generate email"

        try:
            mailbox = Mailbox()
        except Exception:
            self.reporter.save_step(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        self.reporter.save_step(step_n, step, mailbox.email)

        # Fill in valid email
        step_n += 1
        step = "fill email"

        email = mailbox.email

        try:
            self.page.fill_signup_email(email)
        except Exception:
            self.reporter.write(step_n, step, email, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, email)

        # Open family relation dropdown
        step_n += 1
        step = "open family relation"

        try:
            self.page.toggle_family_relation()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Check father relation
        step_n += 1
        step = "check father relation"

        try:
            self.page.check_family_relation_father()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Close family relation dropdown
        step_n += 1
        step = "close family relation"

        try:
            self.page.toggle_family_relation()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Fill in valid phone
        step_n += 1
        step = "fill phone"

        phone = "876878769786"

        try:
            self.page.fill_signup_phone(phone)
        except Exception:
            self.reporter.write(step_n, step, phone, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step, phone)

        # Submit signup form
        step_n += 1
        step = "submit signup"

        try:
            self.page.submit_signup()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Scroll down terms of service
        step_n += 1
        step = "scroll terms"

        try:
            self.page.scroll_terms()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Accept terms of service
        step_n += 1
        step = "accept terms"

        try:
            self.page.accept_terms()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Landing in registration forms
        application = Application(self.driver)

        # Verify regforms loaded
        step_n += 1
        step = "verify regforms loaded"

        try:
            application.verify_page_loaded()
        except Exception:
            self.reporter.write(step_n, step, ok=False)
            self.fail(f"failed to {step}")

        time.sleep(cfg.ANIMATION_DELAY)
        self.reporter.write(step_n, step)

        # Save test user
        self.reporter.save_user(email)

        logger.info(f"{self.name}.test_valid_signup finished")

    def tearDown(self) -> None:
        self.driver.quit()
