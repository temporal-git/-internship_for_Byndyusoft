from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '[name="q"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[value="Поиск в Google"]')
    SEARCH_FIRST_RESULT = (By.CSS_SELECTOR, '.iUh30')


class MainPageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, '.btn--info.js-popup-callback-show')
    TG_LINK = (By.CSS_SELECTOR, '.popup-callback__contacts-tg')
