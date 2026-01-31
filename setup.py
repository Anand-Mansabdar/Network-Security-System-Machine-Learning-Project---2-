# This file is required because its an essential part for packaging and distriibuting python projects. It is used by setup tools to define the configuration of your project, such as metadata, dependencies and more....

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
  # This function will return the list of requirements
  requirement_list: List[str] = []

  try:
    with open('requirements.txt', 'r') as file:
      # Read lines from file
      lines = file.readlines()
      
      for line in lines:
        requirement = line.strip()
        
        # Ignore empty lines and -e.
        if requirement and requirement != "-e .":
          requirement_list.append(requirement)
  except FileNotFoundError:
    print("Files could not fe fetched.")

  return requirement_list

# print(get_requirements())

setup(
  name="Network Security System - ML Project",
  version= "0.0.1",
  author= "Anand Mansabdar",
  author_email= "anandmansabdar.study@gmail.com",
  packages=find_packages(),
  install_requires= get_requirements()
)