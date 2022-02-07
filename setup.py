import subprocess
from setuptools import setup, find_packages

from webviewer import __version__


setup(name="webviewer",
      version=__version__,
      author="Lennart Husvogt",
      author_email="lennart@husvogt.net",
      url="https://github.com/LeAlex27/webviewer",
      packages=find_packages(),
      python_requires=">=3.7",
      install_requires=["PySide6>=6.2"])
