Back using Linux at Home - the Aftermath
########################################

:date: 2017-09-10
:modified: 2017-09-10
:tags: linux
:category: linux
:slug: choosing-linux-once-again-the-aftermath
:authors: Ivan Marin
:summary: And Linux is back

As I wrote in my previous article, I decided to use Linux again on my home laptop.

The winner
----------

I said I would compare the following OS:
- Debian Stable 9.1
- Debian Experimental
- Ubuntu 17.04
- Ubuntu 17.10
- Arch
- Fedora 26
- FreeBSD 11

and in the end, I went back to the good old Debian Stable. The reasons were familiarity, ease of install, and apt.
I know, the OSes above are awesome and all have pros and cons, but in the end, my goal was to have a stable Linux
installation that supported my requirements with a minimum of fuss. So Debian it is.

Installation
------------

I disabled Secure Boot and enabled Legacy OS loading on the BIOS, otherwise Debian wouldn't boot on my Dell. I'll try no
to enter into too many details here. The main choices were:

- Debian Stable 9.1
- LVM partitioning (more on that later)
- KDE 5.8.4 LTS, KDE Framework 5.28, Qt 5.7.1
- NVidia 375.66 with Bumblebee

Partitioning
------------

Remember what I've said about familiarity? I got bitten by it. I'm so used in creating VM instances with Debian from scratch
that I forgot that the debinstall "Assisted use all disk with LVM" *erases* the disk. I was concerned about the Windows
installation and wanted to preserve it, but after doing the partitioning I noticed my mistake. The Windows partition was gone.
I was thinking that this would have an impact, but so far, everything seems better without it.

Applications
------------

I installed the following applications directly from the web:

- Firefox 55 (tar.gz)
- Spotify (deb)
- Google Chrome (deb)
- PyCharm (tar.gz)
- SpiderOak

and from the Debian repos:

- Digikam (5.3)
- Backintime
- Gnucash
- QtPass
- VLC
- Gparted
- Calibre
- Transmission-Qt
- virtualenvwrapper

Problems
--------

Backintime
..........
So far, the only problem that I had with this configuration is that Backintime, when creating a profile, if the destination
drive is not writtable by the user, it will not allow the creation of a profile, but also will not output an error. As
I do my external backups to an external USB disk and for some reason I was not allowed to write to it, Backintime would
balk at it without any error message. I had to go to the terminal and change the owner of the folder to be able to do it.

Flatpak
.......

I thought about using `Flatpak <https://flatpak.org>`_ to install a few applications, like Spotify, but the amount of things that it would pull into
the system was insane, so I didn't go forward with it.

Nix
...

I also installed `Nix <https://nixos.org>`_ to try it out, but again, the amount of stuff it needs to download is staggering. But differently than
Flatpak, I'll try Nix again.

Next steps
----------

Now that the basic stuff is configured and down, there are a few things that I need to do:

- configure my ssh/config file again. This should be stored in a repo somewhere.
- configure my bashrc. I tried using ZSH in the past, but I always come back to bash.
- get Python 3.6 in this system. I definitely don't want to pull from Unstable, so I'm still considering what to do.
- automate the GPG import of my keys. I use my keys for managing my passwords.
