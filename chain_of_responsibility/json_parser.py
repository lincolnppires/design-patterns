# -*- coding: UTF-8 -*-

class Json_parser(object):

    def __init__(self, successor):
        self.__successor = successor


    def parse(self, file_name):
        if(file_name[-4:] == 'json'):
            print('Parser Json')
            return True
        else:
            return self.__successor.parse(file_name)