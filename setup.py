from setuptools import setup, find_packages
import sys, os

version = '0.3'

setup(name='opengraph',
      version=version,
      description="A module to parse the Open Graph Protocol",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='opengraph protocol',
      author='Erik Rivera',
      author_email='erik@rivera.com',
      url='http://rivera.pro',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'BeautifulSoup'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
