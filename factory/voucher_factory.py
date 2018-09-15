# -*- coding: UTF-8 -*-

from factory.food_voucher import Food_Voucher
from factory.clothes_voucher import Clothes_Voucher

class Voucher_Factory(object):

    def create(self, discountPoints):
        if discountPoints <= 0:
            raise Exception('Invalid number of discount points!')

        if discountPoints < 30:
            return Food_Voucher()
        else:
            return Clothes_Voucher()