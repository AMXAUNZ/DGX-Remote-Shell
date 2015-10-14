try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jim Maciejewski',
    'url': 'http://ornear.com/MyProject',
    'download_url': 'http://ornear.com/MyProject/Download',
    'author_email': 'itsmagic_software@ornear.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
