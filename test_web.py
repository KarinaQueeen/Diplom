from testpage import OperationsHelper
import logging
import yaml


class TestHeader:
    with open("config.yaml", encoding="utf-8") as f:
        testdata = yaml.safe_load(f)

    def test_step1(self, browser):
        """
        Тест открывает главную страницу "Яндекс погода",
        вводит название города,
        подтверждает название на дополнительной странице,
        получает координаты города,
        проверяет, что открылась страница с искомым городом
        """
        logging.info("Test_1 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_login_text()=="Войти"

    def test_step2(self, browser):
        """
        Тест открывает главную страницу "Яндекс погода",
        вводит название города,
        подтверждает название на дополнительной странице,
        получает координаты города,
        проверяет, что открылась страница с искомым городом
        """
        logging.info("Test_2 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_login()
        url = browser.current_url
        assert 'hh.ru/account/login' in url