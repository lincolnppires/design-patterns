# -*- coding: UTF-8 -*-

class Text_parser(object):

    def __init__(self, sucessor):
        self.__successor = sucessor


    def parse(self, file_name):
        if(file_name[-3:] == 'txt'):
            print('Parser txt')
            return True
        else:
            return self.__successor.parse(file_name)
