import os.path
import os
import time
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
import base64
import webbrowser

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.labels']


def mark_email_as_read(service, message):
    post_data = {
        "removeLabelIds": [
            "UNREAD"
        ]
    }
    service.users().messages().modify(userId='me', id=message, body=post_data).execute()


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        get_msg = service.users().messages().list(userId='me', labelIds=['INBOX'],
                                                  q="from:[emailId] is:unread", maxResults=1).execute() #Email id of sender without []
        messages = get_msg.get('messages', [])
        if not messages:
            print('no new msgs')
        else:
            msg_id = get_msg['messages'][0]['id']
            print(msg_id)
            mark_email_as_read(service, msg_id)
            # Get the email message
            result = service.users().messages().get(userId='me', id=msg_id).execute()
            payload = result['payload']
            data = payload['body']['data']
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data)
            soup = BeautifulSoup(decoded_data, "lxml")
            body = str(soup.body())
            print(body)
            url = re.findall('http[s]?://e2(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
            # open link
            webbrowser.open(url[0])
            time.sleep(45)
            main()
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
