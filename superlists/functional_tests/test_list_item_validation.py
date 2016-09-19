'''
Following Test Driven Development with Python.pdf
http://it-ebooks.info/book/3526/

Created on 14 Sep 2016

@author: Aamir.Jaffer
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        
        #Edith goes to the home page and accidentally tries to submit
        #an empty list item. She hits ENTER on the empty inputbox
        self.browser.get(self.server_url)
        self.browser.find_element_by_id("id_new_item").send_keys('\n')
        
        #The home page refreshes, and there is an error message saying that
        #list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
                
        #She tries again with some text for the item, which works now
        self.browser.find_element_by_id("id_new_item").send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
                
        #Perversely, she tries to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
                
        #She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        #print(self.browser.response.content.decode())
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
                
        #And she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')        
        
    
    