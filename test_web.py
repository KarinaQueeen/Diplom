from testpage import OperationsHelper
import logging
import yaml
class TestHeader:
    with open("config.yaml", encoding="utf-8") as f:
        testdata = yaml.safe_load(f)
    def test_step1(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят название кнопки для входа
        """
        logging.info("Test_1 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_login_text()=="Войти"
    def test_step2(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят работоспособность кнопки для входа
        """
        logging.info("Test_2 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_login()
        url = browser.current_url
        assert 'hh.ru/account/login' in url
    def test_step3(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят название блока "Новости"
        """
        logging.info("Test_3 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_news_text()=="Новости"
    def test_step4(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят переход по клику на блок "Новости"
        """
        logging.info("Test_4 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_news()
        assert test_page.get_news_feed_text()=="Новости сайта"
    def test_step5(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят название блока "Статьи"
        """
        logging.info("Test_5 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_articles_text()=="Статьи"
    def test_step6(self, browser):
        """
        Тест открывает главную страницу "hh.ru",
        проверят переход по клику на блок "Статьи"
        """
        logging.info("Test_6 Starting")
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_articles()
        assert test_page.get_blog_text()=="Блог"