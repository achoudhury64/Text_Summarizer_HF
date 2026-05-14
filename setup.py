"""
The setup.py file serves as the packaging configuration for your Python project. Its main purposes are:

Package Installation & Distribution

Defines metadata about your project (name, version, author, description)
Specifies how to install your project as a Python package
Enables installation via pip install -e . for development mode
Key Functions in Your File:

Metadata definition: Sets project name (textSummarizer), version, author info, and description
Package discovery: Uses setuptools.find_packages(where="src") to automatically find all packages in the src directory
Directory structure: package_dir={"": "src"} tells Python that packages are located in the src folder
README integration: Reads README.md for the long description shown on PyPI
Repository links: Provides GitHub repository and issue tracker URLs

"""
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-HF"
AUTHOR_USER_NAME = "achoudhury64"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "achoudhury64@gatech.edu"


#This is a call to the setuptools.setup() function, which configures how your Python package is built and installed.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app using HuggingFace transformers",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

#basically it will look for the __init__.py constructor file in every folder and subfolder and include them in the package/src folder.