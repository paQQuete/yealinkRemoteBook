import os
from pathlib import Path
import time

from dotenv import load_dotenv

from utils.context_manager import pysftp_conn_context
from utils.logger import logger
from core.extract import ExtractorSFTP
from core.transform import TransformDictToXML
from core.load import Savetofile

LOCAL_DEBUG = False
if LOCAL_DEBUG:
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

ASTERISK_HOST = os.getenv('ASTERISK_HOST')
ASTERISK_USERNAME = os.getenv('ASTERISK_USERNAME')
ASTERISK_PASSWORD = os.getenv('ASTERISK_PASSWORD')
LOOP_TIMEOUT = int(os.environ.get('LOOP_TIMEOUT'))

if __name__ == '__main__':
    while True:
        with pysftp_conn_context(host=ASTERISK_HOST, username=ASTERISK_USERNAME, password=ASTERISK_PASSWORD) as sftp:
            extractions = ExtractorSFTP(sftp)
            logger.info(f"Extraction from {ASTERISK_HOST} completed")

            transform = TransformDictToXML(extractions.subs)
            logger.info(f"Transform data to XML completed")

            Savetofile.write(filename='addressbook.xml', data=transform.xmlout)
            # TODO: logger 'xml upload to .. here'

            logger.info(
                f"Next sync attempt in {LOOP_TIMEOUT} seconds ({LOOP_TIMEOUT / 60} minutes, {LOOP_TIMEOUT / 3600}).")
            time.sleep(LOOP_TIMEOUT)
