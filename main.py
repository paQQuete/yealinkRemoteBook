import os
from pathlib import Path

from dotenv import load_dotenv

from utils.context_manager import pysftp_conn_context
from core.extract import ExtractorSFTP
from core.transform import TransformDictToXML
from core.load import Savetofile

if __name__ == '__main__':
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    ASTERISK_HOST = os.getenv('ASTERISK_HOST')
    ASTERISK_USERNAME = os.getenv('ASTERISK_USERNAME')
    ASTERISK_PASSWORD = os.getenv('ASTERISK_PASSWORD')

    with pysftp_conn_context(host=ASTERISK_HOST, username=ASTERISK_USERNAME, password=ASTERISK_PASSWORD) as sftp:
        extractions = ExtractorSFTP(sftp)
        trasnform = TransformDictToXML(extractions.subs)
        print(len(trasnform.xmlout))
        print(type(trasnform.xmlout))
        print(trasnform.xmlout)
        Savetofile.write(filename='addressbook.xml', data=trasnform.xmlout)