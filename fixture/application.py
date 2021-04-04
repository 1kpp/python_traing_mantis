from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:
    def __init__(self, browser, base_url, password):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'edge':
            self.wd = webdriver.Edge()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s % browser")
        self.wd.implicitly_wait(2)
        self.project = ProjectHelper(self)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.password = password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
