import boto3

# s3 = boto3.client('s3',region_name='us-east-1')
# s3.create_bucket(Bucket='yshit')
#
# s3 = boto3.resource('s3')
# bucket = s3.Bucket('yshit')
# response = bucket.delete()

# s3 = boto3.client('s3')
# resp = s3.list_buckets()
# print (resp)

def startInstances():
    client = boto3.client('ec2')
    resp = client.start_instances(InstanceIds = ["i-0167c661af5ac8cbb","i-0e5e327f56acf3f69",'i-008c5265be32bb4e8'])
    print (resp)
    return (resp)

def stopInstances():
    client = boto3.client('ec2')
    resp = client.stop_instances(InstanceIds =['i-0e5e327f56acf3f69','i-0167c661af5ac8cbb','i-008c5265be32bb4e8'] )
    print (resp)

stopInstances()