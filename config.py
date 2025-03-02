import boto3


AWS_ACCESS_KEY = "AKIAUQ4L3EW5FZRLYEHK"
AWS_SECRET_KEY = "kyU85vhCdPfB3dd1o9pz+/umroNu5sqG42ezoo5E"

# Update the region to match your S3 bucket's region: "eu-north-1"


S3_BUCKET_NAME = "smartphotoeventretrieval"

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="eu-north-1"
)
