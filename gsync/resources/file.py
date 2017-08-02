import os
from googleapiclient.http import MediaFileUpload
from datetime import datetime
def upload():
	file_path='/home/pawan/Desktop/google-drive/test1.txt'
	media_body = MediaFileUpload(filename=file_path, resumable=False)
	modified_epoch = os.path.getmtime(file_path)
	modified_time = datetime.utcfromtimestamp(modified_epoch).isoformat("T")+ "Z"
	path_segments = file_path.split(os.sep)
# construct upload kwargs
	create_kwargs = {
	    'body': {
	        'name': path_segments.pop(),
	        'modifiedTime': modified_time
	    },
	    'media_body': media_body,
	    'fields': 'id'
	}
	return create_kwargs