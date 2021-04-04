

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        # Logout
        wd = self.app.wd
        wd.find_element_by_css_selector("[class='user-info']").click()
        wd.find_element_by_css_selector("a i[class='fa fa-sign-out ace-icon']").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def login(self, username, password):
        # Log in
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_css_selector("[type='submit']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("[type='submit']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        list = wd.find_elements_by_xpath("// a[contains( @ href, 'logout_page')]")
        x = len(list) > 0
        return x

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("ul[class='breadcrumb'] li a").text




