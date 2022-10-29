from contextlib import contextmanager

import pysftp
from pysftp.exceptions import ConnectionException

from utils.logger import logger
from utils.backoff import backoff

@contextmanager
def pysftp_conn_context(host: str, username: str, password: str, cnopts):
    """Контекстный менеджер для подключения по SFTP к Asterisk"""

    @backoff(ConnectionException, message="Asterisk server connection error")
    def connect(host, username, password, cnopts):
        sftp = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)
        logger.info(f'SFTP connection to {host} created')
        return sftp

    sftp = connect(host, username, password, cnopts)
    try:
        yield sftp
    finally:
        sftp.close()
        logger.info(f'SFTP connection to {host} closed')