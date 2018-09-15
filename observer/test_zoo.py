# -*- coding: UTF-8 -*-

import unittest

from observer.animal_listener import obs1, obs2
from observer.zoo import Zoo
from observer.animal import Animal

class Test_Zoo(unittest.TestCase):

    def test_mp3_context(self):
        obs = [obs1, obs2]
        zoo = Zoo(obs)
        zoo.add_animal(Animal('lion'))
        zoo.add_animal(Animal('elephant'))

if __name__ == '__main__':
    unittest.main()