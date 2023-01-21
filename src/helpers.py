import os
import time
import re
import csv

from lxml import html

from src.mailbox import Mailbox


def extract_otp(s):
    """Extract OTP from a string

    s:          string
    returns:    5 digit OTP code
    """

    r = re.compile(r"\d\d\d\d\d")
    otp = r.search(s)
    return otp.group()


def get_email_from_csv(path, iso):
    """Get test email from users file

    Args:
        path - path to .csv file
    Returns:
        email or None
    """

    if not os.path.exists(path):
        return None

    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["Country"] == iso:
                return r["Email"]


def extract_message_text(msg: dict):
    """Extract text content from Mailbox message

    Args:
        msg: message object
    Returns:
        str: message text
    """

    try:
        # Extract HTML from message
        tree = html.fromstring(msg["htmlBody"])
        # Extract text content from HTML
        return tree.text_content()
    except Exception:
        raise Exception("failed to extract text")
