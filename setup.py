# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fMRI-Dynamic Network Animator',
    'author': 'Xiangzhen Kong',
    'url': 'http://bnucon.github.com/fMRI-DNA/',
    'download_url': 'https://github.com/bnucon/fMRI-DNA',
    'author_email': 'kongxiangzheng@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'fMRI-DNA'
}

setup(**config)
