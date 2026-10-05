import paramiko

# Define server credentials
HOST = 'eu-central-1.sftpcloud.io'
USERNAME = '0dae5b69530e4258a1fdfdba694e4416'
PASSWORD = 'FmRLa0qS4gbqFEyeDCdXyyejcrJFer8M'  # Or use private_key='/path/to/key'
PORT = 22

# Create an SSH client instance
ssh = paramiko.SSHClient()

# Automatically add unknown host keys (Testing / Dev environment ONLY)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD)

    # Open an SFTP session
    sftp = ssh.open_sftp()
    print("Paramiko SFTP connection established!")

    # Perform file operations

    files = sftp.listdir(".")

    for file in files:
        if file.endswith('.pdf'):
            sftp.get("{}".format(file), 'source/{}'.format(file))
    # Close SFTP session
    sftp.close()

finally:
    # Always close the core SSH connection
    ssh.close()
