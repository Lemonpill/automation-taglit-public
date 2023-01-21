from selenium.webdriver.common.by import By

from src.elements.base import BasePageElement


class CookiesAcceptButton(BasePageElement):
    """Homepage cookies CTA"""

    locator = (By.CSS_SELECTOR, "#app > div.toastWrapper > section > div.primaryButton")


class CloseLightboxButton(BasePageElement):
    """Home page lightbox 'X' icon"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.generalPopupWrapper.popup_container > div > div > span",
    )


class SignupTabButton(BasePageElement):
    """Login modal Signup tab button"""

    locator = (
        By.XPATH,
        '//*[@id="app"]/section[2]/div[2]/div/div[1]/div[1]',
    )


class LoginTabButton(BasePageElement):
    """Login modal Login tab button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > div > div.baseModalWrapper.baseModalPopup > div.authPanel.dynamicPanelsWrapper > div.contentContainerNew.login > div.signUp.primaryButton",
    )


class EmailSignupButton(BasePageElement):
    """Login modal 'Signup with email' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.signUp > div.signUp.primaryButton",
    )


class EmailLoginButton(BasePageElement):
    """Login modal 'Login with email' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.login > div.signUp.primaryButton",
    )


class LoginEmailField(BasePageElement):
    """Login modal 'email' field"""

    locator = (
        By.NAME,
        "email",
    )


class LoginOTPField(BasePageElement):
    """Login modal 'OTP' field"""

    locator = (By.ID, "digit_1")


class SignupFirstNameField(BasePageElement):
    """Signup modal 'first name' field"""

    locator = (By.NAME, "first_name")


class SignupLastNameField(BasePageElement):
    """Signup modal 'last name' field"""

    locator = (By.NAME, "last_name")


class SignupBirthDateField(BasePageElement):
    """Signup modal 'birth date' field"""

    locator = (By.NAME, "birth_date")


class SignupEmailField(BasePageElement):
    """Signup modal 'email' field"""

    locator = (By.NAME, "email")


class SignupFamilyRelField(BasePageElement):
    """Signup modal 'family relation' field"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.userDetailsForm > form > div.inputContainer.checkboxList",
    )


class SignupFatherOption(BasePageElement):
    """Signup modal family relation 'Father' option"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.userDetailsForm > form > div.inputContainer.checkboxList > div.checkBoxWrapper > ul > li:nth-child(1) > div > label",
    )


class SignupGenderSelection(BasePageElement):
    """Signup modal 'gender' field"""

    locator = (By.NAME, "gender")


class SignupPhoneField(BasePageElement):
    """Signup modal 'phone' field"""

    locator = (By.NAME, "phone_number")


class SignupSubmitButton(BasePageElement):
    """Signup modal 'Submit' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.userDetailsForm > div.primaryButton.linerStyleButton",
    )


class LoginSubmitButton(BasePageElement):
    """Login modal 'NEXT' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.login.loginWithMailWrapper > div.primaryButton.linerStyleButton",
    )


class ScrollDownTermsButton(BasePageElement):
    """Terms modal 'scroll down' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.privacyAndTerms > div.scrollerDownWrapper > div > i",
    )


class AcceptTermsButton(BasePageElement):
    """Terms modal 'Accept' button"""

    locator = (
        By.CSS_SELECTOR,
        "#app > section.loginSection.newStyleLogin > div.baseModalWrapper.baseModalPopup.scrollMode > div > div.contentContainerNew.privacyAndTerms > div.footerActions > div",
    )
