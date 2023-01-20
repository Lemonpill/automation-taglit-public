import logging
from datetime import datetime
from typing import List

import requests


logger = logging.getLogger(__name__)

BASE_URL = "https://www.1secmail.com/api/v1/"


class API:
    def generate_addresses(n: str) -> List[str]:
        """ Generating random email addresses

            n:          number of addresses to generate
            returns:    a list of addresses

            example:
                [
                    "514adm2s0c@wwjmp.com",
                    "9q6fv8wkwr4@wwjmp.com",
                    "xi9pw5ry@1secmail.com",
                    "xpni3u25w@1secmail.net",
                    "pkbds55jep@1secmail.com",
                    "jeil65xzv8@1secmail.org",
                    "cg89o9i0thml@1secmail.net",
                    "0tw2rcoc3id@1secmail.org",
                    "bdnlnm@1secmail.org",
                    "p8axfdpf65@wwjmp.com"
                ]
        """

        logger.debug(f"API.generate_addresses started: n={n}")

        if not type(n) == int:
            raise Exception("n must be an integer")

        url = BASE_URL + f"?action=genRandomMailbox&count={n}"

        try:
            res = requests.get(url)
        except Exception:
            raise Exception("failed to fetch")

        try:
            data = res.json()
        except Exception:
            raise Exception("failed to decode json")

        logger.debug(f"API.generate_addresses finished")
        
        return data

    def get_domain_list(self) -> List[str]:
        """ List active domains

            returns:    a list of domains
            
            example:
                [
                    "1secmail.com",
                    "1secmail.org",
                    "1secmail.net",
                    "wwjmp.com",
                    "esiix.com",
                    "xojxe.com",
                    "yoggm.com"
                ]
        """

        logger.debug(f"API.get_domain_list started")

        url = BASE_URL + f"?action=getDomainList"

        try:
            res = requests.get(url)
        except Exception:
            raise Exception("failed to fetch")

        try:
            data = res.json()
        except Exception:
            raise Exception("failed to decode json")

        logger.debug(f"API.get_domain_list finished: data={data}")

        return data

    def get_mailbox(e: str) -> List[dict]:
        """ Checking your mailbox

            e:          email address
            returns:    a list of emails
            
            example:
                [{
                    "id": 639,
                    "from": "someone@example.com",
                    "subject": "Some subject",
                    "date": "2018-06-08 14:33:55"
                }, {
                    "id": 640,
                    "from": "someoneelse@example.com",
                    "subject": "Other subject",
                    "date": "2018-06-08 14:40:55"
                }]
        """

        logger.debug(f"API.get_mailbox started: e={e}")

        try:
            login, domain = e.split("@")
        except ValueError:
            raise Exception("valid email required")
        
        url = BASE_URL + f"?action=getMessages&login={login}&domain={domain}"

        try:
            res = requests.get(url)
        except Exception:
            raise Exception("failed to fetch")

        try:
            data = res.json()
        except Exception:
            raise Exception("failed to decode json")

        logger.debug(f"API.get_mailbox finished: data={data}")
        
        return data

    def get_message(e: str, msg_id: int) -> dict:
        """ Fetching single message

            e:          email address
            msg_id:     inbox message id
            returns:    message data
            
            example:
                {
                    "id": 639,
                    "from": "someone@example.com",
                    "subject": "Some subject",
                    "date": "2018-06-08 14:33:55",
                    "attachments": [{
                        "filename": "iometer.pdf",
                        "contentType": "application\/pdf",
                        "size": 47412
                    }],
                    "body": "Some message body\n\n",
                    "textBody": "Some message body\n\n",
                    "htmlBody": ""
                }
        """

        logger.debug(f"API.get_message started: e={e} msg_id={msg_id}")

        try:
            login, domain = e.split("@")
        except ValueError:
            raise Exception("valid email required")

        if not type(msg_id) == int:
            raise Exception("n must be an integer")
        
        url = BASE_URL + f"?action=readMessage&login={login}&domain={domain}&id={msg_id}"

        try:
            res = requests.get(url)
        except Exception:
            raise Exception("failed to fetch")

        try:
            data = res.json()
        except Exception:
            raise Exception("failed to decode json")

        logger.debug(f"API.get_message finished: data={data}")

        return data


    def get_attachment(self):
        """ Attachment download """

        raise NotImplementedError


class Mailbox(object):
    def __init__(self, email=None) -> None:

        logger.debug(f"Mailbox.__init__ started: email={email}")

        if not email:
            email = "qa-" + API.generate_addresses(1)[0]
        self.email = email

        self.refresh_messages()

        logger.debug("Mailbox.__init__ finished")

    def refresh_messages(self) -> None:
        """ Refreshes current messages
        """
        
        logger.debug("Mailbox.refresh_messages started")

        self.messages = API.get_mailbox(self.email)
        self.last_refresh = datetime.now()

        logger.debug("Mailbox.refresh_messages finished")

    def get_all_messages(self) -> List[dict]:

        """ Returns all messages

            returns:    list of messages
        """

        logger.debug("Mailbox.refresh_messages started")

        messages = self.messages

        logger.debug(f"Mailbox.refresh_messages finished: messages={messages}")

        return messages

    def get_single_message(self, msg_id) -> dict:
        """ Returns single message by ID

            msg_id:     message ID
            returns:    message object
        """

        logger.debug(f"Mailbox.get_single_message started: msg_id={msg_id}")

        message = API.get_message(self.email, msg_id)

        logger.debug(f"Mailbox.get_single_message finished: message={message}")

        return message

    def get_last_message(self) -> (dict|None):
        """ Returns last received message

            returns:    message object or None
        """

        logger.debug(f"Mailbox.get_last_message started")

        if not self.messages:
            return None
        
        last_id = self.messages[0]["id"]

        message = API.get_message(self.email, last_id)

        logger.debug(f"Mailbox.get_last_message finished: message={message}")

        return message

    def has_new_messages(self) -> bool:
        """ Returns whether new messages
            were receved

            returns:    bool
        """

        logger.debug(f"Mailbox.has_new_messages started")

        # Copy old messages
        old_messages = self.get_all_messages()[:]

        # Refresh messages
        self.refresh_messages()

        # Copy new messages
        new_messages = self.get_all_messages()[:]
        has_new_messages = False

        # Compare the length of both
        if len(new_messages) > len(old_messages):
            # Return True if lengths differ
            has_new_messages = True

        logger.debug(f"Mailbox.has_new_messages finished: has_new_messages={has_new_messages}")

        # Otherwise return False
        return has_new_messages
