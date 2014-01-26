import boto
import boto.s3
s3conn=boto.connect_s3()
bucket=s3conn.create_bucket('iamroletest')
from boto.s3.key import Key
k=Key(bucket)
k.key='foobar'
k.set_contents_from_string('This is IAM Role Demo')
text=k.get_contents_as_string()
print(text)
