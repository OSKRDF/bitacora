import boto3
from keys import ACCESS_KEY, SECRET_KEY
bucket_name = "bucket-bitacora"


def connectionS3():
    session_aws = boto3.Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print(session_s3)
    return session_s3

#connectionS3()

    
def get_file(session_s3): 
    bucket_project = session_s3.Bucket(bucket_name)
    bucket_objects = bucket_project.objects.all()
    for obj in bucket_objects:
       print(obj.key)
    print(bucket_objects)

#get_file()



def save_file(code,photo):
    ext = photo.filename.split(".")[1]
    photo_name = code + "." + ext
    photo_path = "/tmp/" + photo_name
    photo.save(photo_path)
    print("photo saved")
    return photo_path, photo_name

def upload_file_s3(session_s3, photo_path, photoName):
    image_photo_s3 = "bitacora/" + photoName
    session_s3.meta.client.upload_file(photo_path, bucket_name, image_photo_s3 )
    print("photo subida")
    #s3.upload_file()
 