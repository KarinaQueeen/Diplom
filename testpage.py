from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    '''
    Хранит данные о локаторах для поиска тестируемых элементов в виде коллекции словаря
    '''
    ids = dict()
    with open('locators.yaml', encoding='utf-8') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])


class OperationsHelper(BasePage):
    '''
    Реализует вспомогательные методы для поиска и взаимодействия с элементами веб страницы
    '''

    def enter_text_info_field(self, locator, word, description=None):
        '''
        Вводит текст в поле
        :param locator: локатор для поиска элемента
        :param word: строка текста
        :param description: описание локатора
        :return: True в случае успеха
        '''
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {element_name} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {element_name}')
            return True

    def click_button(self, locator, description=None):
        '''
        Кликает по элементу
        :param locator: локатор для поиска элемента
        :param description: описание локатора
        :return: True в случае успеха
        '''
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception witch click')
        logging.debug(f'Click to element {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        '''
        Получает хранящийся в элементе текст
        :param locator: локатор для поиска элемента
        :param description: описание локатора
        :return: True в случае успеха
        '''
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'Find text {text} in field {element_name}')
        return text

    def get_css_property(self, locator, css, description=None):
        '''
        Получает характеристики элемента
        :param locator: локатор для поиска элемента
        :css: параметр элемента
        :param description: описание локатора
        :return: True в случае успеха
        '''
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            field = self.get_element_property(locator, css)
        except:
            logging.exception(f'Exception while get css from {element_name}')
            return None
        logging.debug(f'Find css {css} in field {element_name}')
        return field

    # ENTER TEXT
    def enter_login(self, login):
        '''
        Вводит текст в поле 'Логин'
        '''
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_ACCOUNT'], login, description='enter_login')

    def enter_work(self, work):
        '''
        Вводит текст в поле 'Вакансия'
        '''
        self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_INPUT_WORK'], work, description='enter_work')

    # CLICK
    def click_login(self):
        '''
        Кликает по кнопке 'Войти'
        '''
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN'],
                          description='click_login')

    def click_news(self):
        '''
        Кликает по ссылке 'Новости'
        '''
        self.click_button(TestSearchLocators.ids['LOCATOR_NEWS'],
                          description='click_news')

    def click_articles(self):
        '''
        Кликает по ссылке 'Статьи'
        '''
        self.click_button(TestSearchLocators.ids['LOCATOR_ARTICLES'],
                          description='click_articles')

    def click_go(self):
        '''
        Кликает по кнопке 'Продолжить'
        '''
        self.click_button(TestSearchLocators.ids['LOCATOR_GO'],
                          description='click_go')

    def click_work(self):
        '''
        Кликает по кнопке 'Найти работу'
        '''
        self.click_button(TestSearchLocators.ids['LOCATOR_BUTTON'],
                          description='click_work')

    # GET TEXT
    def get_login_text(self):
        '''
        Возвращает название кнопки 'Войти'
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LOGIN'], description='get_login_text')

    def get_news_text(self):
        '''
        Возвращает название раздела 'Новости'
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_NEWS'], description='get_news_text')

    def get_news_feed_text(self):
        '''
        Возвращает заголовок новостной ленты
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_NEWS_FEED'], description='get_news_feed_text')

    def get_articles_text(self):
        '''
        Возвращает название раздела 'Статьи'
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ARTICLES'], description='get_articles_text')

    def get_blog_text(self):
        '''
        Возвращает заголовок Блога
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_BLOG'], description='get_blog_text')

    def get_error_login(self):
        '''
        Возвращает текст ошибки при неправильном вводе логина
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_LOGIN'], description='get_error_login')

    def get_color_button(self):
        '''
        Возвращает цвет кнопки 'Найти работу'
        '''
        return self.get_css_property(TestSearchLocators.ids['LOCATOR_BUTTON'], 'background-color',
                                     description='get_color_button')

    def get_h1_text(self):
        '''
        Возвращает текст заголовка
        '''
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_H1'], description='get_h1_text')
