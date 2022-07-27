from setuptools import find_packages, setup

REQUIREMENTS_FILE = "requirements.txt"

with open(REQUIREMENTS_FILE, "r") as dependencies_file:
    DEPENDENCIES = dependencies_file.readlines()

setup(
    name="data-centric-ai",
    version="0.0.0",
    install_requires=DEPENDENCIES,
    packages=find_packages(),
    license='Apache License, Version 2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ben Epstein",
    author_email="ben.epstein97@gmail.com",
    description="A helper package for the requirements of the Data Centric AI Book",
    url="https://github.com/Ben-Epstein/dcai/"
)
