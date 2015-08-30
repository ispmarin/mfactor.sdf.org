Finally, Python 3!
##################
:date: 2015-06-27 09:39
:author: ispmarin
:category: data science, development
:slug: finally-python-3
:status: published

It's 2015 and it's the first time that I'm using Python 3
professionally. And I have to admit, if I knew that all my scripts were
going to work so easily with 3, I would have changed way before. There
were a few hurdles with the Python 3 version of some libraries - patsy,
I'm looking at you - but so far the transition was painless. The things
that I had to change were expected, like the print function and some
dict operations, and xrange. I know it's for the best now, so let's
roll.

First of all, I switched from WinPython to Anaconda. Having to work on a
constrained Windows installation, Anaconda provides better support for
installing packages than pip alone. And as so far using virtualenv has
not been a success on Windows, I'm going to try the conda environment
for my projects.

On the version control front, I finally got access to a git shell on
Windows, and now I can keep my sanity working with code. There's even a
Team Foundation Server plugin for it, and the client is not that bad -
actually, it's useful and keeps the git terminology, helping immensely
someone that was used to git on the command line. Not bad, Microsoft.
Git-cola is still better and is several times smaller than TFS, but hey,
sometimes we have to use what we got. So my working environment now is

\* Anaconda 2.2.0, Python 3 version

\* Packages:

-pandas, sklearn, matplotlib, calendar, sqlalchemy with Oracle plugin,
seaborn (mostly for styles), statsmodels.

\* Editor:

Vim and ipython notebook (depending on the type of work)

`Git for Windows <https://msysgit.github.io/>`__

and Tableau for some visualizations.
