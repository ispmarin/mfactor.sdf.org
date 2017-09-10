####################################
Using `venv` for Python 3 virtualenv
####################################

:date: 2017-05-07 11:44
:modified: 2017-05-07 11:44
:tags: python, python3, virtualenv, venv
:category: development
:slug: 2017_05_07_python3-venv-virtualenv
:authors: Ivan Marin
:summary: How to use `venv` as a virtualenv

I've been trying to use Python 3.6 as much as I can. I've been bitten by the encoding problems of Python 2
too many times to remember - and that's my reason why I want to use Python 3 for now, I will not enter
the `eternal <https://wiki.python.org/moin/Python2orPython3>`_
`flamewar <https://news.ycombinator.com/item?id=13019819>`_ `between <https://news.ycombinator.com/item?id=13504215>`_
`Python 2 <https://news.ycombinator.com/item?id=13061570>`_ `vs <https://news.ycombinator.com/item?id=13053757>`_
`Python 3 <https://www.reddit.com/r/Python/comments/qwq4l/not_trying_to_start_a_flame_war_but_which_python/>`_.

So I decided to try the Python 3 solution for creating virtualenvs: `venv <https://docs.python.org/3/library/venv.html>`_.
It should be the default way tho create virtualenvs, as it's not based on "hacks" as the package `virtualenv` and
it's now part of the default distribution.

So far, it seems that some nice shortcuts and functionalities are still not there, like relocate a virtualenv and
the handy `workon` from the `virtualenvwrapper` package. What is missing so far is a workflow management. The rest is very
similar to working with virtualenvs and `pip`.


Working with `venv`
-------------------

The standard way of working with `venv` is quite similar to `virtualenv`:

::

    /usr/bin/python3.6 -m venv test_env /home/username/bin/virtualenvs/test_env

So now the virtualenv is created. To activate it, use the full `source activate` path:

::

    source /home/username/bin/virtualenvs/test_env/bin/activate

and now we are inside the virtualenv `test_env`. To install packages use the traditional `pip`:

::

    pip install matplotlib sklearn pandas jupyter folium

And that's it. To deactivate a simple `deactivate` suffices.


Managing the virtualenvs
------------------------

One of the things that is both good and bad about Continuum `conda` is the hability of managing the virtualenvs. We
can list the available environments with

::

    conda info --envs

That will show all virtualenvs created using conda and the full paths. With `venv` we have to resort to using the filesystem
tools directly, or being explicit, using `ls`.

Listing packages can be done using `pip` directly. Removing a virtualenv is done using the good old `rm`.


Virtualenvwrapper comparison
----------------------------

The `virtualenvwrapper <http://virtualenvwrapper.readthedocs.io/>`_ package has the purpose of handling the steps explained
above with some shell tools. `venv`, of course doesn't provide any of this. There is even an option that I was not aware on
`virtualenvwrapper`, that is, managing `projects <http://virtualenvwrapper.readthedocs.io/en/latest/projects.html#project-management>`_.
This looks very interesting to me, as I'm `quite found <http://mfactor.sdf.org/blog/2015_12_08_reproducible_ds.html>`_ of reproducible environments and `automated tools <http://mfactor.sdf.org/blog/2015_11_26_conda.html>`_ for it.
I'll test it against the `Data Science Cookie Cutter <https://github.com/ispmarin/cookiecutter-pypackage>`_ and report back.

