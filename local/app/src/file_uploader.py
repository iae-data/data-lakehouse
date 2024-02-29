from minio import Minio
from minio.error import S3Error


class FileUploader:
    def __init__(self, endpoint, access_key, secret_key, bucket_name):
        self.minio_client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=False
        )
        self.bucket_name = bucket_name

    def upload(self, file_path, object_name):
        try:
            self.minio_client.fput_object(
                bucket_name=self.bucket_name,
                object_name=object_name,
                file_path=file_path
            )
        except S3Error as e:
            print(e)
