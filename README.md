PyPiS3
======

PyPiS3 is a fork of [S3PyPI](https://github.com/novemberfiveco/s3pypi) is a CLI tool for creating a Python Package Repository in an S3 bucket, adapted for use as a private PyPi repository entirely backed by S3 storage.


Installation
------------

Install the latest version:

```bash
pip install --upgrade pypis3
```

Install the development version:

```bash
git clone -b develop git@github.com:jamiecressey/pypis3.git
cd pypis3/ && sudo pip install -e .
```


Setting up S3 and S3Auth
----------------------------

Before you can start using ``pypis3``, you must set up a S3Auth enabled bucket. Following the steps on their website: http://www.s3auth.com/

Distributing packages
---------------------

You can now use ``pypis3`` to create Python packages and upload them to your S3 bucket:

```bash
cd /path/to/your/awesome-project/
pypis3 --bucket mybucket --url pypi.example.com
```


Installing packages
-------------------

Install your packages using ``pip`` by pointing the ``--extra-index-url`` to your S3Auth enabled bucket:

```bash
pip install --upgrade awesome-project --extra-index-url http://pypi.example.com/
```

Alternatively, you can configure the index URL in ``~/.pip/pip.conf``:

```
[global]
extra-index-url = http://pypi.example.com
```

