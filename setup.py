import subprocess
from setuptools import setup, find_packages, Command

from webviewer import __version__


class RccCommand(Command):
    description = "compile Qt resources"
    user_options = []

    def initialize_options(self):
        # todo: clean this up
        # self.packages = []
        pass

    def finalize_options(self):
        pass

    def run(self):
        # for package in self.packages:
        #    print(package)

        subprocess.run(['rcc', '-o', 'webviewer/resources.py', '-g', 'python', 'webviewer/resources.qrc'])


setup(name="webviewer",
      version=__version__,
      author="Lennart Husvogt",
      author_email="lennart@husvogt.net",
      url="https://github.com/LeAlex27/webviewer",
      packages=find_packages(),
      python_requires=">=3.7",
      install_requires=["PySide2>=5.14"],
      cmdclass={'rcc': RccCommand})
