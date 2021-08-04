

class MainPageLocators(object):
    # Input email address
    main_locator_login_button = "/html/body/header/nav/div/a[1]"
    login_user_id = "user"
    login_password = "//*[@id='password']"
    user_login_button = "//*[@id='login']"
    password_login_button = "//*[@id='login-submit']/span"

class WorkspaceLocators(object):
    create_workspace = "//*[@id='content']/div/div[2]/div/div[1]/div/div/div[1]/nav/div[2]/div/ul/li/button/span[2]"


class BoardsPageLocators(object):
    # open email form
    start_create_board = "//*[@id='content']/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li/div"
    title_xpath = "//*[@id='layer-manager-overlay']/div/div/div/div[1]/div/input"
    create_board_button = "//*[@id='layer-manager-overlay']/div/div/div/div[2]/div/button"

class SettingsLocators(object):
    workspace_settings = "//*[@id='content']/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/a[4]"

class DeletingLocators(object):
    delete_workspace = "//*[@id='content']/div[3]/div[3]/div[2]/div/div/div/div[2]/a/span"
    delete_forever = "//*[@id='chrome-container']/div[4]/div/div[2]/div/div/div/input"
