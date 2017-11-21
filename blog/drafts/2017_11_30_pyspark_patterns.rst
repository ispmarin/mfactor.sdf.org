PySpark Patterns
################

:date: 2017-11-23 10:20
:modified: 2017-11-24 18:40
:tags: data science, Pyspark, spark, patterns
:category: data science, Spark
:slug: my-super-post
:authors: Ivan Marin
:summary: PySpark common patters

A `software design pattern <https://en.wikipedia.org/wiki/Software_design_pattern>`_ is a "reusable solution to a commonly
occuring problem". After working with `PySpark <https://spark.apache.org/docs/latest/rdd-programming-guide.html>`_ for a
while now, I noticed a few patterns that keep coming up and some solutions that I've been using to solve them. So please
take these patterns with a grain of salt, and if you have a better solution, please don't hesitate to contact me!

Data Ingestion
--------------

PySpark is awesome for several reasons and one of them is the multitude of ways that it can read data. Lately, the most
common one for me is to read some data stored as tables in Hive or Impala. (Actually, the "tables" are stored in HDFS
and mapped to a relational structure by the Hive metastore, both for Hive itself and for Impala.) To keep the ingestion code
general, as is pretty similar to different tables, I use a JSON file or a dictionary with the database information:

::

    db_properties = {
        "src_db_name": "source_db",
        "src_tb_name" : "source_tb",
        "dest_db_name" : "dest_db",
        "dest_tb_name" : "dest_tb"
    }

So the pattern is to keep variable information in a different structure and the PySpark code itself the same for all
ingestion processes:

::

    df_src = spark.table(
        "{}.{}".format(
            properties['src_db_name'],
            properties['src_tb_name']
        )
    )
    df_dest = spark.table(
        "{}.{}".format(
            properties['dest_db_name'],
            properties['dest_tb_name']
        )
    )

I know, not earth-shattering, but very handy when there are lot of different tables to be read. This is also helpul when
different databases are used:

::

    postgres_properties = {
        "user": "myuser",
        "password": "mypassword",
        "db":"postgresdb",
        "table":"postgrestable",
        "host":"myhosturl.local",
        "port":5432,
    }

    df_psql = spark.read.jdbc(
        "jdbc:postgres://{}.{}@{}/{}".format(
            postgres_properties["user"],
            postgres_properties["password"],
            postgres_properties["host"],
            postgres_properties["db"],
        )
    )

The benefit in this case is that the properties dict for PostgreSQL can be kept outside the code, preserving the password.


Filters
-------

Another very common task in a data ingestion pipeline using PySpark is to filter the values, either to remove outliers or
to select the data of interest. As another simple pattern, I use the method chaining for the `filter` method:

::

     df_filter = df.filter(df.dt > '2017-01-01').filter(df.dt <= '2017-03-31').filter(df.mytype == 'A').filter(df.othertype != 'B').\
                   .filter(df.anotherone.isin(['C', 'D']))
