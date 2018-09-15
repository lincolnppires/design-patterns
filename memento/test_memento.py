# -*- coding: UTF-8 -*-

import unittest

from memento.emp_originator import Emp_Originator
from memento.emp_caretaker import Emp_Caretaker

class Test_Memento(unittest.TestCase):

    def test_memento_undo(self):

        emp_originator = Emp_Originator('306',"Mark Ferguson", "131011789610","Sales Manager")
        emp_memento = emp_originator.save_to_memento()
        emp_caretaker = Emp_Caretaker()
        emp_caretaker.add_memento(emp_memento)
        emp_originator.info_emp()

        print('emp_originator after updating phone number')
        emp_originator.phone = '131011888886'
        emp_memento = emp_originator.save_to_memento()
        emp_caretaker.add_memento(emp_memento)
        emp_originator.info_emp()

        print('emp_originator after updating designation')
        emp_originator.designation = 'Senior Sales Manager'
        emp_memento = emp_originator.save_to_memento()
        emp_caretaker.add_memento(emp_memento)
        emp_originator.info_emp()

        print('emp_originator after undoing designation update')
        current = emp_caretaker.get_memento()
        emp_memento = emp_caretaker.get_memento()
        emp_originator.undo_from_memento(emp_memento)
        emp_originator.info_emp()

        print('Original emp-originator after undoing phone number update')
        emp_memento = emp_caretaker.get_memento()
        emp_originator.undo_from_memento(emp_memento)
        emp_originator.info_emp()




if __name__ == '__main__':
    unittest.main()