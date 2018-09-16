# -*- coding: UTF-8 -*-

from command.command_base import Command_Base

class Top_Rotate_Command(Command_Base):

    def __init__(self, rotating_top):
        self.__rotating_top = rotating_top

    def execute(self):
        self.__rotating_top.start_rotating()

    def undo(self):
        self.__rotating_top.stop_rotating()


class Top_Stop_Rotate_Command(Command_Base):

    def __init__(self, rotating_top):
        self.__rotating_top = rotating_top

    def execute(self):
        self.__rotating_top.stop_rotating()

    def undo(self):
        self.__rotating_top.start_rotating()
