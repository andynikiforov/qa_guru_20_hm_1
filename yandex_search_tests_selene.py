from selene import browser, have, be


def test_search():
    browser.open('https://ya.ru')
    browser.element('[name="text"][aria-label="Запрос"]').type('qa.guru').press_enter()
    browser.element('//button[contains(., "Нет, спасибо")]').should(be.clickable).click()
    browser.element('#search-result').should(have.text('Курсы тестировщиков'))


