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
            response= storageClient.update_bucket(namespace, bucketName, UpdateBucketDetails)
            print(response)
