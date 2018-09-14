# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class State(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def press_play(self, context):
        pass

    @abstractmethod
    def value(self):
        pass