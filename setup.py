from setuptools import setup, find_packages

setup(name="webviewer",
      version="0.1",
      author="Lennart Husvogt",
      author_email="lennart@husvogt.net",
      url="https://github.com/LeAlex27/webviewer",
      packages=find_packages(),
      python_requires=">=3.7",
      install_requires=["PySide2"])
