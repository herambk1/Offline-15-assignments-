import paramiko
import os


def download_file():

    HOST = 'eu-central-1.sftpcloud.io'
    USERNAME = 'a7bed7bc0c3d4d9dbdba7d2a3b5ea623'
    PASSWORD = 'N2QtwnucPMVRWF8s0B14hKXqGp1FTABG'
    PORT = 22

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy()
    )

    try:

        ssh.connect(
            HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD
        )

        print("SFTP connection successful")

        sftp = ssh.open_sftp()

        files = sftp.listdir(".")

        if not os.path.exists("source"):
            os.makedirs("source")

        for file in files:

            if file.endswith(".csv"):

                sftp.get(
                    file,
                    "source/" + file
                )

                print(file, "downloaded")

        sftp.close()

    except Exception as e:

        print("SFTP Error:", e)

        raise

    finally:

        ssh.close()