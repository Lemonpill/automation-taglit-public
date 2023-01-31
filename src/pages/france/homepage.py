from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage
from src.config import Config as cfg
from src.elements.homepage import (
    CookiesAcceptButton,
    NavbarLoginButton,
    SignupTabButton,
    LoginTabButton,
    EmailSignupButton,
    EmailLoginButton,
    LoginEmailField,
    LoginSubmitButton,
    LoginOTPField,
    SignupFirstNameField,
    SignupLastNameField,
    SignupBirthDateField,
    SignupEmailField,
    SignupGenderSelection,
    SignupPhoneField,
    SignupSubmitButton,
    ScrollDownTermsButton,
    AcceptTermsButton,
)


class Homepage(BasePage):
    """Class containing actions available
    on France homepage
    """

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        # URL
        if cfg.ENVIRONMENT == "PROD":
            self.base_url = "http://fr.birthrightisrael.com/"
        else:
            self.base_url = "http://fr.taglit.info/"

        # Country
        self.iso = "FR"

        # Title
        self.title = "Taglit | Un voyage offert en Israël"

        # Elements
        self.btn_cookies_cta = CookiesAcceptButton(driver)
        self.btn_navbar_login = NavbarLoginButton(driver)
        self.btn_signup_tab = SignupTabButton(driver)
        self.btn_login_tab = LoginTabButton(driver)
        self.btn_email_signup = EmailSignupButton(driver)
        self.btn_email_login = EmailLoginButton(driver)
        self.fld_login_email = LoginEmailField(driver)
        self.btn_login_submit = LoginSubmitButton(driver)
        self.fld_login_otp = LoginOTPField(driver)
        self.fld_signup_fname = SignupFirstNameField(driver)
        self.fld_signup_lname = SignupLastNameField(driver)
        self.fld_signup_birth_date = SignupBirthDateField(driver)
        self.fld_signup_email = SignupEmailField(driver)
        self.fld_signup_gender = SignupGenderSelection(driver)
        self.fld_signup_phone = SignupPhoneField(driver)
        self.btn_signup_button = SignupSubmitButton(driver)
        self.btn_signup_scroll_terms = ScrollDownTermsButton(driver)
        self.btn_signup_accept_terms = AcceptTermsButton(driver)

    def open(self):
        try:
            self.driver.get(self.base_url)
        except Exception:
            raise Exception("failed to open page")

    def verify_title(self):
        try:
            assert self.title in self.driver.title
        except AssertionError:
            raise Exception("failed to verify title")

    def accept_cookies(self):
        try:
            self.btn_cookies_cta.click()
        except Exception:
            raise Exception("failed to click cookies cta")

    def open_login_popup(self):
        try:
            self.btn_navbar_login.click()
        except Exception:
            raise Exception("failed to open login popup")

    def open_signup_tab(self):
        try:
            self.btn_signup_tab.click()
        except Exception:
            raise Exception("failed to open signup tab")

    def open_login_tab(self):
        try:
            self.btn_login_tab.click()
        except Exception:
            raise Exception("failed to open login tab")

    def open_email_signup(self):
        try:
            self.btn_email_signup.click()
        except Exception:
            raise Exception("failed to open email signup")

    def open_email_login(self):
        try:
            self.btn_email_login.click()
        except Exception:
            raise Exception("failed to open email login")

    def fill_login_email(self, value):
        try:
            self.fld_login_email.fill(value)
        except Exception:
            raise Exception("failed to fill login email")

    def submit_login(self):
        try:
            self.btn_login_submit.click()
        except Exception:
            raise Exception("failed to submit login")

    def fill_login_otp(self, value):
        try:
            self.fld_login_otp.fill(value)
        except Exception:
            raise Exception("failed to fill login otp")

    def fill_signup_first_name(self, value):
        try:
            self.fld_signup_fname.fill(value)
        except Exception:
            raise Exception("failed to fill signup first name")

    def fill_signup_last_name(self, value):
        try:
            self.fld_signup_lname.fill(value)
        except Exception:
            raise Exception("failed to fill signup last name")

    def fill_signup_birth_date(self, value):
        try:
            self.fld_signup_birth_date.fill(value)
        except Exception:
            raise Exception("failed to fill signup birth date")

    def fill_signup_email(self, value):
        try:
            self.fld_signup_email.fill(value)
        except Exception:
            raise Exception("failed to fill signup email")

    def fill_signup_gender(self, value):
        try:
            self.fld_signup_gender.select(value)
        except Exception:
            raise Exception("failed to fill signup gender")

    def fill_signup_phone(self, value):
        try:
            self.fld_signup_phone.fill(value)
        except Exception:
            raise Exception("failed to fill signup phone")

    def submit_signup(self):
        try:
            self.btn_signup_button.click()
        except Exception:
            raise Exception("failed to submit signup")

    def scroll_terms(self):
        try:
            self.btn_signup_scroll_terms.click()
        except Exception:
            raise Exception("failed to scroll down terms")

    def accept_terms(self):
        try:
            self.btn_signup_accept_terms.click()
        except Exception:
            raise Exception("failed to accept terms of service")
