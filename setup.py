from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()
    
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
    
setup(
    name = 'image_processing',
    version= '0.0.1',
    author = 'Leonardo',
    description='image processing code for dio exercise',
    packages= find_packages()
)