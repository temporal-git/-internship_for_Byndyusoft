from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def find_order_button(self):
        order_button = self.browser.find_element(*MainPageLocators.ORDER_BUTTON)
        order_button.click()

    def get_tg_link(self):
        tg_link = self.browser.find_element(*MainPageLocators.TG_LINK).get_attribute('href')
        print(" The current url is: " + tg_link)
        assert tg_link == "https://t.me/alexanderbyndyu", "URL не совпадает"
