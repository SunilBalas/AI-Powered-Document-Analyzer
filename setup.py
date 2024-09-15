from setuptools import find_packages, setup
from typing import List

class Author:
    def __init__(self, name: str | None, email: str | None) -> None:
        self.name = name
        self.email = email

class ProjectSetup:
    def __init__(self) -> None:
        self.HYPHEN_E_DOT = '-e .'
        self.file_path = 'requirements.txt'
        self.project_name = 'Document Analyzer'
        self.version = '0.0.1'
        self.author = Author('SunilBalas', 'balassunil606@gmail.com')
    
    def get_long_description(self):
        with open("./README.md", "r", encoding="utf-8") as f:
            long_description = f.read()
        return long_description

    def get_requirements(self) -> List[str]:
        '''
        Retrieves a list of package requirements from a specified requirements file.

        Returns:
            List[str]: A list of package names and versions extracted from the requirements file.

        '''
        requirements = []
        with open(self.file_path) as file:
            requirements = file.readlines()
            requirements = [req.replace('\n', '') for req in requirements]
            
            if self.HYPHEN_E_DOT in requirements:
                requirements.remove(self.HYPHEN_E_DOT)
                
            return requirements
    
    def do_project_setup(self):
        setup(
            name=self.project_name,
            version=self.version,
            author=self.author.name,
            author_email=self.author.email,
            description="A small python package for fetching insights from the documents",
            long_description=self.get_long_description(),
            long_description_content_type='text/markdown',
            url=f"https://github.com/{self.author.name}/{self.project_name}",
            project_urls={
                "Bug Tracker": f"https://github.com/{self.author.name}/{self.project_name}/issues"
            },
            packages=find_packages(),
            install_requires=self.get_requirements()
        )

if __name__ == "__main__":
    # Instantiated Project Setup Class
    project_setup = ProjectSetup()
    
    # Project setup
    project_setup.do_project_setup()