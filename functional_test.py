from selenium import webdriver
import pytest

def setup_function():
    print("setup function")
    browser = webdriver.Firefox()


def test1():
    browser = webdriver.Firefox()
    print("Running test 1")
    browser.get('http://localhost:8000')
    #browser.get('http://seleniumhq.org/')
    assert 'Django' in browser.title