# -*- coding: UTF-8 -*-

class Bill(object):


    def __init__(self, value):
        self.__value = value


    @property
    def value(self):
        return self.__value


    def payment(self, type):
        return type.pay(self.value)