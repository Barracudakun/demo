# from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User URL directly')
def get_top(context):
    context.app.home.open()

# @when('Click on search by ascending')
# def click_over(context):
#     context.app.sort_price_page.find_sort_option("Sort by price: low to high")
#     context.app.sort_price_select.click_option_select()


@then('verify price in url')
def verify_asc(context):
    # verify that you have order=price in url
    # verify that prices are sorted in asc order
    context.app.sort_price_page.verify_a('?orderby=price')


@then ('verify price-desc in url')
def verify_desc(context):
    # verify that you have order=price in url
    # verify that prices are sorted in asc order
    context.app.sort_price_page.verify_d('price-desc')


@when('Products are displayed in correct order, Sort by price: low to high option is preselected by price')
def click_over(context):

    context.app.sort_price_page.find_sort_option("Sort by price: low to high")


@when('Products are displayed in correct order, Sort by price: high to low option is preselected by price-desc')
def click_over(context):
    context.app.sort_price_page.find_sort_option("Sort by price: high to low")


@then('verify price is ascending starts at {pa}')
def verify_a(context, pa):
    context.app.sort_price_page.method_sor_a(pa)


@then ('verify price-desc is descending starts at {pd}')
def verify_d(context, pd):
    context.app.sort_price_page.method_sor_d(pd)
