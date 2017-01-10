Using `pip` with `--user` flag
##############################

:date: 2016-06-28 19:34
:modified: 2016-06-28 19:34
:tags: development, python
:category: development
:slug: 2016_06_28_pip_with_user
:authors: Ivan Marin
:summary: How to build a Python environment with pip
:status: draft


The problem of generating a remote development environment for Python is always how are you going to build your packages? I have an old [sdf](sdf.lonestar.org) account with MetaArray benefits, but was never able to set up there as my development environment, especially because they run NetBSD. But with the `--user` flag for `pip`, things got a bit easier.

First, we check that we have `python` and `pip` over there - just make sure that you're running Python 2.7. If not, set your `PATH` variable to the correct Python executable and use `pip2.7` to be sure. Now to install the packages that we want, we use the flag [`--user`](https://pip.readthedocs.io/en/latest/user_guide/#user-installs):

```
pip2.7 install --user pandas
```

this will install `pandas` on the directory `$HOME/.local`. The first thing that I do afterwars is to install the package `virtualenvwrapper` and create a few virtualenvs to work with.
