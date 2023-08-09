import boto3


def aws_session(**kwargs):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client
    return boto3.session.Session(**kwargs)


def iam_client(**kwargs):
    return aws_session(**kwargs).client(service_name="iam")


def ec2_client(**kwargs):
    return aws_session(**kwargs).client(service_name="ec2")


def s3_client(**kwargs):
    return aws_session(**kwargs).client(service_name="s3")


def rds_client(**kwargs):
    return aws_session(**kwargs).client(service_name="rds")
