from br.com.domingos.juan.utils.spark_utils import SparkUtils
from br.com.domingos.juan.database.biquery_manager import BigQueryManager
from br.com.domingos.juan.constants.parameters import Parameter as pn

from pyspark.sql import SparkSession 

class ApplicationEntry:

    def __init__(self, parameters):

        self.__SPARK_UTILS = SparkUtils()
        self.__SPARK = self.__SPARK_UTILS.get_spark_session(parameters)
        self.__BQM = BigQueryManager()
        self.__LAKE_PATH = parameters.get(pn.LAKE_PATH)
        self.__TARGET_PATH = parameters.get(pn.TARGET_PATH)

        pass

    def target_path(self)-> str:
        return self.__TARGET_PATH

    def lake_path(self) -> str:
        return self.__LAKE_PATH

    def spark(self) -> SparkSession:
        return self.__SPARK

    def bqm(self) -> BigQueryManager:
        return self.__BQM