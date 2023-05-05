from main import *
import unittest

class TestsSteck(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(mystack.check('[([])((([[[]]])))]{()}'))
        self.assertTrue(mystack.check('(((([{}]))))'))
        self.assertTrue(mystack.check('{{[()]}}'))
        
    def test_false(self):
        self.assertFalse(mystack.check('}{}'))
        self.assertFalse(mystack.check('{{[(])]}}'))
        self.assertFalse(mystack.check('[[{())}]'))