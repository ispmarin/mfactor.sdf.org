Title: Proper way to run PySpark on a Jupyter Notebook
Date: 2016-06-27
Category: data science
Tags: environment, data science, pyspark, jupyter
Authors: Ivan Marin
Summary: How to proper start PySpark with a Jupyter Notebook



Using [Jupyter Notebooks](jupyter.org) with PySpark is the savior combination of all data scientists around the world. The interesting bit about it is that the way that I've saw in the internet to start a PySpark kernel with Jupyter is 

```
IPYTHON_OPTS="notebook --ip 0.0.0.0" ./pyspark 
```

if you want to set the notebook open to the world (careful with that!). But if you launch with this command, you will get this message:

```
[TerminalIPythonApp] WARNING | Subcommand `ipython notebook` is deprecated and will be removed in future versions.
[TerminalIPythonApp] WARNING | You likely want to use `jupyter notebook` in the future
```

This "future" will be probably [version 2.0](https://github.com/apache/spark/blob/master/bin/pyspark#L30), but the proper way to do it already works with 1.6.1: 

```
PYSPARK_DRIVER_PYTHON_OPTS='notebook --ip 0.0.0.0' ./pyspark
```

and done. 
