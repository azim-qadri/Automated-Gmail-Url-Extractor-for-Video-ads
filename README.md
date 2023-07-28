# Automated Gmail Url Extractor for Video ads
Automated Python script to read Gmail emails, extract specific URLs from a designated sender, and open them in a web browser for video ad automation using Gmail API.
This program was created to automate the process of reading Gmail emails from a specific sender, extracting certain URLs from unread emails, and automatically opening these URLs in a web browser for a designated duration. The main purpose behind this automation is to earn money from video ad companies that send emails containing video ads. By visiting these links and watching the video for a specific duration, users can earn cash.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Important Note](#important-note)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Gmail URL Extractor is a Python script that utilizes the Gmail API to read emails from a specific sender such as:(no-reply@e.xyz.com) and find unread emails. It then extracts URLs from these emails and automatically opens each URL in a web browser. The script waits for 45 seconds on each webpage before moving on to the next URL. This automation process is intended to save time and effort when dealing with multiple video ad links sent through emails.

## Installation

Before running the script, ensure you have Python installed on your system. Additionally, you'll need to set up the necessary credentials to access the Gmail API. Follow the steps below to get started:

1. Clone this repository to your local machine or download the script directly from the GitHub repository.

2. Install the required Python libraries using pip:
   ```
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client beautifulsoup4
   ```

3. Set up credentials:
   - Create a project on the [Google Developer Console](https://console.developers.google.com/).
   - Enable the Gmail API for your project.
   - Create OAuth 2.0 credentials and download the JSON file.
   - Save the downloaded JSON file as `client.json` in the same directory as the script.

## Usage

To run the script, open a terminal or command prompt, navigate to the directory containing the script, and execute the following command:

```
python automated_gmail_url_extractor.py
```

The script will start running and will continue to open video ad URLs from unread emails until there are no more unread emails.

## How it Works

1. The script uses the Gmail API to access the user's Gmail account and authenticate the application using OAuth 2.0 credentials.

2. It looks for unread emails from the specified sender (no-reply@e.xyz.com) in the user's inbox.

3. Once an unread email is found, the script extracts the email's HTML content and decodes it to retrieve the URLs.

4. The first URL is opened in a web browser, and the script waits for 45 seconds before proceeding to the next URL.

5. The process is repeated for all unread emails with video ad links.

6. The script marks each processed email as read to avoid processing it again.

## Important Note

This script is intended for educational and personal use only. Using automated scripts to interact with emails or websites might violate the terms of service of certain platforms. Ensure you have the necessary permissions from the email sender and website owners before using this script.

## Contributing

Contributions to this project are welcome. If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes. However, be aware of the potential legal implications of using this script for automated interactions with emails and websites.
