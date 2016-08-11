try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'lexicon',
    'author': 'Eric Yeh',
    'url': 'http://www.ericyeh.me',
    'download_url': 'Where to download it.',
    'author_email': 'ericyeh1995@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
