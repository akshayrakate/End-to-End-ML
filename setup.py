from setuptools import setup, find_packages
from typing import List

# Requirements.txt will through error if we use hyphen variable
HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="akshay_first_project",
    version="0.0.1",
    author="akshay",
    packages=find_packages(),
    # we can define UDF for searching required packages
    requires=get_requirements('requirements.txt'),
)
