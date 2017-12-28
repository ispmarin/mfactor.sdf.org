Title: Using `conda` instead of `pip`
Date: 2015-11-26
Category: Linux
Modified: 2015-11-26 22:42
Tags: python, pip, conda
Slug: conda
Authors: Ivan Marin
Summary: Trying out conda for managing Python environments

I've been struggling with which environment use to develop on Python applications that 
are going to be moved around and run on different systems. There is Hadoop and Spark on the mix, so things are getting
more complicated, too. Thinking about my environment, I have the following requisites:

1. Determine the level of isolation of the application.
2. Point to the `python` binary that I want.
3. Can be moved around 
4. Can be deployed and used in systems without internet
5. Can be deployed and used without root access

So far I have two alternatives: `virtualenv` and `Anaconda`. I've been using `virtualenv` for a while so I know 
better the limitations. I tried, then, to use `Anaconda` to see how it works. The installer is heavy but it comes
with several useful things (`pandas`, for example), so that's ok. Things got a bit complicated using the environments,
though, with the `conda` application. To keep point 2 I changed the recommended `PATH` variable to 

```
export PATH=$PATH:/home/ispmarin/bin:/home/ispmarin/bin/anaconda3/bin
```

so I get the system `python` executable but all the other tools from `Anaconda`. Nice. Then I created and environment
and installed some stuff there. Also works as expected, although it points to the `python` binary from inside `Anaconda`.
Acceptable. Then I deactivated the environment, and to my surprise, the `python` executable didn't change back to 
the system one! Damn, that's a problem right there. There 
[are](http://stackoverflow.com/questions/33955516/anaconda-activate-deactivate-cycle-messes-up-path) 
[several](https://github.com/conda/conda/issues/1846) 
[bug](https://github.com/conda/conda/pull/1727) reports on the `conda` github, but still no final solution. So `conda` is
out for now.