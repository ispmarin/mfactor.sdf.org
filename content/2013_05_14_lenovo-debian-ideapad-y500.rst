New adventures in Lenovo territory: Ideapad Y500
################################################
:date: 2013-05-14 16:31
:author: Ivan Marin
:category:  debian
:tags: debian, ideapad, ideapad y500, lenovo, linux, ubuntu, windows, windows 7, windows 8
:slug: 2013_05_14_lenovo-debian-ideapad-y500
:status: published

After a long struggle of finding a new laptop and deciding to let my
trusted XPS 15 go, finally I got a Lenovo Ideapad Y500, an awesome
configuration for the price. So this is going to be my journal of the
process of getting this machine to work!

2013-05-14, 12:35:00 The note arrives. The lenovo people didn't put the
number of my apartment on my order, so I had to lurk and wait the UPS
girl on my door. Good thing I have good ears! She was very nice, and
more importantly, she asked for a piece of ID before handling the
notebook.

2013-05-14, 12:40:00 Unpacked! The packaging is very spartan, only the
most basic stuff came. Quite nice, though, no frills.

2013-05-14, 12:42:00 Turned it on, checked it, did the entire Windows 8
login process. The screen is marvelous, quite impressed with the
quality.

2013-05-14, 12:43:00 And removed all partitions that came with the note,
including the recovery and the other stuff! Gone! Gone now! Bye bye
Windows 8! Hello Windows 7! I had to disable Secure Boot and UEFI, set
the boot mode to legacy and legacy first devices, removed \_all\_
partitions, and plug a Windows 7 installation from a USB key. The boot
menu button is on the left side, just next to the power plug. Shutdown
the note and press the button. Booted, ran, ok.

2013-05-14, 12:48:00 Finished the installation, here it comes the first
boot. Decided to use 250GB for windows, gonna use around 60 for Debian,
and the rest is going to be /home. The only reason why the windows
partition is that big is because of the games. C'mon, it has a friggin
Nvidia 750M on it!

2013-05-14, 13:00:00 The Windows 7 installation finished, but of course
there are no drivers. I'm downloading the drivers from the lenovo
website to an external drive to be able to install them.

2013-05-14, 13:25:00 After installing all drivers, one by one, I
realized that Nvidia stable driver can't handle the GT 750M, so I had to
go back to the lenovo site to get the driver from them, and realize that
is just the beta driver from Nvidia... Rebooted (3 times now), and OMFG
the screen is nice. Fuck, it is nice. Still tons of stuff to install in
Windows, but now is time to install Debian! Copied the netinst image
(using dd, dd if=<image> of=/dev/sdc bs=4m; sync) from debian netinst,
clicked the button on the side, plugged, and it booted. Installing now!

2013-05-14, 13:33:00 Hit my first snag with Debian. It asked the
firmware for the wireless card, so I had to go to
`here <http://wireless.kernel.org/en/users/Drivers/iwlwifi/?n=downloads#Firmware>`__
and copied to the external drive. It didn't find the firmware, even if
it was in the folder. Had to copy the .tgz to make it work, not only the
ucode. Trying to read it now.

2013-05-14, 13:43:00 It didn't work, so I had to proceed with the
installation without the firmware for the wifi. Gonna have to copy the
.deb later. And now this is tempting: The debian installer is allowing
me to install it on the internal SSD! But when I tried, it failed. It
also failed to see the GPT Windows partitions, so I had to hit the webs
to find how to do it. Had to go to the "expert install". The expert
install also allowed me to choose the NTFS partition handler, so maybe
that was the problem with the external harddrive. I'm already
downloading an Ubuntu 13.04 image...

2013-05-14, 14:05:00 And Debian refuses to see the GPT partition table.
Gonna have to reset everything, reinstall windows with a MBR partition,
and then reinstall the rest. Damn.

2013-05-14, 14:47:00 Had lunch - not really important, but good to know
that I didn't take that amout of time :-) So now reinstalling windows.
This time I'll try to install Debian before installing everything in
windows.

2013-05-14, 15:08:00 Finally! Debian found all partitions and now is
hapilly installing. No luck with the wifi, though, gonna have to do it
after installing the system.

2013-05-14, 15:26:00 After finishing the Debian installation GRUB only
booted windows. I said a big no to Debian and went Ubuntu. Not because I
can't install Debian, but because I don't have the time. Ubuntu booted
and already connected to my wireless network. And it failed to write to
the hard disk. Linux on this machine is getting more and more
frustrating to install. Downloading a new Ubuntu image and checking the
MD5, just to be sure.

2013-05-14, 16:10:00 Image checksummed, copied and booted. Ubuntu
installation is almost finished, still running.

2013-05-14, 16:30:00 Ubuntu installation finished! There is now a
problem with the Windows install. The Windows install put it on the SSD,
and I only got grub working after removing the Windows partition from
the SSD. Ubuntu boots, but windows dont... So here we go again get a
Windows live usb to boot and fix the mbr \_one more time\_. If I knew
that before I could have kept Debian. But, alas... Installing KDE now.

2013-05-14, 18:00:00 KDE installed, Ubuntu system ready to rock. But for
some reason the Windows partittion, although is intact, can't be found
to boot, and can't boot windows from the USB key. Finishing burning an
old fashioned DVD with the Windows 7 image and will try to recover. If
it works, great; if it doesn't, so sorry, gonna move to the new computer
and Windows will be installed later.

2013-05-14, 18:09:00 Windows booted from the DVD, gonna try to fix it
from the recovery menu. Ran  the automatic repair, and it fixed the
windows installation.

2013-05-14, 18:30:00 Booted on Ubuntu again, after Windows was running,
did the usual installations steps for repairing grub, e voilá! Both
systems are ok! But it should be noted that I had to do a grub-install
/dev/sda, the mSATA, NOT the sda disk. What a mess!

Now is copying all files to the new note :-)

 
