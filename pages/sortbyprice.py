from selenium.webdriver.common.by import By
from pages.basepage_methods import Pages


class SortPrice(Pages):

    OPTION_VALUE = (By.CSS_SELECTOR, "select.orderby option")

    def find_sort_option(self, option_name):

        options = self.driver.find_elements(*self.OPTION_VALUE)

        for option in options:
            if option.text == option_name:
                option.click()
                break
# verify using url

    def verify_d(self, price_d):
        print(type(price_d), price_d)
        self.verify_url_contains_query(price_d)

    def verify_a(self, price_d):
        print(type(price_d), price_d)
        self.verify_url_contains_query(price_d)

# verify using sorted func

    def method_sor_d(self, pd):
        options = self.driver.find_elements(*self.OPTION_VALUE)

        if options[1] == pd:
            self.verify_pricing_d(pd)

    def method_sor_a(self, pa):
        options = self.driver.find_elements(*self.OPTION_VALUE)

        if options[1] == pa:
            self.verify_pricing_a(pa)
