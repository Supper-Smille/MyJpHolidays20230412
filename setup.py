from setuptools import setup, find_packages

DESCRIPTION = "MyJpHolidays: You get a combined list of Japan-Holidays. You can customize orignal holidays used ini-file."
NAME = 'MyJpHolidays'
AUTHOR = 'Supper-Smille'
# AUTHOR_EMAIL = 
# URL = 
LICENSE = 'MIT License'
# DOWNLOAD_URL = 
VERSION = '0.8.0'
PYTHON_REQUIRES = ">=3.8.10"

INSTALL_REQUIRES = [
    'numpy >=1.23.1', 
    're>=2.2.1'
]

setup(
    name='MyJpHolidays',
    version='0.8.0',
    packages=find_packages()
)
