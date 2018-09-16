# -*- coding: UTF-8 -*-

import unittest

from visitor.animals import Cat, Dog
from visitor.feeder_visitor import Feeder_Visitor

class Test_Visitor(unittest.TestCase):

    def test_visitor(self):
        result = Cat().accept(Feeder_Visitor())
        self.assertEqual('cat', result)

        result = Dog().accept(Feeder_Visitor())
        self.assertEqual('dog', result)


if __name__ == '__main__':
    unittest.main()