from selenium import webdriver
import pytest


browser = webdriver.Firefox()
# @pytest.fixture(scope="session")
# def setup_browser():
#     print("setting up the browser")
#     browser = webdriver.Firefox()
#     yield browser


def test_1():
    print("Running test 1")
    browser.get('http://localhost:8000')
    #browser.get('http://seleniumhq.org/')
    assert 'Django' in browser.title