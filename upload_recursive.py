from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import os
import sys

authcookie = Office365('https://yourcompany.atsharepoint.com', username='user@yourcompany.org', password='youpassword').GetCookies()
site = Site('https://yourcompany.atsharepoint.com/sites/Your-Sites', version=Version.v2019, authcookie=authcookie) # set the version if necessary

for root, subdirs, files in os.walk('/path/to/root/dir'):
    dest_folder = root.split('/path/to/root')[1] # this will get directory after /path/to/dir and its subdir
    folder = site.Folder('Shared Document/your_dir_ifany/%s' %dest_folder) # this set destination directory or will create directory in sharepoint if doesn't exist
    for fname in files:
        fullfname = os.path.join(root, fname) # get the full path of source file
        with open(fullfname, mode='rb') as file: # read the file in binary
            fileContent = file.read() 
        folder.upload_file(fileContent, fname) # upload the file