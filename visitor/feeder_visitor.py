# -*- coding: UTF-8 -*-

class Feeder_Visitor(object):

    def visit_cat(self, cat):
        cat.eat()
        return 'cat'

    def visit_dog(self, dog):
        dog.eat()
        return 'dog'
