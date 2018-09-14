# -*- coding: UTF-8 -*-

import unittest

from decorator.basic_phone import Basic_Phone
from decorator.android_phone import Android_Phone
from decorator.iPhone import IPhone

class Test_Phone_Decorator(unittest.TestCase):

   def test_phone_decorator(self):
       basic_android = Basic_Phone(Android_Phone())
       basic_android.printModel()

       basic_iphone = Basic_Phone(IPhone())
       basic_iphone.printModel()

       basic_android_iphone = Basic_Phone(Android_Phone(IPhone()))
       basic_android_iphone.printModel()

       iphone_android_basic = IPhone(Android_Phone(Basic_Phone()))
       iphone_android_basic.printModel()

if __name__ == '__main__':
    unittest.main()