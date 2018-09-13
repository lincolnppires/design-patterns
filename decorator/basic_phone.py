# -*- coding: UTF-8 -*-

from decorator.phone_decorator import Phone_Decorator

class Basic_Phone(Phone_Decorator):

    def printModel(self):
        print('Basic Phone')
        super(Basic_Phone, self).other_features()