import oci
import json
import logging
import io
from datetime import datetime
from fdk import respons
from oci.config import from_file

def handler(ctx, data: io.BytesIO = None):
    body=dict()
    try:
        logging.getLogger().info(data)
        body = json.loads(data.getvalue())
        logging.getLogger().info(body)
        eventData = body["data"]["additionalDetails"]
        publicAccessType=eventData["publicAccessType"]
        namespace= eventData["namespace"]
        bucketName= eventData["bucketName"]
        if publicAccessType!='NoPublicAccess' :
            UpdateBucketDetails = oci.object_storage.models.UpdateBucketDetails(public_access_type= 'NoPublicAccess')
            response= storageClient.update_bucket(namespace, bucketName, UpdateBucketDetails)
            print(response)
