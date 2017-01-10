Gnome 3.16 on Debian Unstable: New adventures on the Window Manager lands
#########################################################################
:date: 2015-05-24 15:49
:author: Ivan Marin
:category: tools
:slug: 2015_05_24_gnome-3-16-on-debian-unstable
:status: published

I finally got my hands on a decent monitor, the `Dell
U2515H <http://accessories.la.dell.com/sna/productdetail.aspx?c=br&l=pt&s=dhs&cs=brdhs1&sku=480-ACXS>`__.
It has been, so far, an awesome monitor. But that showed a few issues
with my standard Debian installation, with KDE 4.14 on Debian Unstable.
It seemed that every GTK application decided to throw a fit together and
nothing worked. I tried to adjust a lot of stuff on gtk-qt to fix it to
no avail but as it was GTK that was giving me headaches, maybe
installing Gnome things would be better on KDE side. So after a really
long time I decided to test a new window manager while at it, and now
I'm running Gnome 3.16 on Debian Unstable. (Also, it is a good change of
pace while I wait for KDE 5 hit Unstable.)

But, as every transition... things got a little rough. The `famous
rant <https://plus.google.com/+LinusTorvalds/posts/UkoAaLDpF4i>`__ by
Linus Torvalds rings very true: they simplified so much that it's dumb
(even if Linus is `using it
again <https://plus.google.com/115250422803614415116/posts/KygiWsQc4Wm>`__).
There are some things that I found to be incredible as design decisions,
and Gnome Extensions is one of them.

C'mon, how am I supposed to keep different systems updated, with the
same extensions? How do I know that they will work before I install
them? Who makes them? There are a few packaged in Debian, but not
enough. And to see how this is crazy, I had to install extensions to
show a suspend button, wicd-gtk on a tray, and I still can't find one to
easily lock my screen or close the session! So both things that
shouldn't be broken, standard desktop stuff and extensions, are broken
in one go.

Also, there is no easy way to change the system fonts, colors or
everything else. I had to use gnome-tweak-tool to do all this, a
non-standard tool, and still there are a ton of stuff that I should be
able to configure and it is removed. Even in more lighter environments,
like LXDE, I stil can change the icons or set a random image as my
wallpaper, as a user. I don't want to copy stuff to /usr or other system
directories, I should be able to override the system paths with folders
on my home directory, preferably under .local or .config. (And if you're
thinking that I must go to the image, right-click it to set as wallpaper
as the only way to do it, no, that is no proper behavior.) The fact that
even if I do the right-click thing, now I have a folder called
Wallpapers on my home folder buggers me. I didn't ask for a wallpaper
folder, just use any path that I gave you! ME, not Gnome programmers,
know were my files should go.

Also, I can't lock my screen if GDM is not running. This is now really
bad, not just annoyances like before. They hand-wave this away saying
that this will be solved with Wayland, but Wayland has been in
development for a while and it's not shipping as production ready for
another not known time, so I would have to wait for it to lock my
screen? I don't want to run GDM, I should be able to run whatever login
manager I want and be able to lock my screen in the WM. If Gnome keeps
following this "Windows" path all the complaints in the last years would
be true. The dependency on their own backyard instead of keeping things
interchangeable is a very troubling sign, and like the systemd debacle,
it just keeps getting worse.

I understand the need for standards, and XDG directives are ok, but
instead of thinking that the users are dumb, please at least let us
choose. I know this is kinda of a old rant against Gnome, and it can get
very ugly if I start mentioning Gnome 2, but from a fresh start, Gnome
right now is bad. Yadda yadda use another window manager, I get it. I
will, as soon I can get my hands on KDE 5. But for now, maybe another
voice trying to show what is broken, from an outside perspective, can
help a bit into steering things on a better path.
