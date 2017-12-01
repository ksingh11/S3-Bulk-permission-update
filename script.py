import ConfigParser
import os

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from conf import *

# Initialize S3
s3 = boto3.resource('s3',
                    region_name=AWS_S3_REGION_NAME,
                    aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY,
                    config=Config(signature_version='s3v4'))

# get buckets to be operated on
bucket_name = AWS_STORAGE_BUCKET_NAME
bucket_list = []
if bucket_name:
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        bucket = s3.Bucket(bucket_name)
        bucket_list.append(bucket)
    except ClientError as e:
        print(e.message)
        exit()
else:
    bucket_list = s3.buckets.all()


# Iterate over all the buckets: only one bucket if name is provided
for bucket in bucket_list:
    for key in bucket.objects.all():
        # print('%s: %s' % (key.key, key.Acl().grants))
        key.Acl().put(ACL=NEW_ACL)



