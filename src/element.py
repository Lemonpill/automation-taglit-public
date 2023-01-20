from selenium.webdriver.common.by import By
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


class BtnHomeCookiesCTA(BasePageElement):
    """Homepage cookies CTA"""

    locator = (By.CSS_SELECTOR, "#app > div.toastWrapper > section > div.primaryButton")


class BtnHomeCloseLightbox(BasePageElement):
    """Home page lightbox 'X' icon"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.generalPopupWrapper.popup_container > div > div > span",
    )


class BtnHomeNavbarLogin(BasePageElement):
    """Navigation bar LOGIN button"""

    locator = (
        By.CSS_SELECTOR,
        "#desktopList > li.showIn-desktop.showIn-tablet.showIn-mobile > a",
    )


class BtnHomeSignupTab(BasePageElement):
    """Login modal Signup tab button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.tabsContainerNew > div:nth-child(1)",
    )


class BtnHomeLoginTab(BasePageElement):
    """Login modal Login tab button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.login > div.signUp.primaryButton",
    )


class BtnHomeEmailSignup(BasePageElement):
    """Login modal 'Signup with email' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.signUp > div.signUp.primaryButton",
    )


class BtnHomeEmailLogin(BasePageElement):
    """Login modal 'Login with email' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.login > div.signUp.primaryButton",
    )


class FldHomeLoginEmail(BasePageElement):
    """Login modal 'email' field"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.login.loginWithMailWrapper > form > div > input[type=text]",
    )


class FldHomeLoginOTP(BasePageElement):
    """Login modal 'OTP' field"""

    locator = (By.CSS_SELECTOR, "#digit_1")


class FldHomeSignupFirstName(BasePageElement):
    """Signup modal 'first name' field"""

    locator = (By.NAME, "first_name")


class FldHomeSignupLastName(BasePageElement):
    """Signup modal 'last name' field"""

    locator = (By.NAME, "last_name")


class FldHomeSignupBirthDate(BasePageElement):
    """Signup modal 'birth date' field"""

    locator = (By.NAME, "birth_date")


class FldHomeSignupEmail(BasePageElement):
    """Signup modal 'email' field"""

    locator = (By.NAME, "email")


class FldHomeSignupFamilyRelations(BasePageElement):
    """Signup modal 'family relation' field"""

    locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[3]/form/div[5]/label')


class RadHomeFamilyRelationsFather(BasePageElement):
    """Signup modal family relation 'Father' option"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.userDetailsForm > form > div.inputContainer.checkboxList > div.checkBoxWrapper > ul > li:nth-child(1) > div > label",
    )


class FldHomeSignupGender(BasePageElement):
    """Signup modal 'gender' field"""

    locator = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[3]/form/div[5]/select')


class FldHomeSignupPhone(BasePageElement):
    """Signup modal 'phone' field"""

    locator = (By.NAME, "phone_number")


class BtnHomeSignupButton(BasePageElement):
    """Signup modal 'Submit' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.userDetailsForm > div.primaryButton.linerStyleButton",
    )


class BtnHomeLoginSubmitEmail(BasePageElement):
    """Login modal 'NEXT' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.login.loginWithMailWrapper > div.primaryButton.linerStyleButton",
    )


class BtnHomeSignupScrollTerms(BasePageElement):
    """Terms modal 'scroll down' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup.scrollMode > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.privacyAndTerms > div.scrollerDownWrapper > div",
    )


class BtnHomeSignupAcceptTerms(BasePageElement):
    """Terms modal 'Accept' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup.scrollMode > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.privacyAndTerms > div.footerActions > div",
    )


class BtnFormsChooseTrip(BasePageElement):
    """Registration forms 'Choose Trip' CTA"""

    locator = (By.CSS_SELECTOR, "button[data-qa-id='action-GetStarted-button']")


class ScnFormsTravelSeason(BasePageElement):
    """Registration forms 'Travel season' section"""

    locator = (By.CSS_SELECTOR, "section[data-v-78bcdfad]")
