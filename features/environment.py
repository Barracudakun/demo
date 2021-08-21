from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from app.application import Applications

# from selenium import logger, MyListener
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings


bs_user = 'omarnurhusien1'
bs_pw = 'dxn5AU82PBcDbsLpfQBs'


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
    # context.driver = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver')
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\omar\\jobeasyinternship\\chromedriver.exe')
    # context.driver = webdriver.Chrome(executable_path='/chromedriver.exe')
    # context.driver = webdriver.Firefox(executable_path="C:\\Users\\omar\\jobeasyinternship\\geckodriver.exe")
    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options)
    # options = webdriver.FirefoxOptions()
    # context.driver = webdriver.firefox(firefox_options=options)

    #      EventFiringWebDriver - log file ###
    #     for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    #     for headless mode ###
    #     context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())
    #
    #    for browserstack ###
    # desired_cap = {
    #    'browser': 'Chrome',
    #    'browser_version': '91',
    #    'os': 'Windows',
    #   'os_version': '10',
    #    'name': test_name
    # }
    # url = f'https://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # desired_cap = {
    #     'browserName': 'iPhone',
    #     'device': 'iPhone 11',
    #     'realMobile': 'true',
    #     'os_version': '14.0',
    #     'name': 'BStack-[Python] Sample Test',  # test name
    #     'build': 'BStack Build Number 1',  # CI/CD job or build name
    #     'browserstack.debug': True,
    # }
    # context.driver = webdriver.Remote(
    #     command_executor='https://omarnurhusien1:dxn5AU82PBcDbsLpfQBs@hub-cloud.browserstack.com/wd/hub',
    #     desired_capabilities=desired_cap)
    # context.driver.get("https://www.google.com")
    # if not "Google" in context.driver.title:
    #     raise Exception("Unable to load google page!")
    # elem = context.driver.find_element('name', "q")
    # elem.send_keys("BrowserStack")
    # elem.submit()
    # try:
    #     WebDriverWait(context.driver, 5).until(EC.title_contains("BrowserStack"))
    #     # Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
    #     context.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
    # except TimeoutException:
    #     context.driver.execute_script(
    #         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
    # print(context.driver.title)
    # context.driver.quit(quit)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Applications(context.driver)


# def before_scenario(context, scenario):
#     context.driver.logger.info(f'\nStarted scenario: {scenario.name}')
#     browser_init(context, scenario.name)
#
#
# def before_step(context, step):
#     context.driver.logger.info(f'\nStarted step: {step}')
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         context.driver.logger.info(f'\nStep failed: {step}')
#
#
# def after_scenario(context, feature):
#     context.driver.delete_all_cookies()
#     context.driver.quit()
#
#
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

    context.driver.quit()