# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

class Cross_Compile_Template(object):

    __metaclass__ = ABCMeta

    def cross_compile(self):
        self.collect_source()
        return self.compile_to_target()


    @abstractmethod
    def collect_source(self):
        pass


    @abstractmethod
    def compile_to_target(self):
        pass
