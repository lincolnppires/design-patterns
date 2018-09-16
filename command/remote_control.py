# -*- coding: UTF-8 -*-

class Remote_Control(object):

    def on_button_pressed(self, on_command):
        self.__on_command = on_command
        self.__on_command.execute()
        self.__undo_command = on_command


    def off_button_pressed(self, off_command):
        self.__off_command = off_command
        self.__off_command.execute()
        self.__undo_command = off_command

    def undo_button_pressed(self):
        self.__undo_command.undo()


