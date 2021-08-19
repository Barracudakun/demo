from pages.sortbyprice import SortPrice
from pages.open_home import OpenHomePage
from pages.open_sort_select import Sort


class Applications:
    def __init__(self, driver):
        self.driver = driver
        self.home = OpenHomePage(self.driver)
        self.sort_price_page = SortPrice(self.driver)
        self.sort_price_select = Sort(self.driver)