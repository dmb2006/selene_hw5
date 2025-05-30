import pytest
from selene import browser

@pytest.fixture()
def test_browser_option():
    browser.config.base_url='https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1920
    browser.config.window_height = 1020
