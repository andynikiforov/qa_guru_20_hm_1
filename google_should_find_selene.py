from selene import browser, be, have


def test_search():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').type('qa.guru')
    browser.element('[name="btnK"]').click()
    browser.element('html').should(have.text('Об этой странице'))
