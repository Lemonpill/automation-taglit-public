from datetime import datetime
from typing import List

import requests



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

        url = BASE_URL + f"?action=getDomainList"

        try:
            res = requests.get(url)
        except Exception:
            raise Exception("failed to fetch")

        try:
            data = res.json()
        except Exception:
            raise Exception("failed to decode json")

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

        return data


    def get_attachment(self):
        """ Attachment download """

        raise NotImplementedError


class Mailbox(object):
    def __init__(self, email=None) -> None:
        if not email:
            email = "qa-" + API.generate_addresses(1)[0]

        self.email = email
        
        self.refresh_messages()

    def refresh_messages(self) -> None:
        """ Refreshes current messages
        """

        self.messages = API.get_mailbox(self.email)
        self.last_refresh = datetime.now()

    def get_all_messages(self) -> List[dict]:
        """ Returns all messages

            returns:    list of messages
        """

        return self.messages

    def get_single_message(self, msg_id) -> dict:
        """ Returns single message by ID

            msg_id:     message ID
            returns:    message object
        """

        return API.get_message(self.email, msg_id)

    def get_last_message(self) -> (dict|None):
        """ Returns last received message

            returns:    message object or None
        """

        if not self.messages:
            return None
        
        last_id = self.messages[0]["id"]

        return API.get_message(self.email, last_id)

    def has_new_messages(self) -> bool:
        """ Returns whether new messages
            were receved

            returns:    bool
        """

        # Copy old messages
        old_messages = self.get_all_messages()[:]
        print(f'old: {old_messages}')

        # Refresh messages
        self.refresh_messages()

        # Copy new messages
        new_messages = self.get_all_messages()[:]
        print(f'new: {new_messages}')

        # Compare the length of both
        if len(old_messages) != len(new_messages):
            # Return True if lengths differ
            print("got new messages")
            return True

        # Otherwise return False
        print("got no new messages")
        return False
