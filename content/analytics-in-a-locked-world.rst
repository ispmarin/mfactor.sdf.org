Analytics in a locked world
###########################
:date: 2015-04-21 19:25
:author: I M 
:category: data science
:tags: pandas, Python
:slug: analytics-in-a-locked-world
:status: published

As a data scientist, I have to deal with data from several different
sources. This begs for a wide range of tools and great flexibility of
using these tools, otherwise manipulating the data can be almost
impossible. And then your employer says that you can only use Windows,
without admin rights, and you can only install software from a very
restrict pre-approved list. What do you do? Go to a corner and cry?

Almost. But then, you find a breach, a sliver of hope. You can install
python on your machine. And in this moment, you smile, asking if you're
up to the challenge. (Dramatic, no?)

With one of the best Python installations for Windows is
`WinPython <https://winpython.github.io/>`__, that comes prepackaged
with `Numpy, Scipy and
Pandas <https://github.com/winpython/winpython/issues/56>`__ and other
neat stuff, you can start really working. The second best part is that
you can install on your user folder, so you don't need admin rights.
Ufta! And the savior for sane workflows in this setting is
`Jupyter <https://jupyter.org/>`__, the new IPython shell. It is awesome
for the data and modelling workflow.

My workflow now consists of:

1. Getting all raw data in one place, be excel spreadsheets (don't ask),
CSV files, word files (I said don't ask!), and some data banks. Most of
my data are time series.

2. Importing the data or connecting the services on a jupyter python
notebook. I have to connect to an oracle BD, so
`cx\_Oracle <http://cx-oracle.sourceforge.net/>`__ is the connector.

3. Parsing the data with
`ExcelFile <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.excel.ExcelFile.parse.html>`__
from `pandas <http://pandas.pydata.org/>`__. It can be tricky. As each
sheet is different, I use a JSON file with the starting line, starting
and ending columns, number of lines to be read and headers. That way I
can process it automatically, and if the file changes is quite easy to
adjust.

4. Ok, clear the data! This is usually the most problematic part. One of
the things that I had to do was to convert zero values to NaNs. The
reason is that zero is a valid value on my data, but not a real one, so
it would skew all statistics. Pandas can handle NaNs in the\ `Right
Way <http://pandas.pydata.org/pandas-docs/version/0.16.0/gotchas.html>`__,
so you would be better off. But beware, there are a few problems with
`some
functions <http://stackoverflow.com/questions/29747850/error-using-bootstrap-plot-in-pandas-if-values-have-nan>`__,
so you have to be careful anyway.

5. With the data in a proper format, (`tidy
format <www.jstatsoft.org/v59/i10/paper>`__, NaNs for invalid values,
all values with proper references), I start doing some exploratory
analysis on the data. For now, basic stuff like line graphs, boxplots,
averages by year and month, autocorrelation and some rolling means, and
scatter plots.

6. With that things start to get more interesting. I decided to use
`Scikit-Learn <http://scikit-learn.org/stable/>`__ to do the regressions
instead of statsmodels because of the next step, prediction. You have to
transform the data again so scikit can understand it, but it's\ `not
that
hard <http://stackoverflow.com/questions/29748717/use-scikit-learn-to-do-linear-regression-on-a-time-series-pandas-data-frame>`__,
and worth the while. Now I do some stardard Linear Squares to get the
trend and a RANSAC to get more specific results.

And all this inside a ipython notebook! Pretty awesome, right? Next
steps, do a full
`Box-Jenkins <http://en.wikipedia.org/wiki/Box%E2%80%93Jenkins>`__ on
the results.
