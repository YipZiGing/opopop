import os
import sys

sys.path.append(os.getcwd())

from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class NetworkPage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text,'更多')]"

    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"

    # 首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2g按钮
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3g按钮
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def click_more_button(self):
        self.click(self.more_button)

    def click_network_button(self):
        self.click(self.network_button)

    def click_first_network_button(self):
        self.click(self.first_network_button)

    def click_network_2g_button(self):
        self.click(self.network_2g_button)

    def click_network_3g_button(self):
        self.click(self.network_3g_button)