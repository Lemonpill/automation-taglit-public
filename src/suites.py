import unittest

from src.cases import *


loader = unittest.TestLoader()

# Load existing tests
valid_us_hp_signup = loader.loadTestsFromTestCase(SignupHomepageUnitedStates)
valid_ca_hp_signup = loader.loadTestsFromTestCase(SignupHomepageCanada)
valid_fr_hp_signup = loader.loadTestsFromTestCase(SignupHomepageFrance)
valid_uk_hp_signup = loader.loadTestsFromTestCase(SignupHomepageUnitedKingdom)
valid_su_hp_signup = loader.loadTestsFromTestCase(SignupHomepageRussia)
valid_de_hp_signup = loader.loadTestsFromTestCase(SignupHomepageGermany)
valid_ar_hp_signup = loader.loadTestsFromTestCase(SignupHomepageArgentina)

valid_us_hp_login = loader.loadTestsFromTestCase(LoginHomepageUnitedStates)
valid_ca_hp_login = loader.loadTestsFromTestCase(LoginHomepageCanada)
valid_fr_hp_login = loader.loadTestsFromTestCase(LoginHomepageFrance)
valid_uk_hp_login = loader.loadTestsFromTestCase(LoginHomepageUnitedKingdom)
valid_su_hp_login = loader.loadTestsFromTestCase(LoginHomepageRussia)
valid_de_hp_login = loader.loadTestsFromTestCase(LoginHomepageGermany)
valid_ar_hp_login = loader.loadTestsFromTestCase(LoginHomepageArgentina)

# Valid signup from homepage test suite
# * Populates reports/test-users.csv
valid_hp_signup = unittest.TestSuite(
    [
        valid_us_hp_signup,
        valid_ca_hp_signup,
        valid_fr_hp_signup,
        valid_uk_hp_signup,
        valid_su_hp_signup,
        valid_de_hp_signup,
        valid_ar_hp_signup,
    ]
)

# Valid login from homepage test suite
# * This requires users in reports/test-users.csv
valid_hp_login = unittest.TestSuite(
    [
        valid_us_hp_login,
        valid_ca_hp_login,
        valid_fr_hp_login,
        valid_uk_hp_login,
        valid_su_hp_login,
        valid_de_hp_login,
        valid_ar_hp_login,
    ]
)

# Signup and login from homepage suite
valid_hp_signup_login = unittest.TestSuite(
    [
        valid_us_hp_signup,
        valid_us_hp_login,
        valid_ca_hp_signup,
        valid_ca_hp_login,
        valid_fr_hp_signup,
        valid_fr_hp_login,
        valid_uk_hp_signup,
        valid_uk_hp_login,
        valid_su_hp_signup,
        valid_su_hp_login,
        valid_de_hp_signup,
        valid_de_hp_login,
        valid_ar_hp_signup,
        valid_ar_hp_login,
    ]
)
