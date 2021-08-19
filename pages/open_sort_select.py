from pages.basepage_methods import Pages
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Sort(Pages):
    OPTION_VALUE = (By.CSS_SELECTOR, "select.orderby option")
   # OPTION_TEXT = "Sort by price: low to high"

    def select_department(self):
        select = Select(self.find_elements(*self.OPTION_VALUE))
        print(select)
        select = select.select_by_value('price')
        return select

    def click_option_select(self, select):
        self.click(select)

