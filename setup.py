from setuptools import find_packages, setup
from typing import List

HYPHEN_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requiremnts:

    """
    requirements = []
    with open(file_path) as file_obj:
        requiremnts = file_obj.readlines()
        requirements= [req.replace('\n',' ') for req in requirements]
         
        if HYPHEN_E in requirements:
            requirements. remove(HYPHEN_E)

    return requirements  

setup(
name = 'address_detection_2025_end_to_end',
version = '0.0.1',
author = 'Sushil',
author_email = 'sushildev0818@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
