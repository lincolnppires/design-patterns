# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Voucher(object):

    __metaclass__ = ABCMeta


    @abstractmethod
    def code(self):
        pass

    @abstractmethod
    def html_message(self):
        pass