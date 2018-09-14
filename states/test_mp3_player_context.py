# -*- coding: UTF-8 -*-

import unittest

from states.mp3_player_context import MP3_Player_Context
from states.concrete_state import Playing_State

class Test_Mp3_Player_Context(unittest.TestCase):

    def test_mp3_context(self):
        mp3 = MP3_Player_Context(Playing_State())
        mp3.play()
        self.assertEqual('Playing', mp3.state)
        mp3.play()
        self.assertEqual('Standby', mp3.state)


if __name__ == '__main__':
    unittest.main()