import os
import csv
import logging
from pathlib import Path
from datetime import date

from selenium.webdriver.remote.webdriver import WebDriver


class Reporter:
    def __init__(self, driver: WebDriver, iso: str, name: str) -> None:
        self.test_driver = driver
        self.test_iso = iso
        self.test_name = name

        filepath = Path(__file__)

        # Creating base report path
        self.basepath = filepath.parent.parent / "report"
        if not os.path.exists(self.basepath):
            os.mkdir(self.basepath)

        # Creating test result directory
        self.resultdir = self.basepath / self.test_name
        if not os.path.exists(self.resultdir):
            os.mkdir(self.resultdir)

        # Creating screenshots directory
        self.imagedir = self.resultdir / "screenshots"
        if not os.path.exists(self.imagedir):
            os.mkdir(self.imagedir)

        # Creating results directory
        self.resultpath = self.resultdir / "result.csv"
        with open(self.resultpath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Step #", "Action", "Data", "Status"])

        # Creating users file
        self.userspath = self.basepath / "test-users.csv"
        if not os.path.exists(self.userspath):
            with open(self.userspath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Country", "Email"])


    def save_screenshot(self, stepN: int, step: str, ok=True):
        logging.debug(f"Reporter: save screenshot: stepN={stepN} step={step} ok={ok}")

        step = "-".join(step.split(" "))
        img_name = f"{stepN}-{step}"

        if not ok:
            img_name += "-fail"
        img_name += ".png"

        path = self.imagedir / img_name
        self.test_driver.save_screenshot(path)

        logging.debug("Reporter: save screenshot: success")

    def save_step(self, stepN: int, step: str, data: str = "", ok=True):
        logging.debug(f"save step: stepN={stepN} step={step} data={data} ok={ok}")

        with open(self.resultpath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                str(stepN),
                step,
                data,
                "pass" if ok else "fail"
            ])

        logging.debug(f"Reporter: save step: success")

    def save_user(self, email: str):
        logging.debug(f"save user: email={email}")

        now = date.today().strftime("%d-%m-%Y")
        with open(self.userspath, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([now, self.test_iso, email])

        logging.debug(f"Reporter: save user: success")

    def write(self, stepN: int, step: str, data: str = "", ok=True):
        logging.debug(f"Reporter: write: stepN={stepN} step={step} data={data} ok={ok}")

        self.save_screenshot(stepN, step, ok)
        self.save_step(stepN, step, data, ok)

        logging.debug(f"Reporter: write: success")
