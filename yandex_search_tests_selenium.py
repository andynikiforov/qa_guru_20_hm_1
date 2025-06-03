from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search():
    driver = webdriver.Chrome()
    driver.get('https://www.ya.ru/')

    search_box = driver.find_element(By.NAME, 'text')
    search_box.send_keys('qa.guru' + Keys.RETURN)

    try:
        no_thanks_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Нет, спасибо')]")))
        no_thanks_button.click()
    except:
        print("Всплывающее окно не появилось")

    assert 'Курсы тестировщиков' in driver.page_source
    driver.quit()