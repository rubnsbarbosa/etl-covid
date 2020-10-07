# ETL Pipeline Covid-19

This repository is about an ETL (Extract, Transform and Load) of coronavirus data, referring to the state of Ceará and it's also part of hacktoberfest an open source software celebration you can read more about it: hacktoberfest.digitalocean.com.

## Public API

Extract data from a public API called IntegraSUS.

![ce-SUS](https://user-images.githubusercontent.com/17646546/83458857-a49c0180-a439-11ea-9f60-8ca994680a22.png)

### Method GET

> GET https://indicadores.integrasus.saude.ce.gov.br/api/casos-coronavirus

## Quick Usage

### Requirements

```bash
$ pip install -r requirements.txt
```

### Docker Build

Build an image called **etl-covid**:

```bash
$ docker build -t etl-covid .
```

### Docker Run

Run the image **etl-covid**:

```bash
$ docker run etl-covid
```

## Features

* Extract data from a public API;
* Transform data;
* Load to IBM Bucket.
