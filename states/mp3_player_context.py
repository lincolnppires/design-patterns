# -*- coding: UTF-8 -*-

class MP3_Player_Context(object):

    def __init__(self, state):
        self.__state = state


    def play(self):
        self.__state.press_play(self)


    @property
    def state(self):
        return self.__state.value


    @state.setter
    def state(self, state):
        self.__state = state



