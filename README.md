# S3 Bulk permission update
Update file permissions on S3, when they are too many in numbers. Also, the script is very easy to make modifications according to your need.

Detailed documentation on S3: [Amazon S3 (BOTO3)](http://boto3.readthedocs.io/en/latest/guide/migrations3.html)


## Get access key and secret:
> Create a new AMI user on AWS console, and grant **Programmatic Access** to the user.
>
> Attach policy **AmazonS3FullAccess**, from the section __'Attach existing policies directly'__.
>
> Get **Access key ID** and **Secret access key**, to be used in script.

## Configure:
> Please edit conf.py before moving forward.
> 
> To iterate all buckets set AWS_STORAGE_BUCKET_NAME = None, otherwise specify the particular bucket name to be modified.

## Installation:
```shell
$ git clone git@github.com:ksingh11/S3-Bulk-permission-update.git
$ cd S3-Bulk-permission-update/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python script.py
```
