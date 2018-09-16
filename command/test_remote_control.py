# -*- coding: UTF-8 -*-

import unittest

from command.car import Car
from command.car_command import Car_Move_Command, Car_Stop_Command
from command.top_rotate_command import Top_Rotate_Command, Top_Stop_Rotate_Command
from command.rotating_top import Rotating_top
from command.remote_control import Remote_Control


class Test_Remote_Control(unittest.TestCase):

   def test_remote_control(self):
       remote_control = Remote_Control()

       car_move_command = Car_Move_Command(Car())
       car_stop_command = Car_Stop_Command(Car())

       remote_control.on_button_pressed(car_move_command)
       remote_control.off_button_pressed(car_stop_command)
       remote_control.undo_button_pressed()

       top_rotate_command = Top_Rotate_Command(Rotating_top())
       top_stop_rotate_command = Top_Stop_Rotate_Command(Rotating_top())

       remote_control.on_button_pressed(top_rotate_command)
       remote_control.off_button_pressed(top_stop_rotate_command)
       remote_control.undo_button_pressed()


if __name__ == '__main__':
    unittest.main()