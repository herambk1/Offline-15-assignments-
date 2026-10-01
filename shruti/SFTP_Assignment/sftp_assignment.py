import pysftp
# Define server credentials
HOST = 'eu-central-1.sftpcloud.io'
USERNAME = 'e21f08afd17c4060a4fb26a0eb9b128c'
PASSWORD = 'sdo3514pzswQqPsuwYx9XzOlCmuCLJc6'
port = 22
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

#put_local = r"C:\Users\Devendra Otari\OneDrive\Documents\sample22.txt"
#on_remote = "sample22.txt"

from_remote = "sample22.txt"
get_on_local = "sample22.txt"

# Establish connection
with pysftp.Connection(HOST, username=USERNAME, password=PASSWORD, cnopts=cnopts) as sftp:
    print("Connection successfully established!")
    directory_structure = sftp.listdir()
    print("Files on server:", directory_structure)
    #sftp.put(put_local, on_remote)
    #print("File uploaded successfully!")
    sftp.get(from_remote, get_on_local)
    print("File downloaded successfully!")



