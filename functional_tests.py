#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
