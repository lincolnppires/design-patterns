# -*- coding: UTF-8 -*-

import unittest

from factory.voucher_factory import Voucher_Factory

class Test_Voucher_Factory(unittest.TestCase):

    def test_voucher_factory(self):
        voucher = Voucher_Factory().create(20)
        msg = voucher.html_message()
        self.assertTrue('Food Voucher' in msg)

        voucher = Voucher_Factory().create(40)
        msg = voucher.html_message()
        self.assertTrue('Clothes Voucher' in msg)


if __name__ == '__main__':
    unittest.main()