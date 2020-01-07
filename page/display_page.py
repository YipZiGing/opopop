from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_search_text(self, text):
        self.input_text(self.input_text_view, text)

    def click_text_view(self):
        self.click(self.input_text_view)

    def click_back(self):
        self.click(self.back_button)
