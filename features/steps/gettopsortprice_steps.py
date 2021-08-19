# from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User URL directly')
def get_top(context):
    context.app.home.open()


@when('Click on search by descending')
def click_over(context):
    #context.app.sort_price_page.click_over()
    context.app.sort_price_page.find_sort_option("Sort by price: low to high")
#    context.app.sort_price_page.find_sort_option()
   # context.app.sort_price_select.select_department()


@when('Click on search by ascending')
def click_over(context):
    context.app.sort_price_page.find_sort_option("Sort by price: low to high")
    context.app.sort_price_select.click_option_select()


@then('Products are displayed in correct order, Sort by price: high to low option is preselected')
def verify_select_desc(context):
    context.app.sort_price_page.find_sort_option()


@then('Products are displayed in correct order, Sort by price: low to high option is preselected')
def verify_select_asc(context):
    context.app.sort_price_page.find_sort_option()
