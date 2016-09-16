'''
Following Test Driven Development with Python.pdf
http://it-ebooks.info/book/3526/

Created on 14 Sep 2016

@author: Aamir.Jaffer
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        pass
    
    