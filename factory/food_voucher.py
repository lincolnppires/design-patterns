# -*- coding: UTF-8 -*-

import random

from factory.voucher import Voucher

class Food_Voucher(Voucher):


    def code(self):
        return random.randint(10,20)


    def html_message(self):
        return '<html><body><h1>Food Voucher</h1></body></html>'