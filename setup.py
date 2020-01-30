import os
from setuptools import setup, find_packages, Command
from pathlib import Path
import subprocess


class RccCommand(Command):
    description = "compile Qt resources"
    user_options = []

    def initialize_options(self):
        self.packages = []

    def finalize_options(self):
        pass

    def run(self):
        for package in self.packages:
            print(package)

        subprocess.run(['rcc', '-o', 'webviewer/resources.py', '-g', 'python', 'webviewer/resources.qrc'])


setup(name="webviewer",
      version="0.1",
      author="Lennart Husvogt",
      author_email="lennart@husvogt.net",
      url="https://github.com/LeAlex27/webviewer",
      packages=find_packages(),
      python_requires=">=3.7",
      install_requires=["PySide2"],
      cmdclass={'rcc': RccCommand})
