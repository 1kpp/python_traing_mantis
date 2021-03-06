from model.project import Project


def test_add_project(app, json_projects):
    old_list_of_projects = app.soap.get_projects_list()
    project_data = json_projects
    app.project.add_project(project_data)
    new_list_of_projects = app.soap.get_projects_list()
    old_list_of_projects.append(project_data)
    assert sorted(old_list_of_projects, key=Project.max_id) == sorted(new_list_of_projects, key=Project.max_id)
