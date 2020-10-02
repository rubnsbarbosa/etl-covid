#!/usr/local/bin/python
import pandas as pd
from etl import extracting
from etl import transforming
from etl import loading

import ibm_boto3
import ibm_botocore.client
from config import cos_client


if __name__ == "__main__":

    df = extracting()
    data = transforming(df)

    dataset = pd.DataFrame()
    for idx, row in data.iterrows():
        dataset = dataset.append(row, ignore_index=True)
    # sava dataset in CSV file
    dataset.to_csv("covid.csv", index=False)

    loading(cos_client, 'event-bucket', 'covid.csv')