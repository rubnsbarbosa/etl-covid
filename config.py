#!/usr/local/bin/python
import ibm_boto3
import ibm_botocore.client
from cos_config import cos

# Create Cloud Object Storage Client
cos_client = ibm_boto3.client("s3",
    ibm_api_key_id=cos["apikey"],
    ibm_service_instance_id=cos["iam_serviceid_crn"],
    ibm_auth_endpoint = cos["ibm_auth_endpoint"],
    config=ibm_botocore.client.Config(signature_version="oauth"),
    endpoint_url=cos["endpoints"]
)