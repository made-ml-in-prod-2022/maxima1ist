from setuptools import find_packages, setup


with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="ml_project",
    packages=find_packages(),
    version="0.1.0",
    description="It's fully \"production ready\" project for solution of classification problem.",
    author="maxima1ist",
    install_requires=required,
)
