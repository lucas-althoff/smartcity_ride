from __future__ import print_function
from googleapiclient.http import MediaFileUpload


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']


class FormUploader:

    def __init__(self):
        self.service = None

    def create_service(self):
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('./backend/src/servicos/token.json'):
            creds = Credentials.from_authorized_user_file('./backend/src/servicos/token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    './google/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('drive', 'v3', credentials=creds)
            print('OK')
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')

    def upload_file(self, file_name, file_path):
        if not self.service:
            self.create_service()
        file_metadata = {
            'name': file_name
        }

        media_content = MediaFileUpload(f'{file_path}/{file_name}', mimetype='text/plain'
        )
        existing_files = {'nivel_componente_municipio.csv': '1EunYyGhmD35kU3Pm8v-BfZca_GVfFl1U'}
        if file_name in existing_files.keys():
            file = self.service.files().update(
                body=file_metadata,
                media_body=media_content,
                supportsAllDrives=True,
                fileId=existing_files.get(file_name)
            ).execute()
        else:
            file = self.service.files().create(
                body=file_metadata,
                media_body=media_content,
                supportsAllDrives=True
            ).execute()


if __name__ == '__main__':
    up = FormUploader()
    up.upload_file('test.csv')
