import os

AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

def connect():
    if not AWS_SECRET_KEY:
        raise EnvironmentError("AWS_SECRET_KEY environment variable is not set")
    print(f"Connecting with: {AWS_SECRET_KEY}")
