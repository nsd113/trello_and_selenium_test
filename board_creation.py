import unittest
#import system_settings
from system_settings import path
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException
import os
from selenium import webdriver
import pages

load_dotenv()  # looks for a . env file and load the environment variables and make them accessible to the project
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
board_title = os.getenv('BOARD_TITLE')
#email = "test4203@mail.ru"
#password = "Gy[Qu$j$!R8e)w5"
#board_title = "This is first board"

class TrelloTestOnePlentific(unittest.TestCase):
    """Test for the public Trello APIActions/steps to be covered:
    ● Create a board
    ● Create 3 cards on that board
    ● Edit one of the cards
    ● Delete one of the cards
    ● Add a comment to one of the cards"""


    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(path, options=self.chrome_options)
        #self.driver = webdriver.Chrome(os.getcwd() + '/chromedriver', options=self.chrome_options)
        #self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)

        try:
            self.driver.get("https://trello.com/")
            print("URL successfully Accessed")
            self.driver.maximize_window()
        except TimeoutException:
            print("Page load Timeout Occurred. Quiting !!!")
            self.driver.quit()

    def test_trello_board_creation(self):
        """Sends the letter from test account on mail.ru."""
        # login to main page
        login_page = pages.MainPage(self.driver)
        login_page.trello_main()
        login_page.trello_login(user_email=email, password=password)

        #
        first_board=pages.CreateABoard(self.driver)
        first_board.create_a_board(board_title)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
