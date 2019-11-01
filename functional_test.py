from selenium import webdriver
import pytest



@pytest.fixture()
def setup_browser():
    global browser
    print("setting up the browser")
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    yield
    browser.quit()

def test_1(setup_browser):
    print("Running test 1")
    browser.get('http://localhost:8000')
    #browser.get('http://seleniumhq.org/')
    assert 'Django' in browser.title