from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl#op.idp643324792")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        list = []
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl#op.idp643324792")
        try:
            raw_data = client.service.mc_projects_get_user_accessible(self.app.config['web']['username'], self.app.config['web']['password'])
            for row in raw_data:
                id = row["id"]
                name = row["name"]
                description = row["description"]
                list.append(Project(id=id, name=name, description=description))
            return list
        except WebFault:
            return False

