import logging
import unittest
from pathlib import Path

from src.suites import hp_signup_login


"""
TODO:
1. Change verify forms in CA
2. Add more logging
"""


if __name__ == "__main__":

    currpath = Path(__file__)
    logpath = currpath.parent / "test.log"

    logging.basicConfig(
        filemode="w",
        filename=logpath,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    runner = unittest.runner.TextTestRunner()
    runner.run(hp_signup_login)
