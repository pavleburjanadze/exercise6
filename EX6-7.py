import boto3

ec2 = boto3.resource('ec2')

vpc = ec2.create_vpc(CidrBlock='10.16.0.0/16')


vpc.create_tags(Tags=[{"Key": "Name", "Value": "btu_vpc"}])

internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)




