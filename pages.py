from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPageLocators, BoardsPageLocators, SettingsLocators, DeletingLocators, WorkspaceLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_element_loc(self, path, method=By.XPATH, time=20):
        WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located((method, path)),
                                               message=f"Can't find element: {path}")


class MainPage(BasePage):
    """Home page action methods come here."""

    def trello_main(self):
        self.wait_element_loc(path = MainPageLocators.main_locator_login_button)
        self.driver.find_element_by_xpath(MainPageLocators.main_locator_login_button).click()

    def trello_login(self, user_email, password):
        enter_email = self.driver.find_element_by_id(MainPageLocators.login_user_id)
        ActionChains(self.driver).move_to_element(enter_email).send_keys(user_email).pause(3).perform()
        self.driver.find_element_by_xpath(MainPageLocators.user_login_button).click()
        enter_password = self.driver.find_element_by_xpath(MainPageLocators.login_password)
        ActionChains(self.driver).move_to_element(enter_password).send_keys(password).pause(3).perform()
        self.driver.find_element_by_xpath(MainPageLocators.password_login_button).click()
        print('Log in successful')

class BuildWorkspace(BasePage):
    def workspace_builder(self):
        self.driver.find_element_by_xpath(WorkspaceLocators.create_workspace).click()


class CreateABoard(BasePage):
    def create_a_board(self):
        self.driver.set_page_load_timeout(10)
        self.driver.find_element_by_xpath(BoardsPageLocators.start_create_board).click()

    def set_title(self, title):
        self.wait_element_loc(path = BoardsPageLocators.title_xpath)
        self.driver.find_element_by_xpath(BoardsPageLocators.title_xpath).send_keys(title)
        self.driver.find_element_by_xpath(BoardsPageLocators.create_board_button).click()

class DeleteWorkspace(BasePage):
    def delete_workspace(self):
        self.driver.find_element_by_xpath(SettingsLocators.workspace_settings).click()
        self.driver.find_element_by_xpath(DeletingLocators.delete_workspace).click()
        self.driver.find_element_by_xpath(DeletingLocators.delete_forever).click()