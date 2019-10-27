from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
#browser.get('http://seleniumhq.org/')
assert 'Django' in browser.title