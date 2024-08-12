# My first Python library

Loading function
ft_tqdm - reproduce tqdm in my own style.

pip3 install ./dist/ft_package-0.0.1.tar.gz
or 
pip3 install ./dist/ft_package-0.0.1-py3-none-any.whl

to check the installation
pip3 show -v ft_package

To create library
pip3 install wheel
python3 setup.py sdist bdist_wheel

in setup.py
from setuptools import setup, find_packages

setup(
    name = "ft_package",
    version = "0.0.1",
    author="TomTris",
    author_email="quoctrido.jb@gmail.com",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TomTris/42-Python-0-Starting",
    license="MIT",
    packages=find_packages(),
	classifiers=[
		"Programing Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Ondependent",
    ],
	python_requires='>=3.9'
)

