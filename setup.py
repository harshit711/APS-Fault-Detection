'''
This is the file to create 'sensor' package
'''
from setuptools import find_packages, setup

def get_required_packages():
    '''
    This function returns the list of requirements
    '''
    # with open('requirements.txt', 'r') as f:
    #     required_packages = f.read().splitlines()
    # return required_packages

setup(
    name='sensor',
    version='0.0.1',
    author='Harshit Kumr Taneja',
    author_email='harshittaneja3@gmail.com',
    packages=find_packages(),
    install_requires=get_required_packages(),
)