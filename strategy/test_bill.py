# -*- coding: UTF-8 -*-

import unittest

from strategy.bill import Bill
from strategy.cash import Cash
from strategy.credit_card import Credit_Card
from strategy.debit_card import Debit_Card


class Test_Bill(unittest.TestCase):

    def test_payment(self):
        bill = Bill(500)
        self.assertEqual(450, bill.payment(Cash()))
        self.assertEqual(500, bill.payment(Debit_Card()))
        self.assertEqual(550, bill.payment(Credit_Card()))


if __name__ == '__main__':
    unittest.main()