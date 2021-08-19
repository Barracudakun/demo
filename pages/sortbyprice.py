from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.basepage_methods import Pages
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SortPrice(Pages):
   # SORTED_ASC = (By.CSS_SELECTOR, "span.price")
   # SORTED_DESC = (By.CSS_SELECTOR, "span.price-desc")
    #ELEMENT = (By.CSS_SELECTOR, "select.orderby")
    OPTION_VALUE = (By.CSS_SELECTOR, "select.orderby option")
    #OPTION_TEXT = "Sort by price: low to high"
    # def click_over(self):
    #
    #     self.click(*self.ELEMENT)

    # def select_by_desc(self):
    #     self.verify_select_desc(self, *self.SORTED_DESC)
    #
    # def select_by_asc(self):
    #     self.verify_select_asc(self, *self.SORTED_ASC)

    def find_sort_option(self, option_name):
        try:
            options = self.find_elements(self.OPTION_VALUE)
        # print(options)
            wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.element_to_be_clickable(self.OPTION_VALUE))

            for option in options:
                if option.text == self.option_name:
                # print('text', option.text)
                # print("Value is: %s" % option.get_attribute("value"))
                # print("Text is: %s" % option.get_attribute("text"))
                    wait.until(EC.element_to_be_clickable(options))

# I am not sure why Montilla wants here
                    option.click()
                    # ignore comments
#         select = Select(self.driver.find_element_by_tag('option'))
# # select.select_by_index(index)
#         print(select.select_by_visible_text("text"))
#         print(select.select_by_value("value"))
#
#         print(select = Select(self.driver.find_element_by_id('id')))
#         select.deselect_all()

        except (InvalidArgumentException,TypeError, IndentationError ) as e:
            print(type(e), e)
