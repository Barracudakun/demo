from pages.basepage_methods import Pages


class OpenHomePage(Pages):
    URL = "https://gettop.us/product-category/iphone/"

    def open(self):
        self.open_url(self.URL)
