# -*- coding: UTF-8 -*-

class Emp_Caretaker(object):

    def __init__(self):
        self.__mementos = []

    def get_memento(self):
        emp_memento = self.__mementos[-1]
        del self.__mementos[-1]
        return emp_memento

    def add_memento(self, emp_memento):
        self.__mementos.append(emp_memento)

    