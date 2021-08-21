
from pages.sortbyprice import SortPrice
from pages.open_home import OpenHomePage


class Applications:
    def __init__(self, driver):
        self.driver = driver
        self.home = OpenHomePage(self.driver)
        self.sort_price_page = SortPrice(self.driver)
