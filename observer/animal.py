# -*- coding: UTF-8 -*-

class Animal(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    