try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Exercise 47',
  'author': 'Jonathan Hartford',
  'url': 'URL to get it at.',
  'download_url': 'Where to download it.',
  'author_email': 'jon@outland.net',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['ex47'],
  'scripts': [],
  'name': 'ex47'
}

setup(**config)
