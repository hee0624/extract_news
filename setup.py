from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='extract_news',
      version=version,
      description="Python package to parse news from various news website",
      long_description="""\
Python package to parse news from various news website.We can get news content, news public time and news public source by this tool.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='news extract parser article',
      author='chenhe',
      author_email='hee0624@163.com',
      url='https://hee0624.github.io/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'beautifulsoup4==4.6.0',
            'bs4==0.0.1',
            'chardet==3.0.4',
            'fake-useragent==0.1.10',
            'jieba==0.39',
            'lxml==4.2.0',
            'wincertstore==0.2'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
