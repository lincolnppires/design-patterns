# -*- coding: UTF-8 -*-

class Zoo(object):

    def __init__(self, observers=[]):
        self.__observers = observers
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

        for observe in self.__observers:
            observe(self.__animals[-1])
