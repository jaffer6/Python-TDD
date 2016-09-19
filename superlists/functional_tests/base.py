'''
Following Test Driven Development with Python.pdf
http://it-ebooks.info/book/3526/

Created on 14 Sep 2016

@author: Aamir.Jaffer
'''

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys

class FunctionalTest(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        # Used to do test setup for the whole class, run once
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
        
    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
    
    def setUp(self):
        # Runs before each test
        self.browser = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        # Runs after each test
        self.browser.refresh()
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')