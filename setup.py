# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.1'

setup(name='cmsplugin-news',
      version=version,
      description="A news application which is pluggable into django-cms",
      keywords='django cms news',
      author='Harro van der Klauw',
      url='https://bitbucket.org/MrOxiMoron/cmsplugin-news',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      )
