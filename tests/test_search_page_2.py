from pages.search_page import SearchPage
from pages.main_page import MainPage
import pytest


class TestMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://www.google.ru/"
        search_text = "Byndyusoft"

        page = SearchPage(browser, link)
        page.open()
        page.fill_search(search_text)
        page.start_search()
        page.choose_first_result()
        page.change_tab()
        get_url = browser.current_url
        return get_url

    def test_tg_link(self, browser, setup):
        page = MainPage(browser, setup)
        page.open()
        page.find_order_button()
        page.get_tg_link()

