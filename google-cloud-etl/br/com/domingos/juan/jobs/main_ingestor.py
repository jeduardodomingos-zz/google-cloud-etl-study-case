
import os
import logging
import sys

from br.com.domingos.juan.utils.parameter_manager import ParameterManager
from br.com.domingos.juan.utils.application_entry import ApplicationEntry
from br.com.domingos.juan.processors.bill_of_material_processor import BillOfMaterialsProcessor
from br.com.domingos.juan.processors.comp_boss_processor import CompBossProcessor
from br.com.domingos.juan.processors.price_quote_processor import PriceQuoteProcessor

from pyspark.sql import SparkSession

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

__LOG = logging.getLogger("BigqueryIngestor")


def process(application_entry):
    __LOG.info("Starting Bigquery ingestor processor.")

    processors = get_processors(application_entry)

    for processor in processors:
        processor.build()

    __LOG.info("Finishing Bigquery ingestor processor.")

    pass

def get_processors(application_entry):
    return [
        BillOfMaterialsProcessor(application_entry),
        CompBossProcessor(application_entry),
        PriceQuoteProcessor(application_entry)        
    ]

if __name__ == "__init__":

    args = sys.argv[1:]
    parameters = ParameterManager(args)
    application_entry = ApplicationEntry(parameters)

    process(application_entry)
    
