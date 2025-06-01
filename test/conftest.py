import pytest
from selene import browser

@pytest.fixture()
def credentials():
    return {
        "first_name": "Oleg",
        "last_name": "Petrov",
        'email': 'test@test.ru',
        'mobile': 7911888664,
        'date_birth': '12 june 1989',
        'subject': 'Autotesting',
        'current_address': 'Saint-Petersburg'
}

@pytest.fixture(scope="function", autouse=True)
def browser_option():
    browser.config.base_url='https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1020
    yield browser
    browser.quit()

# @pytest.fixture()
# def credentials():
#     cred_key = ['first_name', 'last_name', 'email', 'mobile', 'date_birth', 'subject', 'current_address']
#     cred_values = ['Oleg', 'Petrov', 'test@test.ru', '7911888664', '12 june 1989', 'Autotesting', 'Saint-Petersburg']
#     dict(zip(cred_key, cred_values))
#     return
