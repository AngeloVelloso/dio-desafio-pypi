from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

#with open("requirements.txt") as f:
#    requirements = f.read().splitlines()

setup(
    name="get_table_sped",
    version="0.0.1",
    author="angelo velloso",
    author_email="vellosov@hotmail.com",
    description="Package to download SPED tables",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AngeloVelloso/dio-desafio-pypi",
    packages=find_packages(),
    install_requires=['mechanize', 'pandas'],
    python_requires='>=3.8',
)