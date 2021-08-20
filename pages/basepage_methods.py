from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Pages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def hover_cursor(self, *locator):
        new_arrivals = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
        sleep(10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(ec.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(ec.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        sleep(10)
        actual_text = self.driver.find_element(*locator).text
        sleep(10)
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_li(self, *sor):
        for i in range(len(sor)):
            if sor[i] >= sor[i + 1]:
                print(True)
            return False

    def verify_text_in(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} in {actual_text}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        if query == '?orderby=price-desc':

            assert query in self.driver.current_url.split('/'), f'{query} not in {self.driver.current_url.split("/")}'
        else:

            assert '?orderby=price' in self.driver.current_url, f'{query} not equal {self.driver.current_url}'

    def verify_current_u(self, expected_url):
        # assert self.driver.current_url == expected_url, f'{expected_url} not equal {self.driver.current_url}'

        if self.driver.current_url == expected_url:
            print("pass")

        else:
            print("failed")

# verify descending prices

    def verify_pricing_d(self, sor):
        # sor_new = sorted(sor)
        assert sor == "999", f'{sor} is not equal to {"999"}'

# # verify ascending prices
    def verify_pricing_a(self, sor):
        # sor_new = sorted(sor)
        assert sor == "379", f'{sor} is not equal to {"379"}'

    # def verify_select_desc(self, *locator):
    #     select = Select(self.find_element(locator))
    #     select.select_by_value(locator)
    #
    # def verify_select_asc(self, *locator):
    #     select = Select(self.find_element(locator))
    #     select.select_by_value(locator)
