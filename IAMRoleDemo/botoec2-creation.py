import boto.ec2
conn=boto.ec2.connect_to_region('ap-southeast-1')
conn.run_instances('ami-c2e9a790',key_name='snehangshu',instance_type='t1.micro',security_groups=['allssh'])
