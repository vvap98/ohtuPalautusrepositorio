from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = tomli.loads(content)

        project = toml_dict["project"]
        name = project["name"]
        description = project["description"]
        dependencies = project["dependencies"]
        dev_dependencies = toml_dict["dependency-groups"]["dev"]
        licence = project["licence"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
