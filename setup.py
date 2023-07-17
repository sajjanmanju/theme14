from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in theme14/__init__.py
from theme14 import __version__ as version

setup(
	name="theme14",
	version=version,
	description="Theme for V14",
	author="Manju Sajjan",
	author_email="mgsajjan1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
