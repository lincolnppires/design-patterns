# -*- coding: UTF-8 -*-

from states.state import State

class Playing_State(State):

    def press_play(self, context):
        context.state = Standby_State()

    @property
    def value(self):
        return 'Standby'



class Standby_State(State):

    def press_play(self, context):
        context.state = Playing_State()

    @property
    def value(self):
        return 'Playing'