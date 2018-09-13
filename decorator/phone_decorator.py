# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Phone_Decorator(object):
    __metaclass__ = ABCMeta


    def __init__(self, other_phone = None):
        self.__other_phone = other_phone


    def other_features(self):
        if(self.__other_phone is None):
            print('End')
        else:
            return self.__other_phone.printModel()

    @abstractmethod
    def printModel(self):
        pass


