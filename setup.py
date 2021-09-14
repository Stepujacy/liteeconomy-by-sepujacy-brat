from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(name="lib_economy",
      version=VERSION,
      author='Stępujący brat#1017',
      author_email='x.higheconomy@gmail.com',
      license='A poo co to komu XD',
      description='Ekonomia na wysokim poziomie a tak seriop to gówno robione z nudów',
      packages=find_packages(),
      install_requires=['sqlite3', 'nextcord']
      )