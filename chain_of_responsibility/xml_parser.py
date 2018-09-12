# -*- coding: UTF-8 -*-

class XML_parser(object):

    def __init__(self, sucessor):
        self.__successor = sucessor


    def parse(self, file_name):
        if(file_name[-3:] == 'xml'):
            print('Parser XML')
            return True
        else:
            self.__successor.parse(file_name)
