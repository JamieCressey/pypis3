from setuptools import setup, find_packages

from pypis3 import __prog__, __version__


setup(
    name=__prog__,
    version=__version__,

    description='CLI tool for creating a private Python Package Repository backed entirely by AWS S3 storage',

    author='Jamie Cressey',
    author_email='jamiecressey89@gmail.com',
    url='https://github.com/JamieCressey/pypis3',
    download_url='https://github.com/jamiecressey/pypis3/tarball/' + __version__,

    packages=find_packages(),
    package_data={__prog__: ['templates/*.j2']},

    install_requires=['boto3', 'Jinja2', 'wheel'],
    entry_points={'console_scripts': ['{0}={0}.cli:main'.format(__prog__)]},
)
