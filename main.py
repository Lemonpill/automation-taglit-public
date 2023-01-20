import logging
import unittest
from pathlib import Path

from src.suites import (
    # valid_hp_signup,
    # valid_hp_login,
    valid_hp_signup_login
)


"""
TODO:
    1. Add more logging
    2. Add webdriver folder in root
"""


if __name__ == "__main__":

    filepath = Path(__file__)
    logpath = filepath.parent / "test.log"

    logging.basicConfig(
        filemode="w",
        filename=logpath,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    runner = unittest.runner.TextTestRunner()
    runner.run(valid_hp_signup_login)
