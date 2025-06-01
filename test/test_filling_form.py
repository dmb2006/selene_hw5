from selene import browser, command, have
import pytest
import os

file_path = r"D:\home_work_QaGuru\selene_hw5"

def test_felling_form(browser_option, credentials):
    assert os.path.exists(file_path)

    browser.open('/automation-practice-form')
    browser.element('#firstName').type(credentials["first_name"])
    browser.element('#lastName').type(credentials["last_name"])
    browser.element('#userEmail').type(credentials['email'])
    browser.element('//div//label[contains(text(), "Male")]').click()
    browser.element('#userNumber').type(credentials['mobile'])
    browser.element('#dateOfBirthInput').click()
    browser.element('//select[@class="react-datepicker__year-select"]//option[contains(text(), "1989")]').click()
    browser.element('//select[@class="react-datepicker__month-select"]//option[contains(text(), "September")]').click()
    browser.element('.react-datepicker__day--012').click()
    browser.element('#subjectsInput').type(credentials['subject'])
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').perform(command.js.scroll_into_view).type(credentials['current_address'])
    # browser.element('#currentAddress').type(credentials['current_address'])
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    browser.element('.table-responsive').all('td').even.should(have.exact_texts(
        'Oleg Petrov', 'test@test.ru', 'Male', '7911888664', '12 September,1989', '', 'Reading, Sports',
        'selene_hw5', 'Saint-Petersburg', 'Haryana Karnal'
    ))

