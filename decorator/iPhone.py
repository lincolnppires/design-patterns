# -*- coding: UTF-8 -*-

from decorator.phone_decorator import Phone_Decorator

class IPhone(Phone_Decorator):

    def printModel(self):
        print('Adding Features of Iphone')
        super(IPhone, self).other_features()