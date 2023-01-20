import os
import csv
import logging
from pathlib import Path
from datetime import date

from selenium.webdriver.remote.webdriver import WebDriver


logger = logging.getLogger(__name__)


class Reporter:
    def __init__(self, driver: WebDriver, iso: str, name: str) -> None:

        logger.debug(f"Reporter.__init__ started: driver={driver} | iso={iso} | name={name}")

        self.test_driver = driver
        self.test_iso = iso
        self.test_name = name

        self.filepath = Path(__file__)

        self._create_files()

        logger.debug(f"Reporter.__init__: finished")

    def save_screenshot(self, stepN: int, step: str, ok=True):
        logger.debug(f"Reporter.save_screenshot started: stepN={stepN} | step={step} | ok={ok}")

        step = "-".join(step.split(" "))
        img_name = f"{stepN}-{step}"

        if not ok:
            img_name += "-fail"
        img_name += ".png"

        path = self.imagedir / img_name
        self.test_driver.save_screenshot(path)

        logger.debug(f"Reporter.save_screenshot: finished")

    def save_step(self, stepN: int, step: str, data: str = "", ok=True):
        logger.debug(f"Reporter.save_step started: stepN={stepN} | step={step} | data={data} | ok={ok}")

        with open(self.resultpath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                str(stepN),
                step,
                data,
                "pass" if ok else "fail"
            ])

        logger.debug(f"Reporter.save_step finished")

    def save_user(self, email: str):
        logger.debug(f"Reporter.save_user started: email={email}")

        now = date.today().strftime("%d-%m-%Y")
        with open(self.userspath, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([now, self.test_iso, email])
        
        logger.debug(f"Reporter.save_user finished")


    def write(self, stepN: int, step: str, data: str = "", ok=True):
        logger.debug(f"Reporter.write started: stepN={stepN} | step={step} | data={data} | ok={ok}")

        self.save_screenshot(stepN, step, ok)
        self.save_step(stepN, step, data, ok)

        logger.debug(f"Reporter.write finished")

    # Private methods
    def _create_reports_directory(self):
        logger.debug("Reporter._create_reports_directory started")

        if not self.filepath:
            raise Exception("missing filepath")
        
        self.basepath = self.filepath.parent.parent / "report"
        
        if not os.path.exists(self.basepath):
            os.mkdir(self.basepath)
            logger.info(f"Reporter._create_reports_directory created {self.basepath}")

        logger.debug("Reporter._create_reports_directory finished")

    def _create_results_directory(self):
        logger.debug("Reporter._create_results_directory started")

        if not self.basepath:
            raise Exception("missing basepath")

        self.resultdir = self.basepath / self.test_name

        if not os.path.exists(self.resultdir):
            os.mkdir(self.resultdir)
            logger.info(f"Reporter._create_results_directory created {self.resultdir}")

        logger.debug("Reporter._create_results_directory finished")


    def _create_screenshot_directory(self):
        logger.debug("Reporter._create_screenshot_directory started")

        if not self.resultdir:
            raise Exception("missing resultdir")

        self.imagedir = self.resultdir / "screenshots"
        
        if not os.path.exists(self.imagedir):
            os.mkdir(self.imagedir)
            logger.info(f"Reporter._create_screenshot_directory created {self.imagedir}")

        logger.debug("Reporter._create_screenshot_directory finished")

    def _create_results_file(self):
        logger.debug("Reporter._create_results_file started")

        if not self.resultdir:
            raise Exception("missing resultdir")
        
        self.resultpath = self.resultdir / "result.csv"
        with open(self.resultpath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Step #", "Action", "Data", "Status"])
            logger.info(f"Reporter._create_results_file created {self.resultpath}")

        logger.debug("Reporter._create_results_file finished")

    def _create_users_file(self):
        logger.debug("Reporter._create_users_file started")

        if not self.basepath:
            raise Exception("missing basepath")

        self.userspath = self.basepath / "test-users.csv"
        if not os.path.exists(self.userspath):
            with open(self.userspath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Country", "Email"])
            logger.info(f"Reporter._create_users_file created {self.userspath}")

        logger.debug("Reporter._create_users_file finished")

    def _create_files(self):
        logger.debug("Reporter._create_files started")

        self._create_reports_directory()
        self._create_results_directory()
        self._create_screenshot_directory()
        self._create_results_file()
        self._create_users_file()

        logger.debug("Reporter._create_files finished")
