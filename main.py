import logging
import unittest
from pathlib import Path

from src.suites import hp_signup_login


if __name__=="__main__":

    currpath = Path(__file__)
    logpath = currpath.parent / "test.log"

    logging.basicConfig(
        filemode="w",
        filename=logpath,
        level=logging.DEBUG
    )

    runner = unittest.runner.TextTestRunner()
    runner.run(hp_signup_login)