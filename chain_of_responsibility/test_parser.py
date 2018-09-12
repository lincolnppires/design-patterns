# -*- coding: UTF-8 -*-

import unittest

from chain_of_responsibility.text_parser import Text_parser
from chain_of_responsibility.json_parser import Json_parser
from chain_of_responsibility.xml_parser import XML_parser
from chain_of_responsibility.csv_parse import CSV_parser
from chain_of_responsibility.invalid_parser import Invalid_parser
from chain_of_responsibility.parser import Parser

class Test_Parser(unittest.TestCase):

   def test_each_one_parse(self):
       parser = Text_parser(Invalid_parser())
       self.assertTrue(parser.parse('arquivo.txt'))

       parser = Json_parser(Invalid_parser())
       self.assertTrue(parser.parse('arquivo.json'))

       parser = XML_parser(Invalid_parser())
       self.assertTrue(parser.parse('arquivo.xml'))

       parser = CSV_parser(Invalid_parser())
       self.assertTrue(parser.parse('arquivo.csv'))

   def test_chain_of_parse(self):
       parser = Parser()
       self.assertTrue(parser.process('arquivo.txt'))
       self.assertTrue(parser.process('arquivo.json'))
       self.assertTrue(parser.process('arquivo.xml'))
       self.assertTrue(parser.process('arquivo.csv'))
       self.assertFalse(parser.process('arquivo.xpto'))

if __name__ == '__main__':
    unittest.main()