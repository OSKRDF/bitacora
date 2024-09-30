import boto3
import keys import ACCES_KEY, SECRET_KEY


def connectionS3():
    session_aws = boto3.session(ACCES_KEY,SECRET_KEY)
    print(session_aws)

connectionS3()