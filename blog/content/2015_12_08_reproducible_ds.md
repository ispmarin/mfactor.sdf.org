Title: Data Science workflow with reproducible research
Date: 2015-12-08
Category: data science
Modified: 2015-12-08 22:42
Tags: data science, data
Authors: Ivan Marin
slug: 2015_12_08_reproducible_ds
Summary: Organization of a data science workflow using CRISP-DM and Reproducible Research

# Data science workflow

I've been wondering and tinkering about how to structure my data science projects, thinking on the lines of [Reproducible Research](http://reproducibleresearch.net/) and separation of information. There is a lot of talk about the CRISP-DM [Cross Industry Standard Process for Data Mining](https://en.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining) and I believe that CRISP-DM is indeed a good approach. There are others like [SEMMA](https://en.wikipedia.org/wiki/SEMMA) that are similar. But how these processes come down to a real project organization? Breaking down the steps, in a general overview, a data science project generally has

- `data`, either the datasets or samples, that will be worked on
- `src` (a code folder), for analysis, ETL and modeling
- `documentation` about the problem, business case, the data and the solution
- `results`, in form of processed data, a software deployment process or final documentation (including presentation)

Of course your project will have other needs or either a more complex or more simple structure, also depending on how you think about CRISP-DM or your own approach. But so far this structure above has helped me to keep things organized and understandable based on CRISP-DM. I try to keep in line the ideas from both the process and reproducible research.

I also have a few other requirements for my projects:

1. all code must be versioned
2. all data must be identified by data and local
3. the documentation should also be versioned a preferably autogenerated
4. the results should be reproducible, without intervention
5. libraries should be isolated from the system and preferably portable to other systems

Requirements 1 and 3 are satisfied using `git`. I usually set the root of the project as the `git` base directory and exclude on the `.gitignore` the data and results directories. I decided not to include the `results` folder because of requirement 4 and also because they can be big. An exception can be made if there are presentations inside `results` that are not autogenerated. Part of the autogeneration of the documentation is made writing it on the analysis code itself, a la `jupyter` notebook style.

Requirement 2 is satisfied using a simple directory structure. Inside the `data` folder I create a directory with the date as the name, like `20151207` and include hour and minute if I'm generating samples with this precision. If I need to generate a sample a `sample` directory inside the dated directory suffices. Some people advise to save intermediate steps if there are a lot of data cleanup steps. I tend to do it if the cleanup step is too time consuming, otherwise I just recompute the cleanup step. I also tend to include the metadata with the data, outside the data file, with the same name as the data file but with a `.meta` termination.

The local part of the `data` can be tricky when using a database as a source, for example. This is one of the points where reproducible research helps a bit: databases can change, so let's say you run today a model with data pulled from a database. You should be able to reproduce exactly the same results any time, but the database could have been updated in the meantime and your project is not reproducible anymore. I download the data to a local storage file (either csv or HDF5 or other format at hand) and use this file to do my computations. There is a real problem if the data set is too large or the data is sensitive, but so far I've managed to do it without serious issues.

I usually use `jupyter` and `python` to do my analysis and modeling, so to satisfy requirement 4 I tend to write my notebooks and code so they are idempotent and can be restarted from different points. That also means that the results would be overwritten everytime the code is run. This can be a problem if a experiment is being done with different inputs, so this should be taken into account when thinking on the structure of the `results` folder (It can use the same dated approach from the `data` directory).

The last requirement depends on the language or languages that are being used in the project. This is a rather lengthy subject, so I will restrict myself to Python. I use `virtualenvs` without site packages and keep them on the `src` folder. Each project has its own virtualenv. Other requirements, like map data, is also included on the project structure, so the entire project folder can be moved without great impact. Virtualenvs are not that portable between systems and this has been a problem so far without solution, especially if the other system doesn't have internet access.

## Project Example

As an example I have the `polls` project, with the following directory structure:

```
.pools
+-- data
   +-- 20151206
      +-- polls.csv
      +-- polls.meta
      +-- sample
         +-- polls_sample_1000.csv
         +-- polls_sample_200.csv
   +-- 20151203
      +-- polls_rs.csv
      +-- sample
         +-- polls_sample_rs_1000.csv
         +-- polls_sample_pe_200.csv
   +-- 20151202
      +-- all_polls.hdf
      +-- all_polls.meta
+-- src
   +-- analysis
      +-- pools.ipynb
   +-- sampling
      +-- sampling.py
   +-- etl
      +-- extract_from_mongo.py
   +-- generate_results
      +-- do_models.py
      +-- generate_webpage.py
      +-- generate_approach_action.py
         +-- images
            +-- header.png
            +-- logo.svg
+-- doc
   +-- business
      +-- use_case.md
   +-- algorithm
      +-- machine_learning.md
      +-- analysis_results.md
         +-- images
            +-- analysis_all.png
+-- results
   +-- 20151207
      +-- voters.csv
      +-- control_group.csv
      +-- approach_and_action.md
```

One of the things that I also consider is the use of symbolic links from the `src` folder to the `results` folder or do a copy of a figure, from example.

On the next article I plan to show a pattern for `jupyter` notebooks to handle this structure.

