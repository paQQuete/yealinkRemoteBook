import re

import pysftp


class Extractor:
    '''
    Класс для чтения и парсинга файла sip.conf
    :param sftp: объект класса pystfp.Connection с готовым соединением
    '''

    def __init__(self, sftp: pysftp.Connection):
        self.__sftp = sftp
        self.__sipconf_path = '/etc/asterisk/sip.conf'
        self._get_sipconf()
        self.__sipconf_obj = self._read_sipconf()
        self.__subs = self._take_callers()

    def _get_sipconf(self) -> None:
        self.__sftp.get(self.__sipconf_path, 'sip.conf')

    def _read_sipconf(self) -> str:
        ''' Функция через контекстный менеджер открывает sip.conf по заданному пути,
        возвращает прочитанный файл в строке, закрывает файл '''
        with open('sip.conf', mode='r') as conffile:
            return conffile.read()

    def _take_callers(self) -> dict:
        ''' Функция формирует словарь вида
        {номер телефона (строка): имя (строка, из параметра sip конфига callerid} '''
        raw = re.findall(r'''callerid=.*''', self.__sipconf_obj)
        output = dict()
        for each in raw:
            each = each.split('"')
            name = each[1]
            caller_number = re.search(r'\d{3}', each[2]).group()
            output.update({caller_number: name})
        return output

    @property
    def subs(self):
        return self.__subs
