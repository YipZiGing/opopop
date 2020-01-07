import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        self.display_page.click_display()
        self.display_page.click_search()
        self.display_page.input_search_text("1")
        self.display_page.click_text_view()
        self.display_page.click_back()