#!/usr/local/bin/python
import os
import sys
import json
import logging
import datetime
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