import boto
s3conn=boto.connect_s3()
full_bucket=s3conn.get_bucket('iamroletest')
for key in full_bucket.list():
	key.delete()
	
res=s3conn.delete_bucket('iamroletest')
print("Bucket delete")
