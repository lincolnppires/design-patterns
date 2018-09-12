# -*- coding: UTF-8 -*-

from chain_of_responsibility.text_parser import Text_parser
from chain_of_responsibility.json_parser import Json_parser
from chain_of_responsibility.xml_parser import XML_parser
from chain_of_responsibility.csv_parse import CSV_parser
from chain_of_responsibility.invalid_parser import Invalid_parser

class Parser(object):

    def process(self, file_name):
        result = Text_parser(
                    Json_parser(
                        XML_parser(
                            CSV_parser(
                                Invalid_parser()
                            )
                        )
                    )
                ).parse(file_name)

        return result
