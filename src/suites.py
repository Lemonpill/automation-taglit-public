import unittest

from src.cases.signup import (
    us_hp_signup,
    us_lp_signup,
    ca_hp_signup,
    fr_hp_signup,
    uk_hp_signup,
    su_hp_signup,
    de_hp_signup,
    ar_hp_signup,
)
from src.cases.login import (
    us_hp_login,
    us_lp_login,
    ca_hp_login,
    fr_hp_login,
    uk_hp_login,
    su_hp_login,
    de_hp_login,
    ar_hp_login,
)


loader = unittest.TestLoader()

# Load existing tests
valid_us_hp_signup = loader.loadTestsFromModule(us_hp_signup)
valid_us_lp_signup = loader.loadTestsFromModule(us_lp_signup)
valid_ca_hp_signup = loader.loadTestsFromModule(ca_hp_signup)
valid_fr_hp_signup = loader.loadTestsFromModule(fr_hp_signup)
valid_uk_hp_signup = loader.loadTestsFromModule(uk_hp_signup)
valid_su_hp_signup = loader.loadTestsFromModule(su_hp_signup)
valid_de_hp_signup = loader.loadTestsFromModule(de_hp_signup)
valid_ar_hp_signup = loader.loadTestsFromModule(ar_hp_signup)

valid_us_hp_login = loader.loadTestsFromModule(us_hp_login)
valid_us_lp_login = loader.loadTestsFromModule(us_lp_login)
valid_ca_hp_login = loader.loadTestsFromModule(ca_hp_login)
valid_fr_hp_login = loader.loadTestsFromModule(fr_hp_login)
valid_uk_hp_login = loader.loadTestsFromModule(uk_hp_login)
valid_su_hp_login = loader.loadTestsFromModule(su_hp_login)
valid_de_hp_login = loader.loadTestsFromModule(de_hp_login)
valid_ar_hp_login = loader.loadTestsFromModule(ar_hp_login)

# Valid signup from homepage test suite
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

# Valid signup from login page test suite
valid_lp_signup = unittest.TestSuite(
    [
        valid_us_lp_signup,
    ]
)

# Valid login from login page test suite
valid_lp_login = unittest.TestSuite(
    [
        valid_us_lp_login,
    ]
)

# Valid login from homepage test suite
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

# Signup and login from homepage
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

# Signup and login from login page
valid_lp_signup_login = unittest.TestSuite(
    [
        valid_us_lp_signup,
        valid_us_lp_login,
    ]
)
