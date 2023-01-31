import unittest

from src.cases import *


loader = unittest.TestLoader()

# Load existing tests
valid_us_hp_signup = loader.loadTestsFromTestCase(USHomeSignupChrome)
valid_ca_hp_signup = loader.loadTestsFromTestCase(CAHomeSignupChrome)
valid_fr_hp_signup = loader.loadTestsFromTestCase(FRHomeSignupChrome)
valid_uk_hp_signup = loader.loadTestsFromTestCase(UKHomeSignupChrome)
valid_su_hp_signup = loader.loadTestsFromTestCase(SUHomeSignupChrome)
valid_de_hp_signup = loader.loadTestsFromTestCase(USHomeSignupChrome)
valid_ar_hp_signup = loader.loadTestsFromTestCase(ARHomeSignupChrome)

valid_us_hp_login = loader.loadTestsFromTestCase(USHomeLoginChrome)
valid_ca_hp_login = loader.loadTestsFromTestCase(CAHomeLoginChrome)
valid_fr_hp_login = loader.loadTestsFromTestCase(FRHomeLoginChrome)
valid_uk_hp_login = loader.loadTestsFromTestCase(UKHomeLoginChrome)
valid_su_hp_login = loader.loadTestsFromTestCase(SUHomeLoginChrome)
valid_de_hp_login = loader.loadTestsFromTestCase(USHomeLoginChrome)
valid_ar_hp_login = loader.loadTestsFromTestCase(ARHomeLoginChrome)

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
