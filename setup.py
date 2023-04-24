from setuptools import find_packages,setup
from typing import List

constant_e='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if constant_e in requirements:
            requirements.remove(constant_e)

setup(
    name='mlproj',
    version='0.0.1',
    author='Tharun',
    author_email='iamtharun18@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') #reduce the work & space we store it in that

)
