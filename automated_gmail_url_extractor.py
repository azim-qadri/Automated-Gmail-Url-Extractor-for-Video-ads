from googleapiclient.discovery import build
from google.oauth2 import service_account
import re

# email id
email_id = "roufiachesti123@gmail.com"

# credential file
credentials = service_account.Credentials.from_service_account_file(
    'client.json')

# Connect to the Gmail API
service = build('gmail', 'v1', credentials=credentials)

# Get the email message
result = service.users().messages().get(userId='me', id=email_id).execute()

# Get the content of the email message
email_content = result['payload']['body']['data']

# Use a regular expression to extract the link from the email content

link_regex = re.compile(r'(https?://[^\s]+)')
links = re.findall(link_regex, email_content)

# Return the extracted link
print(links[0])
