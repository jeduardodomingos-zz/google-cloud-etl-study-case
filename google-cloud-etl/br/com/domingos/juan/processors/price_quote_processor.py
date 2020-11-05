class PriceQuoteProcessor:

    def __init__(self, application_entry):
        self.__APP_ENTRY = application_entry

    def build(self):
        bqm = self.__APP_ENTRY.bqm()
        bq_table_name = "price_quote"
        spark = self.__APP_ENTRY.spark()
        raw_data_path = f"gs://{self.__APP_ENTRY.lake_path()}/price_quote.csv"
        target_data_path = f"gs://{self.__APP_ENTRY.target_path()}/price_quote/"

        source_df = spark.read.option("header", "true").csv(raw_data_path)

        source_df.write.mode("overwrite").parquet(target_data_path)

        bqm.write(bq_table_name, f"{target_data_path}/*.parquet")

        pass