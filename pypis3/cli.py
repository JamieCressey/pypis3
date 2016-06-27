#!/usr/bin/env python
import argparse

from pypis3 import __prog__, __version__
from pypis3.package import Package
from pypis3.storage import S3Storage

__author__ = 'Jamie Cressey'
__copyright__ = 'Copyright 2016, Jamie Cressey'
__license__ = 'MIT'


def main():
    p = argparse.ArgumentParser(prog=__prog__, version=__version__)
    p.add_argument('--bucket', required=True, help='S3 bucket')
    p.add_argument('--url', help='Custom URL', default=None)
    p.add_argument(
        '--no-wheel',
        dest='wheel',
        action='store_false',
        help='Skip wheel distribution')
    args = p.parse_args()

    package = Package.create(args.wheel)
    storage = S3Storage(args.bucket, args.url)

    index = storage.get_index(package)
    index.packages.discard(package)
    index.packages.add(package)

    storage.put_package(package)
    storage.put_index(package, index)


if __name__ == '__main__':
    main()
