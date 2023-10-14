from testpage import OperationsHelper
import logging
import yaml
class TestHeader:
    with open("config.yaml", encoding="utf-8") as f:
        testdata = yaml.safe_load(f)
    def test_positive_1(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят название кнопки для входа
        """
        logging.info("Positive Test 1")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_login_text()=="Войти"
    def test_positive_2(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят работоспособность кнопки для входа
        """
        logging.info("Positive Test 2")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_login()
        url = browser.current_url
        assert 'hh.ru/account/login' in url
    def test_positive_3(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят название раздел "Новости"
        """
        logging.info("Positive Test 3")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_news_text()=="Новости"
    def test_positive_4(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят переход по клику на раздел "Новости"
        """
        logging.info("Positive Test 4")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_news()
        assert test_page.get_news_feed_text()=="Новости сайта"
    def test_positive_5(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят название раздела "Статьи"
        """
        logging.info("Positive Test 5")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_articles_text()=="Статьи"
    def test_positive_6(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят переход по клику на раздел "Статьи"
        """
        logging.info("Positive Test 6")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_articles()
        assert test_page.get_blog_text()=="Блог"

    def test_positive_7(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят цвет кнопки
        """
        logging.info("Positive Test 7")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_color_button() == "#1785e5"
    def test_negative_1(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят текст ошибки при неверном вводе логина
        """
        logging.info("Negative Test 1")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_login()
        test_page.enter_login('8900')
        test_page.click_go()
        assert test_page.get_error_login()=="Пожалуйста, укажите email или телефон"

    def negative_test_2(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят переход по клику на раздел "Статьи"
        """
        logging.info("Negative Test 2")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_articles()
        assert test_page.get_blog_text()=="Блог"
