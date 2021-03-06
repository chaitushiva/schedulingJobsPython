from collections import defaultdict
import boto3
""" 
A tool for retrieving basic information from the running EC2 instances. 
"""
client = boto3.client('ec2')
regions = client.describe_regions()['Regions']
for region in regions:
     region_name=region['RegionName']
# Connect to EC2
for region in regions:
 print("below are the instances running in")
 region_name=region['RegionName']
 print(region_name)
 ec2 = boto3.resource('ec2',region_name=region['RegionName'])
# Get information for all running instances
 running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])
 print (running_instances)
 ec2info = defaultdict()
 for instance in running_instances:
    print (instance.id)
    print (instance.tags)
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time
        }
 attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
 for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")
