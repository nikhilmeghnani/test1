from pyspark.sql import SparkSession

from pyspark.sql import Sp


if __name__ == "__main__":
    print("application started")

    spark = (
        SparkSession.builder.appName("first spark with python")
        .master("local[*]")
        .getOrCreate()
    )

    # commit test


    input_file_path = (
        "D:\\nikhil_meghnani\\ilink_work\\pycharm_workspace\\learning\\sample.txt"
    )

    tech_rdd = spark.sparkContext.textFile(input_file_path)

    print(tech_rdd.collect())
