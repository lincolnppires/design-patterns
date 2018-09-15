# -*- coding: UTF-8 -*-

from memento.emp_memento import Emp_Memento

class Emp_Originator(object):

    def __init__(self, id, name, phone, designation):
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__designation = designation

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def designation(self):
        return self.__designation

    @designation.setter
    def designation(self, designation):
        self.__designation = designation

    def save_to_memento(self):
        emp_memento = Emp_Memento(self.id, self.name, self.phone, self.designation)
        return emp_memento

    def undo_from_memento(self, emp_memento):
        self.__id = emp_memento.id
        self.__name = emp_memento.name
        self.__phone = emp_memento.phone
        self.__designation = emp_memento.designation


    def info_emp(self):
        print('id: ' + self.id + ' ,name: ' + self.name + ' ,phone: ' + self.phone + ' ,designation: ' + self.designation)




