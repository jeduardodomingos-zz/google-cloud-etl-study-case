from br.com.domingos.juan.utils.parameter_manager import ParameterManager
from br.com.domingos.juan.constants.parameters import Parameter as pn

from pyspark.sql import SparkSession
from datetime import datetime

class SparkUtils:

    def get_spark_session(self, parameters: ParameterManager) -> SparkSession:
        app_name = f"GoogleCloudIngestor{parameters.get(pn.APP_NAME)}"

        return SparkSession.builder.master("yarn")    \
                                   .appName(app_name) \
                                   .getOrCreate()