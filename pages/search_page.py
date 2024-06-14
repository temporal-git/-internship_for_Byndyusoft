from .base_page import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SearchPage, self).__init__(*args, **kwargs)

    def fill_search(self, text):
        search_field = self.browser.find_element(*SearchPageLocators.SEARCH_INPUT)
        search_field.send_keys(text)

    def start_search(self):
        search_field = self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_field.click()

    def choose_first_result(self):
        search_field = self.browser.find_element(*SearchPageLocators.SEARCH_FIRST_RESULT)
        search_field.click()

    def change_tab(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
