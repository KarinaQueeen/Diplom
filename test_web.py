from testpage import OperationsHelper
import logging
import yaml


class TestClass:
    def test_positive_1(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят название кнопки 'Войти'
        '''
        logging.info('Positive Test 1')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_login_text() == 'Войти'

    def test_positive_2(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят переход при клике по кнопке 'Войти'
        '''
        logging.info('Positive Test 2')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_login()
        url = browser.current_url
        assert 'hh.ru/account/login' in url

    def test_positive_3(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят название раздела 'Новости'
        '''
        logging.info('Positive Test 3')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_news_text() == 'Новости'

    def test_positive_4(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят переход по клику на раздел 'Новости'
        '''
        logging.info('Positive Test 4')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_news()
        assert test_page.get_news_feed_text() == 'Новости сайта'

    def test_positive_5(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят название раздела 'Статьи'
        '''
        logging.info('Positive Test 5')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_articles_text() == 'Статьи'

    def test_positive_6(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят переход по клику на раздел 'Статьи'
        '''
        logging.info('Positive Test 6')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_articles()
        assert test_page.get_blog_text() == 'Блог'

    def test_positive_7(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят цвет кнопки 'Найти работу'
        '''
        logging.info('Positive Test 7')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        assert test_page.get_color_button() == 'rgba(23, 133, 229, 1)'

    def test_positive_8(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Вводит название вакансии
        3. Кликает по кнопке 'Найти работу'
        4. Проверяет корректность запроса
        '''
        logging.info('Positive Test 8')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.enter_work('Тестировщик')
        test_page.click_work()
        assert 'Работа тестировщиком' in test_page.get_h1_text()

    def test_negative_1(self, browser):
        '''
        1. Открывает главную страницу 'hh.ru'
        2. Проверят ошибку при неверном вводе логина для авторизации
        '''
        logging.info('Negative Test 1')
        test_page = OperationsHelper(browser)
        test_page.go_to_site()
        test_page.click_login()
        test_page.enter_login('8900')
        test_page.click_go()
        assert test_page.get_error_login() == 'Пожалуйста, укажите email или телефон'
