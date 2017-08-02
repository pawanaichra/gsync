from gsync.credentials import get_credentials
import httplib2
from apiclient import discovery

def client():
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('drive', 'v3', http=http)
	drive_client = service.files()
	return drive_client