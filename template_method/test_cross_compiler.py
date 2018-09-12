# -*- coding: UTF-8 -*-

import unittest

from template_method.iphone_compiler import IPhone_Compiler
from template_method.android_compiler import Android_Compiler

class Test_Cross_Compiler(unittest.TestCase):

    def test_cross_compiler(self):
        iphone = IPhone_Compiler()
        self.assertEqual('iphone', iphone.cross_compile())

        android = Android_Compiler()
        self.assertEqual('android', android.cross_compile())


if __name__ == '__main__':
    unittest.main()