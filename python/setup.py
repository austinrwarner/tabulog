from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='tabulog',
      version='0.1.1',
      description='Parsing Semi-Structured Log Files into Tabular Format',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/austinnar/tabulog',
      author='Austin Nar',
      author_email='austin.nar@gmail.com',
      license='MIT',
      packages=['tabulog'],
      install_requires=['PyYAML', 'pandas']
      )
