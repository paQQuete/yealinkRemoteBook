from typing import Tuple

import xml.etree.ElementTree as ET


class TransformDictToXML():
    def __init__(self, data: dict):
        self.__rawdata = data
        self.__rootel, self.__titleel, self.__menuel = self._structure_init()
        self._transform()
        self.__rootel = self._cooking_root()

    def _structure_init(self) -> Tuple[ET.Element, ET.Element, ET.Element]:
        root = ET.Element('YealinkIPPhoneBook')
        title = ET.SubElement(root, 'Title')
        title.text = 'Yealink'
        menu = ET.SubElement(root, 'Menu')
        menu.set('Name', 'Телефонная книга Medimcom')
        return root, title, menu

    def _transform(self) -> dict:
        subobjects = dict()
        for caller_number, name in self.__rawdata.items():
            subobjects.update({caller_number: ET.SubElement(self.__rootel, 'Unit')})
            subobjects[caller_number].set('Name', name)
            subobjects[caller_number].set('Phone1', caller_number)
            subobjects[caller_number].set('Phone2', '')
            subobjects[caller_number].set('Phone3', '')
            subobjects[caller_number].set('default_photo', 'Resource:')
        return subobjects

    def _cooking_root(self):
        return ET.tostring(self.__rootel, 'utf-8')

    @property
    def xmlout(self):
        return self.__rootel
