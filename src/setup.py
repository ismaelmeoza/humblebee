#!/usr/bin/env python
#encoding:utf-8

from setuptools import setup

setup(
    name='humblebee',
    version='0.6',
    description='A scraper for TV shows.',
    author='Steinthor Palsson',
    author_email='steinitzu@gmail.com',
    url='https://github.com/steinitzu/romdb',
    license='MIT',

    include_package_data=True,
    
    packages=[
        'humblebee', 
        ],
    
    package_data = {'humblebee' : ['default.cfg', 'schema.sql']},
    
    entry_points={
        'console_scripts': [
            'humblebee = humblebee.cli:main'
            ]
        },    
    
    install_requires=[
        'httplib2', 
        'pyUnRAR2',
        'send2trash',
        'unidecode',
        'gnarlytvdb',
        'xmltodict',
        ]
    )
