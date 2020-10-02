#!/usr/local/bin/python
import os
import sys
import json
import logging
import requests
import pandas as pd

logging.basicConfig(stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
logger = logging.getLogger(__name__)


def extracting():
    logger.info('EXTRACTING...')
    # extract data from API
    url = 'https://indicadores.integrasus.saude.ce.gov.br/api/casos-coronavirus'
    req = requests.get(url)
    data = req.json()
    df = pd.DataFrame(data)
    return df

def transforming(df):
    logger.info('TRANSFORMING...')
    logger.info('REMOVING COLUMNS')
    list_drop_columns = ['estadoPaciente', 'codigoMunicipioPaciente', 'dataNotificacao', 'bairroPaciente', 'dataColetaExame',
    'dataResultadoExame', 'resultadoFinalExame', 'dataSolicitacaoExame', 'dataObito', 'obitoConfirmado', 'paisPaciente']
    df.drop(list_drop_columns, axis=1, inplace=True)

    logger.info('SORTING THE DATE IN ASCENDING ORDER')
    df_covid = df.sort_values(['dataInicioSintomas'], ascending=[1])

    logger.info('NORMALIZING THE DATE')
    df_covid['dataInicioSintomas'] = pd.to_datetime(df_covid['dataInicioSintomas'], utc=False)
    df_covid['dataInicioSintomas'] = df_covid['dataInicioSintomas'].dt.date
    print(df_covid[:5])

    logger.info('RETURN DATASET')
    return df_covid[:50]

def loading(cos, bucket_name, filename):
    logger.info('UPLOADING {} TO IBM BUCKET {}...'.format(filename, bucket_name))
    try:
        cos.upload_file(Filename=filename, Bucket=bucket_name, Key=os.path.basename(filename))
        logger.info('UPLOAD COMPLETED')
    except Exception as e:
        logger.error("UPLOAD FAILED")
        logger.exception(e)
