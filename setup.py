from setuptools import setup

import journal


setup(
    name = 'journal',
    packages = ['journal'],
    description = 'Maintain and review a log of your activities.',
    version = journal.__version__,
    author = 'Ted Stein',
    author_email = 'karamarisan@gmail.com',
    entry_points = {
      'console_scripts': [
        'journal = journal:entry'
      ]
    }
)

