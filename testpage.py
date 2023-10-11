from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import yaml


class TestSearchLocators:
    """
    Хранит данные о локаторах для поиска тестируемых элементов в виде коллекции словаря
    """
    ids = dict()
    with open("locators.yaml", encoding="utf-8") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


#    for locator in locators["css"].keys():
#        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):
    """
    Реализует вспомогательные методы для поиска и взаимодействия с элементами веб страницы
    """
    with open("config.yaml", encoding="utf-8") as f:
        testdata = yaml.safe_load(f)



    def enter_text_info_field(self, locator, word, description=None):
        """
        Вводит строку текста в поле найденному по локатору
        :param locator: локатор для поиска элемента
        :param word: строка текста
        :param description: описание локатора
        :return: True в случае успеха
        """
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {element_name} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {element_name}")
            return True

    def click_button(self, locator, description=None):
        """
        Кликает по элементу найденному по локатору
        :param locator: локатор для поиска элемента
        :param description: описание локатора
        :return: True в случае успеха
        """
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
            logging.exception("Exception witch click")
        logging.debug(f"Click to element {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        """
        Получает хранящийся в элементе текст
        :param locator: локатор для поиска элемента
        :param description: описание локатора
        :return: True в случае успеха
        """
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
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"Find text {text} in field {element_name}")
        return text

    def get_attribute_from_element(self, locator, attribute, description=None):
        """
        Получает значение атрибута элемента
        :param locator:  локатор для поиска элемента
        :param attribute: название атрибута
        :param description: описание локатора
        :return: значение атрибута
        """
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            attr = field.get_attribute(attribute)
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"Find attribute {attribute} in field {element_name}")
        return attr

    # ENTER TEXT
    def enter_city(self, city):
        """
        Вводит название города в поле ввода
        :param city: название города
        """
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_INPUT_CITY"], city, description="INPUT_LOGIN")

    # CLICK

    def click_login(self):
        """
        Кликает по кнопке для входа
        """
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN'],
                          description="click_login")
    #
    # GET TEXT
    def get_login_text(self):
        """
        Возвращает название кнопки для регистрации
        """
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_LOGIN"], description="login")


