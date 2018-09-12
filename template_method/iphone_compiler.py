# -*- coding: UTF-8 -*-

from template_method.cross_compile_template import Cross_Compile_Template

class IPhone_Compiler(Cross_Compile_Template):

    def collect_source(self):
        print('Iphone')

    def compile_to_target(self):
        return 'iphone'

