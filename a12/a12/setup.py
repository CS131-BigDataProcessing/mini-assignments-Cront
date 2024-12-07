from setuptools import setup, find_packages

setup(
    name="A12_package",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas>=2.2.3"],
    description="Assignment 12 package",
    author_email="syed.abidi@sjsu.edu",
    author="Syed Abidi",
)
