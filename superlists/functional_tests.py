'''
Created on 14 Sep 2016

@author: Aamir.Jaffer
'''

from selenium import webdriver

browser = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
browser.get("http://localhost:8000")

print(browser.title)

assert 'Django' in browser.title
