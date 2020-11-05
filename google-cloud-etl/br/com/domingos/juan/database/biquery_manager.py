import logging
import os

from google.cloud import bigquery

class BigQueryManager:

    def __init__(self, dataset = "gcp-data-load", append = True):
        self.__setup()

        self.__LOG = logging.getLogger("BigQueryManager")
        self.__CLIENT = bigquery.Client()
        self.__JOB_CONFIG = bigquery.LoadJobConfig()
        self.__DATASET = self.__CLIENT.dataset(dataset)

        self.__JOB_CONFIG.source_format = bigquery.SourceFormat.PARQUET

        if(append):
            self.__JOB_CONFIG.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        else:
            self.__JOB_CONFIG.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

        pass


    def write(self, table, uri):
        self.__LOG.info("Writing data into {}".format(table))

        job = self.__CLIENT.load_table_from_uri(
            uri, 
            self.__DATASET.table(table), 
            job_config = self.__JOB_CONFIG)
        
        print(f"Submmited JOB ID:${job.job_id}")

        job.result()

    def __setup(self):
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
        pass