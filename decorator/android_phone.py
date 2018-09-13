# -*- coding: UTF-8 -*-

from decorator.phone_decorator import Phone_Decorator

class Android_Phone(Phone_Decorator):

    def printModel(self):
        print('Adding Features of Android')
        super(Android_Phone, self).other_features()

