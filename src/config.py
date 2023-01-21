from pathlib import Path


class Config:
    """Configuration settings"""

    filedir = Path(__file__)
    DRIVERS_PATH = filedir.parent.parent / "drivers"
    REPORTS_PATH = filedir.parent.parent / "reports"

    ANIMATION_DELAY = 1
    ENVIRONMENT = "PROD"
    LOCATE_TIMEOUT = 30

    CHROMEDRIVER_PATH = DRIVERS_PATH / "chromedriver.exe"