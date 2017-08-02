from __future__ import print_function
import os
from gsync.client import client
from gsync.resources.folder import get_folder
from gsync.resources.file import upload
import time

def main():
    drive_client = client()
    create_kwargs = upload()
    parent_id = get_folder()
    time.sleep(5)
    create_kwargs['body']['parents'] = [parent_id]
    file = drive_client.create(**create_kwargs).execute()
    print(create_kwargs)
    print("done")

if __name__ == '__main__':
    main()