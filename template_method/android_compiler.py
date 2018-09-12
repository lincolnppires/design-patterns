# -*- coding: UTF-8 -*-

from template_method.cross_compile_template import Cross_Compile_Template

class Android_Compiler(Cross_Compile_Template):

    def collect_source(self):
        print('Android')

    def compile_to_target(self):
        return 'android'
