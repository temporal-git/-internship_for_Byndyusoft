import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def options():
    options = Options()
    # options.add_argument('--headless')
    options.page_load_strategy = 'eager'

    return options 


@pytest.fixture 
def browser(options):
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

