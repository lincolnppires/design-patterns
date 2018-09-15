import random

from factory.voucher import Voucher

class Clothes_Voucher(Voucher):


    def code(self):
        return random.randint(1,10)


    def html_message(self):
        return '<html><body><h1>Clothes Voucher</h1></body></html>'