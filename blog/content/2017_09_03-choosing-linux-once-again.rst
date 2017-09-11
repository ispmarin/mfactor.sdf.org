Back using Linux at Home
########################

:date: 2017-09-03
:modified: 2017-09-03
:tags: linux
:category: linux
:slug: choosing-linux-once-again
:authors: Ivan Marin
:summary: Going back to Linux at home

After running Windows on my new home laptop, I decided that it is time to switch back to Linux. After a long struggle
I managed to run Linux back at work, so after doing a lot of clean up and selecting files, I´m ready to move back
to Linux full time. The problem is: which Linux?

I´m a long time Debian user and its various flavours. My latest personal installation was a Debian that morphed into
a Frankenstein quickly of Stable, Testing and Unstable. And it broke a couple of times. I don´t want to do that anymore,
I want to turn on my computer and just use it. So Debian Stable would be perfect, right? Well, maybe.

I decided to write this to also organize my ideas of what I need in my Home Linux machine. So below I´ll list some
workflows, some applications and what I´m planning to do, hoping that by the end of this article my choice is clear.

Systems to be compared
----------------------

I will compare the following OS:
- Debian Stable 9.1
- Debian Experimental
- Ubuntu 17.04
- Ubuntu 17.10
- Arch
- Fedora 26
- FreeBSD 11

Why those? Because I want to. I also have familiarity with each of them.

Base system
-----------

For my base system, I need a distro that can dual boot with Windows, for starters. I´ll also need Nvidia blob support,
suspend and hibernate working properly. This can be hit or miss, but from my experience, Ubuntu, Debian and Fedora
have a good support for this. As of now, Ubuntu and Debian are fairly syncronized, while Arch is almost in sync with upstream.
As expected, Debian Experimental is a not good mix.
One problem, though, is that Debian Stable will remain with this version for a long time, although the Debian backports got you covered there.

For the kernel, there are the stable and long stable branches, so it depends. But it shouldn´t be too important if
the basic stuff works.

And finally, the infamous package manager. In this regard, I always will prefer `apt-get`, but `dnf` seems to be very
robust these days.

- Debian: `apt`
- Ubuntu: `apt`
- Arch: `pacman`
- Fedora: `dnf`

So, you may wonder, why not FreeBSD? I say, yes, why not? So far,

- Nvidia driver: 375.39
- kernel: not Linux :-)
- Package manager: ports (`pkg`)

Not bad so far.

Development
-----------

These days most of my development is done in Python, R or Java. How are these on each system?
For Python, considering that `tensorflow <https://www.tensorflow.org/install/>`_ now supports Python 3.6, there is no reason anymore
to use Python 3.5. The rest of the Python packages I install using `pip <https://pypi.python.org/pypi/pip>`_ anyway,
so only the main version is important.

For R, the versions are close enough and it changes slowly. I´ll also use CRAN directly, no worries here.

Java is another matter. Will I use OpenJDK or Oracle Java? If we go on the Oracle route, The webup8 packages are up to date
with Oracle. For the OpenJDK, it depends, but fairly there too. What about support and things breaking? It´s been a while
since I used the OpenJDK, but recently I had to use it with Spark and other Hadoop components and it seemed to hold ok.

My current IDE is either PyCharm or IntelliJ, so no problems there too, I can use them on any of the above platforms. The
rest of my work is done in Jupyter notebooks.

Desktop Environment
-------------------
Here lies dragons. Things start to get pretty bad pretty fast here. I used KDE for a long time, but before that, I used Gnome 2.
And in the middle I used XFCe, Gnome 3, and so on. Never liked Unity. Honestly I don´t know witch one I´ll stick, so lets list
all versions.

Media
-----

I use `digikam <https://www.digikam.org>`_ a lot these days to manage my photos and other media. This is the biggest
difference between all distributions, so I´ll not list here. But also, the changelog between the versions is not that large.

I also use Spotify, and excluding FreeBSD, it is also installable on all distros.

Browsers
--------

I use Firefox mostly and here is always a problem. The version in the distro repositories is always outdated, and the installation
using the binary package directly from Mozilla is quite easy. I think that I´ll keep using it as an external download and not
the distro repository version. Chromium/Chrome is the same: usually I download directly from Google.

Conclusions
-----------

Considering the balance between keeping up with the most up to date packages and the stability of the system, I can exclude
FreeBSD and any Ubuntu from my list. Either the packages are not up to date enough or are in a transitioning version.

Fedora seems to be a good choice, but it is the one that lacks the most documentation. It is quite hard to find package
versions, installation instructions and so on, so I´ll discard Fedora too.

So it remains Debian Stable and Arch. Debian Stable is, well, stable and the package versions are not that old, tracking either
the stable upstream branches or being quite close to upstream. Digikam is one downside but I think that the impact will not be
that large.

The other side is using Arch. Arch has the most up to date packages of everything, of course: it´s a rolling release. The
installation is a bit more troublesome, but not much. So how much would be using Arch satisfy the "Oh shiny" syndrome?