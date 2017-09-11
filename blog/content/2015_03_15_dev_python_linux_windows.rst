Development with Python on Linux is turning into Windows
########################################################
:date: 2015-03-15 06:05
:author: Ivan Marin
:category: debian
:tags: debian, pip, PyCharm, Python
:slug: 2015_03_15_dev_python_linux_windows
:status: published

Yes, the title is a flamebait, but please bear with me.

|image0|

As I said in the last post, I installed Debian on my Chromebook using
`crouton <https://github.com/dnschneid/crouton>`__. It worked quite
easily, KDE installed. But then I started building my dev environment,
using Python. But first, a quick digression.

I have to use Windows at work now. I know, I know, but there's no way
around it. Setting up a dev environment on Windows is very very tricky
and not very funny, especially if you don't have admin rights on your
own machine. I managed to get the basics working, but it was not easy.
The loop search internet->download->install->internet was not fun at all
after all these years with apt-get.

So, when I started setting up my environment on the Debian on the
chromebook it struck me. *I'm doing exactly as I done in Windows.* How
so? First, I installed Python 2.7.9 via apt-get. Nothing funny so far.
Then I decided to use a virtualenv. Ops. To install it I can use the
Debian package or download a newer version directly. Ok, ok... but then
it comes virtualenvwrapper. Ok, I still can install it using the Debian
repos, but it's an old version. After I set up my virtualenv, I start
using pip. Pip is ok, but now I have to download all packages from
different places. I know that this is one of the features of pip, but
nonetheless is divorced from the operating system, there is no search to
speak about inside pip, there is no update all, etc etc. Ok, but there
is still hope, right? Next thing, PyCharm. Bam, gotta go back to the
internet, download it, install... Windows again!

You can argue that I chose to use these packages, that there are several
in the Debian repos that can satisfy my needs. That this is just a rant
that "package A or B is not in the repos!", and I tend to agree with
you. But I didn't have to do nothing like this when I was developing in
C, C++ or Fortran, including libraries, so I started thinking that maybe
the Python tools integration with Debian or any other Linux distro is
not as good as it could be. What can we do to make it easier? So far I
don't know. Any suggestions?

.. |image0| image:: https://dxprience.files.wordpress.com/2014/08/bear-with-me.jpg
