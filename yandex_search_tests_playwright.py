from playwright.sync_api import sync_playwright, expect
import pytest


def test_search():
    with sync_playwright() as p:
        # Запуск браузера с явным указанием headless=False для визуального наблюдения
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto('https://www.ya.ru/', timeout=10000)

            # Ждем появления поисковой строки
            search_box = page.locator('[name="text"]')
            expect(search_box).to_be_visible()

            # Ввод поискового запроса
            search_box.fill('qa.guru')
            search_box.press('Enter')

            # Ожидание перехода на страницу результатов
            page.wait_for_url('**/search/**', timeout=10000)

            # Обработка возможного всплывающего окна (более надежный способ)
            no_thanks_button = page.locator("button:has-text('Нет, спасибо')")
            if no_thanks_button.is_visible(timeout=5000):
                no_thanks_button.click()

            # Проверка наличия текста на странице
            expect(page.locator('body')).to_contain_text('Курсы тестировщиков')

        except Exception as e:
            pytest.fail(f"Тест упал с ошибкой!: {str(e)}")
        finally:
            browser.close()