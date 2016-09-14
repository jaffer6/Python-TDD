'''
Following Test Driven Development with Python.pdf
http://it-ebooks.info/book/3526/

Created on 14 Sep 2016

@author: Aamir.Jaffer
'''

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        # Runs before each test
        self.browser = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        # Runs after each test
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):        
        # Edith has heard about a cool new online todo-app.
        # She goes to check out it's homepage
        self.browser.get("http://localhost:8000")
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        
        self.fail("Finish the test!")
        
        # She is invited to enter a to-do item straight away
        
        # She types "Buy peacock feathers" into a text box
        # Edith's hobby is tying fly-fishing lures 
        
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        
        # There is still a text box inviting her to add another item
        # She enters "Use peacock feathers to make a fly"
        
        # The page updates again, and now shows both items on her List
        
        # Edith wonders whether the site will remember her list. Then she
        # sees the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        
        #She visits the URL, her to-do list is still there.
        
        # Satisfied she goes back to sleep
    
    
if __name__ == "__main__":
    unittest.main(warnings='ignore')