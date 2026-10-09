import os
import json
import paramiko

from utils.logger import get_logger
logger = get_logger()

def read_config():

    try:
        with open("utils/config.json", "r") as file:
            config = json.load(file)

        return config

    except Exception as e:

        logger.exception("Config file reading error")

        print("Config Error:", e)
        return None

def download_file():

    transport = None
    sftp = None

    try:
        config = read_config()

        if config is None:
            return None

        sftp_config = config["sftp"]

        host = sftp_config["host"]
        username = sftp_config["username"]
        password = sftp_config["password"]
        port = sftp_config["port"]
        file_name = sftp_config["file_name"]

        logger.info("Connecting to SFTP server")

        print("Connecting to SFTP server...")

        transport = paramiko.Transport((host, port))

        transport.connect(username=username,password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)

        logger.info("SFTP connection successful")

        print("SFTP connected successfully")

        # Create download folder automatically
        os.makedirs("download", exist_ok=True)

        remote_path = "/" + file_name
        local_path = "download/" + file_name

        # Check exact file
        try:

            sftp.stat(remote_path)

        except FileNotFoundError:

            logger.error("Required file not found: %s",file_name)

            print("Required file not found:",file_name)

            return None

        # Download exact file
        sftp.get(remote_path,local_path)

        logger.info("File downloaded successfully: %s",file_name)

        print("File downloaded successfully:",file_name)

        return local_path

    except Exception as e:

        logger.exception("SFTP error occurred")
        print("SFTP Error:", e)
        return None

    finally:

        if sftp:
            sftp.close()

        if transport:
            transport.close()

        logger.info("SFTP connection closed")