from gsync.client import client

def create_folder():
	parent_id = ''
	drive_client = client()
# construct query and creation arguments
	folder_kwargs = {
	    'body': {
	        'name': 'google-drive1',
	        'mimeType' : 'application/vnd.google-apps.folder'
	    },
	    'fields': 'id'
	}

	response = drive_client.create(**folder_kwargs).execute()
	parent_id = response.get('id')
	return parent_id

def get_folder():
	folder_name = 'google-drive1'
	parent_id = ''
	drive_client = client()
	query_kwargs = {
	    'spaces': 'drive',
	    'fields': 'files(id, parents)'
	}
# search for folder id in existing hierarchy
	walk_query = "name = '%s'" % folder_name
	if parent_id:
		walk_query += "and '%s' in parents" % parent_id
	query_kwargs['q'] = walk_query
	response = drive_client.list(**query_kwargs).execute()
	file_list = response.get('files', [])

	if file_list:
	    parent_id = file_list[0].get('id')
	    print("exists")
	else:
		parent_id = create_folder()
	return parent_id
