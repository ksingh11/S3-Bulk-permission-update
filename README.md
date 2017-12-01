# S3 Bulk permission update
Update file permissions on S3, when they are too many in numbers. Also, the script is very easy to make modifications according to your need.

Detailed documentation on S3: [Amazon S3 (BOTO3)](http://boto3.readthedocs.io/en/latest/guide/migrations3.html)


## Configure:
> Please edit conf.py before moving forward.
> 
> To iterate all buckets set AWS_STORAGE_BUCKET_NAME = None, otherwise specify bucket name.

## Installation:
```shell
$ git clone git@github.com:ksingh11/S3-Bulk-permission-update.git
$ cd cd S3-Bulk-permission-update/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python script.py
```
