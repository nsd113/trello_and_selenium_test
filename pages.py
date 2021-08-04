from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPageLocators, BoardsPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_element_loc(self, path, time=20):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, path)),
                                               message=f"Can't find element: {path}")


class MainPage(BasePage):
    """Home page action methods come here."""

    def trello_main(self):
        self.wait_element_loc(MainPageLocators.main_locator_login_button)
        self.driver.find_element_by_xpath(MainPageLocators.main_locator_login_button).click()

    def trello_login(self, user_email, password):
        self.driver.find_element_by_id(MainPageLocators.login_user_id).send_keys(user_email)
        self.driver.find_element_by_id(MainPageLocators.login_password_id).send_keys(password)
        self.driver.find_element_by_xpath(MainPageLocators.user_login_button).click()
        print('Log in successful')

class CreateABoard(BasePage):
    def create_a_board(self, title):
        self.driver.find_element_by_xpath(BoardsPageLocators.start_create_board).click()
        self.driver.find_element_by_xpath(BoardsPageLocators.title_xpath).send_keys(title)
        self.driver.find_element_by_xpath(BoardsPageLocators.create_board_button).click()
