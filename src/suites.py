import unittest

from src.cases.signup import (
    us_hp_signup,
    ca_hp_signup,
    fr_hp_signup,
    uk_hp_signup,
    su_hp_signup,
    de_hp_signup,
    ar_hp_signup
)
from src.cases.login import (
    us_hp_login,
    ca_hp_login,
    fr_hp_login,
    uk_hp_login,
    su_hp_login,
    de_hp_login,
    ar_hp_login
)


loader = unittest.TestLoader()

hp_signup = unittest.TestSuite([
    loader.loadTestsFromModule(us_hp_signup),
    loader.loadTestsFromModule(ca_hp_signup),
    loader.loadTestsFromModule(fr_hp_signup),
    loader.loadTestsFromModule(uk_hp_signup),
    loader.loadTestsFromModule(su_hp_signup),
    loader.loadTestsFromModule(de_hp_signup),
    loader.loadTestsFromModule(ar_hp_signup),
])

hp_login = unittest.TestSuite([
    loader.loadTestsFromModule(us_hp_login),
    loader.loadTestsFromModule(ca_hp_login),
    loader.loadTestsFromModule(fr_hp_login),
    loader.loadTestsFromModule(uk_hp_login),
    loader.loadTestsFromModule(su_hp_login),
    loader.loadTestsFromModule(de_hp_login),
    loader.loadTestsFromModule(ar_hp_login),
])

hp_signup_login = unittest.TestSuite([
    loader.loadTestsFromModule(us_hp_signup),
    loader.loadTestsFromModule(us_hp_login),
    loader.loadTestsFromModule(ca_hp_signup),
    loader.loadTestsFromModule(ca_hp_login),
    loader.loadTestsFromModule(fr_hp_signup),
    loader.loadTestsFromModule(fr_hp_login),
    loader.loadTestsFromModule(uk_hp_signup),
    loader.loadTestsFromModule(uk_hp_login),
    loader.loadTestsFromModule(su_hp_signup),
    loader.loadTestsFromModule(su_hp_login),
    loader.loadTestsFromModule(de_hp_signup),
    loader.loadTestsFromModule(de_hp_login),
    loader.loadTestsFromModule(ar_hp_signup),
    loader.loadTestsFromModule(ar_hp_login),
])