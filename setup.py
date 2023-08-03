import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_NAME = "Ritu000addy"
SRC_REPO = "cnnCLASSIFIER"
AUTHOR_EMAIL = "addy.rituparna@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A package for CNN app",
    long_description= long_description,
    long_description_content= "text/markdown",
    url= f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where="src")
)