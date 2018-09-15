# -*- coding: UTF-8 -*-

import unittest

from factory.voucher_factory import Voucher_Factory

class Test_Voucher_Factory(unittest.TestCase):

    def test_voucher_factory(self):
        voucher = Voucher_Factory().create(20)
        print(voucher.html_message())

        voucher = Voucher_Factory().create(40)
        print(voucher.html_message())


if __name__ == '__main__':
    unittest.main()