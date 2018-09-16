# -*- coding: UTF-8 -*-

class Cat(object):

    def eat(self):
        print('eat cat')

    def accept(self, visitor):
        return visitor.visit_cat(self)


class Dog(object):

    def eat(self):
        print('eat dog')

    def accept(self, visitor):
        return visitor.visit_dog(self)