import boto3

rekg = boto3.client('rekognition', 'us-east-2' , aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,)   # provide access_key and secret_key

response = rekg.detect_faces(Image={
    "S3Object": {
        "Bucket": 's3_bucket',
        "Name": 'Images.jpg',
    }
},
                             Attributes=['ALL'],
                            )	# provide s3 bucket and image name in which operation is to be performed

for i in range(len(response['FaceDetails'])):
    print(f'Person {i}')
    print(f"\tAge Range: {response['FaceDetails'][i]['AgeRange']}")
    print(f"\tGender: {response['FaceDetails'][i]['Gender']['Value']}")
    print(f"\tGender: {response['FaceDetails'][i]['Beard']['Value']}")
    print(f"\tGender: {response['FaceDetails'][i]['Smile']['Value']}")