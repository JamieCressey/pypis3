import os

import boto3

from pypis3.package import Index

__author__ = 'Jamie Cressey'
__copyright__ = 'Copyright 2016, Jamie Cressey'
__license__ = 'MIT'


class S3Storage(object):
    """Abstraction for storing package archives and index files in an S3 bucket."""

    def __init__(self, bucket, url=None):
        self.s3 = boto3.client('s3')
        self.bucket = bucket

        self.url = url

    def _key(self, package, filename):
        path = '%s/%s' % (package.name, filename)
        return self.s3.get_object(
            Bucket=self.bucket,
            Key=path)

    def get_index(self, package):
        try:
            html = self._key(package, 'index.html')['Body']
            return Index.parse(self.url, html)
        except Exception:
            return Index(self.url, [])

    def put_index(self, package, index):
        self.s3.put_object(
            ACL='private',
            Body=index.to_html(),
            Bucket=self.bucket,
            ContentType='text/html',
            Key='{}/{}'.format(package.name, 'index.html')
        )

    def put_package(self, package):
        for filename in package.files:
            self.s3.put_object(
                ACL='private',
                Body=os.path.join('dist', filename),
                Bucket=self.bucket,
                ContentType='application/x-gzip',
                Key='{}/{}'.format(package.name, filename)
            )
