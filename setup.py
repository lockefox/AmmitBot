'''wheel setup for Prosper common utilities'''

from os import path, listdir
from sys import executable
from setuptools import setup, find_packages
import distutils.cmd
import subprocess

HERE = path.abspath(path.dirname(__file__))

class PyTest(distutils.cmd.Command):
    '''override `test` with pytest call
    (stolen from https://github.com/tomerfiliba/plumbum/blob/master/setup.py)'''
    #user_options = [('cov', 'c', 'Produce coverage'),
    #                ('report', 'r', 'Produce html coverage report')]

    def initialize_options(self):
        #self.cov = None
        #self.report = None
        pass
    def finalize_options(self):
        pass
    def run(self):
        #import sys, subprocess
        proc = [executable, '-m', 'pytest', 'tests/']
        #if self.cov or self.report:
        #    proc += ['--cov','--cov-config=.coveragerc']
        #if self.report:
        #    proc += ['--cov-report=html']
        errno = subprocess.call(proc)
        raise SystemExit(errno)

def include_all_subfiles(path_included):
    '''for data_files {path_included}/*'''
    local_path = path.join(HERE, path_included)
    file_list = []

    for file in listdir(local_path):
        file_list.append(path_included + '/' + file)

    return file_list

setup(
    name='AmmitBot',
    author='John Purcell',
    author_email='jpurcell.ee@gmail.com',
    url='https://github.com/lockefox/AmmitBot',
    download_url=None, #TODO
    version='0.0.1',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    keywords='discord nltk moderation chat community management',
    packages=find_packages(),
    data_files=[
        #TODO: license + README
        ('test', include_all_subfiles('test')),
        ('docs', include_all_subfiles('docs'))
    ],
    package_data={
        'ammit':[
            'ammit_config.cfg'
        ]
    },
    install_requires=[
        'aiohttp==1.0.5',
        'async-timeout==1.1.0',
        'chardet==2.3.0',
        'colorama==0.3.7',
        'discord.py==0.13.0',
        'multidict==2.1.2',
        'nltk==3.2.1',
        'numpy==1.11.2',
        'pandas==0.19.0',
        'py==1.4.31',
        'pymongo==3.3.0',
        'pytest==3.0.3',
        'python-dateutil==2.5.3',
        'pytz==2016.7',
        'requests==2.11.1',
        'six==1.10.0',
        'tinydb==3.2.1',
        'tinymongo==0.1',
        'ujson==1.35',
        'websockets==3.2'
    ],
    cmdclass={
        'test':PyTest
    }
)
