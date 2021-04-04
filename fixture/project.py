from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_project(self, project_data):
        wd = self.app.wd
        self.open_manage_section()
        self.fill_form(project_data)
        wd.find_element_by_css_selector("[type='submit']").click()

    def open_manage_section(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a i[class='fa fa-gears menu-icon']").click()
        wd.find_element_by_css_selector("ul[class='nav nav-tabs padding-18'] li:nth-child(3)").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form(self, project_data):
        wd = self.app.wd
        wd.find_element_by_css_selector("button[class='btn btn-primary btn-white btn-round']").click()
        self.type("name", project_data.name)
        self.type("description", project_data.description)

    def del_project(self, project):
        wd = self.app.wd
        self.open_manage_section()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]"% project.id).click()
        wd.find_element_by_css_selector("input[value='Удалить проект']").click()
        wd.find_element_by_css_selector("input[value='Удалить проект']").click()

