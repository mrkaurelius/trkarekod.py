from setuptools import setup
from setuptools import find_packages

setup(
    name='trkarekod',
    version='0.1.0',
    author_email='abdulhamit.kumru@gmail.com',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'trkarekod = trkarekod.trkarekod_cli:main'
        ]
    }
)