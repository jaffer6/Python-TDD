'''
Following Test Driven Development with Python.pdf
http://it-ebooks.info/book/3526/

Created on 14 Sep 2016

@author: Aamir.Jaffer
'''

from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):            
        
    def test_layout_and_styling(self):
        # Edith goes to the home Page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
                
        #She notices the inputbox is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] /2, 512, delta=10)