import boto3

def lambda_handler(event, context):
    # Replace 'your-bucket-name' with the name of your S3 bucket
    bucket_name = 'innovation101'
    file_name = 'to_be_upload.txt'
    # Create an S3 client
    s3 = boto3.client('s3')

    # List all objects in the bucket
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        for obj in response['Contents']:
            print(obj['Key'])
    except Exception as e:
        return f"Accessing S3 failed with error. {e}"

    # Upload a file to the bucket
    try:
        filename = file_name
        with open(filename, 'rb') as f:
            s3.upload_fileobj(f, bucket_name, filename)
    except Exception as e:
        return f"Upload file failed with error. {e}"

    # Download a file from the bucket
    try:
        object_key = file_name
        with open(object_key, 'wb') as f:
            s3.download_fileobj(bucket_name, object_key, f)
    except Exception as e:
        return f"Download file failed with error. {e}"