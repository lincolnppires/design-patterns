# -*- coding: UTF-8 -*-

from command.command_base import Command_Base

class Car_Move_Command(Command_Base):

    def __init__(self, car):
        self.__car = car

    def execute(self):
        self.__car.move()

    def undo(self):
        self.__car.stop()


class Car_Stop_Command(Command_Base):

    def __init__(self, car):
        self.__car = car

    def execute(self):
        self.__car.stop()

    def undo(self):
        self.__car.move()

