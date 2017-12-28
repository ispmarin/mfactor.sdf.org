Using Virtual Machines and Ubuntu to Keep a Sane Development Environment
########################################################################
:date: 2012-12-11 15:06
:author: ispmarin
:category: debian 
:tags: fortran, symlink, ubuntu, virtualbox, windows
:slug: using-virtual-machines-and-ubuntu-to-keep-a-sane-development-environment
:status: published

I tried. I swear I tried. But it's plain and simple painful to develop
in Fortran in Windows. There, I said it. Is it *possible*? Yes. Is it
easy? Not a chance in Hell.

First of all, there aren't a lot of options for Fortran Compilers for
the Microsoft Windows Platform (and I'm talking about Windows 7, I would
imagine that Windows 8 would be worse.). The most sane one, Intel
Fortran, is even now Intel Visual Fortran Compiler for Windows (`I kid
you
not <http://software.intel.com/en-us/forums/intel-visual-fortran-compiler-for-windows>`__.).
And then there's the interfaces. Microsoft provides for free the
`Express <http://www.microsoft.com/visualstudio/eng/products/visual-studio-express-products>`__
suit, so things are not that bad, right? No. The Express suit can't use
Intel Visual Fortran Compiler for Windows support, so you're out of luck
unless you buy the full Visual Studio Suite, and which one I dunno -
never understood the Ultimate/Professional/Premium/Alien/KitchenCleaning
version confusion. Eclipse CDT/Photran would be a good one instead,
right? No. Intel Visual Fortran Compiler for Windows also doesn't
support Eclipse CDT/Photran. Where to run?

Maybe MinGW could help us? Yes, maybe. Both Intel Visual Fortran
Compiler for Windows and MinGW can compile a Fortran source file from
the command line, but we're in friggin Windows, right? Also, for large
projects, code completion and syntax errors are a must. I didn't try the
LLVM/dragonegg and mingw-fortran combination, but as I wouldn't get the
advantages that I'm looking for, I decided that if I have to use a
Windows machine, no one would prevent to use a sane, decent Linux
environment *inside* that Windows machine. Ubuntu plus VirtualBox it is!

Downloaded 12.10-amd64, installed in a VDI image, all with standard
options. Of course Ubuntu would give me some headaches: had to uninstall
that creepy shopping lens, install Google Chrome. Google Chrome
installation was interesting: the Software Center gave me an "This
package is of low quality. Don't install it." Just hit ignore and
install it anyway. And Ubuntu froze. Unity recomposed itself, but I
figured that there is something funky going on between X and VirtualBox,
so I went back to VirtualBox settings and disabled the 3D video, what
made things a bit better - but still no changing resolution with
changing the size of the VM window. Strange. Will probably install KDE
anyway... so I plugged my external drive to copy all the files to the
VM. And then, Compiz hanged again. Definitely annoying. So while I
waited to see what the 12.10 would do (keep freezed, it seems), decided
to use my 12GB of RAM and my Core i7 and hit an 12.04 installation. It
started to be a little ironic that I was running away from one platform
that is impossible to program to another one that refuses to work to
begin with. I decided to keep going, nonetheless, and see where I would
get.

I still kept my hopes that things would be easier after I got an Ubuntu
running. My plan was to use the VM as a full development environment
that I could transport easily to different computers. I thought about
keeping a git repository of the important stuff, but the multiplatform
problems that I detailed above with Fortran made this a no-go. 12.04 was
much better than 12.10, and while 12.10 was still frozen, I managed to
install 12.04, update it, install the required dkms modules for
VirtualBox. Also downloaded Eclipse CDT, `Eclipse Colour
Plugin <http://eclipsecolorthemes.org/>`__,
`Pydev <http://pydev.org/>`__ and
`Photran <http://www.eclipse.org/photran/>`__,
`OpenJDK <http://openjdk.java.net/>`__, everything running ok! Copied
from my external drive all the source files, all beautiful. Decided not
to use 12.10 and stick with 12.04. So now, the next step: moving the VM
to the external drive.

After copying the entire VB folder to the external drive, I would have
to test it and see if there's anything missing. And it works! Now doing
some backups on external hard drives and transporting happily my virtual
machines around. It's cumbersome to transport 20GB up and down an
external drive every time, but it's better than use Windows to program,
that's for sure!

One last trick: to share a folder between the Ubuntu guest and Windows
host and be able to create soft symlinks, I had to issue this command in
the Windows host:

::

    VBoxManage setextradata VM_NAME VBoxInternal2/SharedFoldersEnableSymlinksCreate/SHARE_NAME 1


    Where VM_NAME is your virtual machine name. Done!
