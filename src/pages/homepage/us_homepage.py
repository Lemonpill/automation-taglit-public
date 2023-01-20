from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from src.pages.basepage import BasePage
from src.config import Config as cfg
from src.element import (
    BtnHomeCookiesCTA,
    BtnHomeCloseLightbox,
    BtnHomeNavbarLogin,
    BtnHomeSignupTab,
    BtnHomeLoginTab,
    BtnHomeEmailSignup,
    BtnHomeEmailLogin,
    FldHomeLoginEmail,
    BtnHomeLoginSubmitEmail,
    FldHomeLoginOTP,
    FldHomeSignupFirstName,
    FldHomeSignupLastName,
    FldHomeSignupBirthDate,
    FldHomeSignupEmail,
    FldHomeSignupFamilyRelations,
    RadHomeFamilyRelationsFather,
    FldHomeSignupPhone,
    BtnHomeSignupButton,
    BtnHomeSignupScrollTerms,
    BtnHomeSignupAcceptTerms,
)


class HomepageUS(BasePage):
    """ Class containing actions available
        on United States homepage
    """

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

        # URL
        if cfg.ENVIRONMENT == "PROD":
            self.base_url = "http://www.birthrightisrael.com/"
        else:
            self.base_url = "http://www.taglit.info/"
        
        # Country
        self.iso = "US"

        # Title
        self.title = "A Free Trip to Israel | Taglit - Birthright Israel"

        # Elements
        self.btn_cookies_cta = BtnHomeCookiesCTA(self)
        self.btn_close_lightbox = BtnHomeCloseLightbox(self)
        self.btn_navbar_login = BtnHomeNavbarLogin(self)
        self.btn_signup_tab = BtnHomeSignupTab(self)
        self.btn_login_tab = BtnHomeLoginTab(self)
        self.btn_email_signup = BtnHomeEmailSignup(self)
        self.btn_email_login = BtnHomeEmailLogin(self)
        self.fld_login_email = FldHomeLoginEmail(self)
        self.btn_login_submit = BtnHomeLoginSubmitEmail(self)
        self.fld_login_otp = FldHomeLoginOTP(self)
        self.fld_signup_fname = FldHomeSignupFirstName(self)
        self.fld_signup_lname = FldHomeSignupLastName(self)
        self.fld_signup_birth_date = FldHomeSignupBirthDate(self)
        self.fld_signup_email = FldHomeSignupEmail(self)
        self.fld_family_rel = FldHomeSignupFamilyRelations(self)
        self.rad_family_rel_father = RadHomeFamilyRelationsFather(self)
        self.fld_signup_phone = FldHomeSignupPhone(self)
        self.btn_signup_button = BtnHomeSignupButton(self)
        self.btn_signup_scroll_terms = BtnHomeSignupScrollTerms(self)
        self.btn_signup_accept_terms = BtnHomeSignupAcceptTerms(self)
        

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
            self.btn_cookies_cta.see_and_click()
        except Exception:
            raise Exception("failed to click cookies cta")

    def close_lightbox(self):
        try:
            self.btn_close_lightbox.see_and_click()
        except Exception:
            raise Exception("failed to close lightbox")

    def open_login_popup(self):
        try:
            self.btn_navbar_login.see_and_click()
        except Exception:
            raise Exception("failed to open login popup")

    def open_signup_tab(self):
        try:
            self.btn_signup_tab.see_and_click()
        except Exception:
            raise Exception("failed to open signup tab")

    def open_login_tab(self):
        try:
            self.btn_login_tab.see_and_click()
        except Exception:
            raise Exception("failed to open login tab")

    def open_email_signup(self):
        try:
            self.btn_email_signup.see_and_click()
        except Exception:
            raise Exception("failed to open email signup")

    def open_email_login(self):
        try:
            self.btn_email_login.see_and_click()
        except Exception:
            raise Exception("failed to open email login")

    def fill_login_email(self, value):
        try:
            self.fld_login_email.see_and_fill(value)
        except Exception:
            raise Exception("failed to fill login email")

    def submit_login(self):
        try:
            self.btn_login_submit.see_and_click()
        except Exception:
            raise Exception("failed to submit login")

    def fill_login_otp(self, value):
            try:
                self.fld_login_otp.see_and_fill(value)
            except Exception:
                raise Exception("failed to fill login otp")

    def fill_signup_first_name(self, value):
        try:
            self.fld_signup_fname.see_and_fill(value)
        except Exception:
            raise Exception("failed to fill signup first name")

    def fill_signup_last_name(self, value):
        try:
            self.fld_signup_lname.see_and_fill(value)
        except Exception:
            raise Exception("failed to fill signup last name")

    def fill_signup_birth_date(self, value):
        try:
            self.fld_signup_birth_date.see_and_fill(value)
        except Exception:
            raise Exception("failed to fill signup birth date")

    def fill_signup_email(self, value):
        try:
            self.fld_signup_email.see_and_fill(value)
        except Exception:
            raise Exception("failed to fill signup email")

    def toggle_family_relation(self):
        try:
            self.fld_family_rel.see_and_click()
        except Exception:
            raise Exception("failed to toggle family relation")

    def check_family_relation_father(self):
        try:
            self.rad_family_rel_father.see_and_click()
        except Exception:
            raise Exception("failed to check father relation")

    def fill_signup_phone(self, value):
        try:
            self.fld_signup_phone.see_and_fill(value)
        except Exception:
            raise Exception("failed to fill signup phone")

    def submit_signup(self):
        try:
            self.btn_signup_button.see_and_click()
        except Exception:
            raise Exception("failed to submit signup")

    def scroll_terms(self):
        try:
            self.btn_signup_scroll_terms.see_and_click()
        except Exception:
            raise Exception("failed to scroll down terms")

    def accept_terms(self):
        try:
            self.btn_signup_accept_terms.see_and_click()
        except Exception:
            raise Exception("failed to accept terms of service")
