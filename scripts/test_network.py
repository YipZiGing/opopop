import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import NetworkPage


class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_2g(self):
        self.network_page.click_more_button()
        self.network_page.click_network_button()
        self.network_page.click_first_network_button()
        self.network_page.click_network_2g_button()

    def test_3g(self):
        self.network_page.click_more_button()
        self.network_page.click_network_button()
        self.network_page.click_first_network_button()
        self.network_page.click_network_3g_button()