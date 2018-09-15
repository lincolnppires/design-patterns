# -*- coding: UTF-8 -*-

class Emp_Memento(object):
    def __init__(self, id, name, phone, designation):
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__designation = designation

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def designation(self):
        return self.__designation

    def info_emp(self):
        print('id: ' + self.id + ' name: ' + self.name + ' phone ' + self.phone + ' designation ' + self.designation)
