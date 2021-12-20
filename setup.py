from setuptools import setup, find_packages

with open('requirements.txt') as f:
    content = f.readlines()
    requirements = [x.strip() for x in content]

setup(name='test770',
      description="first package",
      packages=find_packages,
      requires=requirements,
      scripts=['scripts/batch-run'])
