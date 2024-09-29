#This file is used to treat local folders as packages so that it can be accesed in another files.

from setuptools import find_packages, setup

setup(
    name = "Generative AI based Recruitment Project",
    version = '0.0.0',
    author = 'Huzaifa',
    author_email = 'azharhuzaifa123@gmail.com',
    packages = find_packages(),
    install_requires = []
)