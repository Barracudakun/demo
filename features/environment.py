from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from app.application import Applications
# from pages.logger import logger, MyListener
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = ''
bs_pw = ''


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\omar\\jobeasyinternship\\chromedriver.exe')

    # HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(chrome_options=options)

    # EventFiringWebDriver - log file ###
    # for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())

    # for browserstack ###
   # desired_cap = {
    #    'browser': 'Chrome',
   #     'browser_version': '91',
   #     'os': 'Windows',
   #    'os_version': '10',
    #    'name': test_name
    #}
    #url = f'https://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    #context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Applications(context.driver)


# def before_scenario(context, scenario):
#     logger.info(f'\nStarted scenario: {scenario.name}')
#     browser_init(context, scenario.name)
#
#
# def before_step(context, step):
#     logger.info(f'\nStarted step: {step}')
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         logger.info(f'\nStep failed: {step}')
#
#
# def after_scenario(context, feature):
#     context.driver.delete_all_cookies()
#     context.driver.quit()


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()

# context.driver.quit()