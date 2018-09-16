# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Command_Base(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass