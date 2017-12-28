Virtualbox cloning and networking in Debian
###########################################
:date: 2012-08-15 08:23
:author: ispmarin
:category: debian, pesquisa, rede
:tags: cluster, debian, network, networking, virtual machine, virtualbox
:slug: virtualbox-cloning-and-networking-in-debian
:status: published

Hey all,

While we're working on the post for Ubuntu and Openstack, we ran into
some problems with Virtual Machines using Virtualbox. We needed an
environment to test and learn, and as we don't have a lot of spare
machines lying around, we decided to use VMs. So first, we installed
Ubuntu Server, configured it, and put it to work. That's great! But what
if I want to access it from the host? Well, here comes the internet to
the rescue. `This
guy <http://wpscale.com/how-to-ping-and-ssh-ubuntu-guest-host-virtualbox/>`__
showed in a very good post how to create a network interface in
Virtualbox and making the connection with the host. Let's do this:

With all VMs down, Open Virtualbox and on the Manage Window, click File
-> Preferences -> Network -> and Add a "host-only" network adapter. This
should create a network interface in the host, called vboxnet0 on my
case, and give it an IP address (192.168.56.1 on my case). Now head for
the Configuration section in the Virtual Machine and add a new Network
adapter with the option "host-only network adapter". Ok! Now start up
the virtual machine and configure the new network (eth1, for example). I
gave it an static IP address on the same network from the one in the
host, so we can talk. The important bits are these: on Debian/Ubuntu,
insert in the file /etc/network/interfaces this:

    | auto eth1
    |  iface eth1 inet static
    |  address 192.168.56.101
    |  netmask 255.255.255.0

Done! You should be able now to access via ssh, for example, from the
host and from the guest (remember that the host has an IP of
192.168.56.1). For example, from host to guest:

    ssh user@192.168.56.101

And vice-versa, from guest to host:

    ssh user@192.168.56.1

That's it! Now, what about clones? That's also easy, with a small
caveat. Shutdown all VMs, select one, and clone it using the Clone
button! I opted for a Hard Copy, not a Linked one, but YMMV. Also ask to
change the MAC address of the interfaces. There are two things that you
need to change on the new clone: first head to /etc/hostname and change
it to a new one. The second one is that, thanks to `this
guy <http://koansys.com/tech/create-virtualbox-clone-with-its-own-mac-address>`__,
we have to remove the file

    sudo rm /etc/udev/rules.d/70-persistent-net.rules

as it seems that both Debian and Ubuntu, even if you change the MAC
address, can't cope with it. Removing and reeboting and voilà, you
should have your new clone up and running! Configure again the vboxnet
interface on the guest for a new ip, for example

    | auto eth1
    |  iface eth1 inet static
    |  address 192.168.56.102
    |  netmask 255.255.255.0

And now you can ssh to your heart's content, even between the two VMs!
Great, huh?]

PS: Also another great idea: create an VM, configure it, deploy it on an
USB pendrive, and install it! I Love it! From
here: \ http://ubuntuforums.org/showthread.php?t=1904557
