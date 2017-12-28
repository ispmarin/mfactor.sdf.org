SSD and Lenovo Y500: Should the saga continue?
##############################################
:date: 2014-05-22 16:39
:author: ispmarin
:category: computational physics
:tags: debian, grub, lenovo, ssd, y500
:slug: ssd-and-lenovo-y500-should-the-saga-continue
:status: published

After a long while fighting the SSD and the NVidia board on this laptop,
finally Debian and the Y500 can talk. So now, running Debian Sid,
everything seems to be ok.

| uname -a
|  Linux endeavor 3.12-1-amd64 #1 SMP Debian 3.12.9-1 (2014-02-01)
  x86\_64 GNU/Linux

| dpkg -l \| grep nvidia
|  ii glx-alternative-nvidia 0.4.1 amd64 allows the selection of NVIDIA
  as GLX provider
|  ii libgl1-nvidia-glx:amd64 331.67-1 amd64 NVIDIA binary OpenGL
  libraries
|  ii libgl1-nvidia-glx:i386 331.67-1 i386 NVIDIA binary OpenGL
  libraries
|  ii libnvidia-ml1:amd64 331.67-2 amd64 NVIDIA Management Library
  (NVML) runtime library
|  ii nvidia-alternative 331.67-1 i386 allows the selection of NVIDIA as
  GLX provider
|  ii nvidia-cg-dev:amd64 3.1.0013-1 amd64 Cg Toolkit - GPU Shader
  Authoring Language (headers)
|  ii nvidia-cg-toolkit 3.1.0013-1 amd64 Cg Toolkit - GPU Shader
  Authoring Language
|  ii nvidia-driver 331.67-1 amd64 NVIDIA metapackage
|  ii nvidia-installer-cleanup 20131102+1 amd64 cleanup after driver
  installation with the nvidia-installer
|  ii nvidia-kernel-common 20131102+1 amd64 NVIDIA binary kernel module
  support files
|  ii nvidia-kernel-dkms 331.67-2 amd64 NVIDIA binary kernel module DKMS
  source
|  ii nvidia-settings 331.67-1 amd64 tool for configuring the NVIDIA
  graphics driver
|  ii nvidia-support 20131102+1 amd64 NVIDIA binary graphics driver
  support files
|  ii nvidia-vdpau-driver:amd64 331.67-1 amd64 NVIDIA vdpau driver
|  ii nvidia-xconfig 331.67-1 amd64 X configuration tool for non-free
  NVIDIA drivers
|  ii xserver-xorg-video-nvidia 331.67-1 amd64 NVIDIA binary Xorg driver

 

With a reasonable performance on Kerbal Space.

But, as things that are working are boring, there's a 10GB SSD sleeping,
unused, both in Windows and Linux. Boy, it would be fun to run /usr/bin
from there!

fdisk tells me

After a long while fighting the SSD and the NVidia board on this laptop,
finally Debian and the Y500 can talk. So now, running Debian Sid,
everything seems to be ok.

| uname -a
|  Linux endeavor 3.12-1-amd64 #1 SMP Debian 3.12.9-1 (2014-02-01)
  x86\_64 GNU/Linux

| dpkg -l \| grep nvidia
|  ii glx-alternative-nvidia 0.4.1 amd64 allows the selection of NVIDIA
  as GLX provider
|  ii libgl1-nvidia-glx:amd64 331.67-1 amd64 NVIDIA binary OpenGL
  libraries
|  ii libgl1-nvidia-glx:i386 331.67-1 i386 NVIDIA binary OpenGL
  libraries
|  ii libnvidia-ml1:amd64 331.67-2 amd64 NVIDIA Management Library
  (NVML) runtime library
|  ii nvidia-alternative 331.67-1 i386 allows the selection of NVIDIA as
  GLX provider
|  ii nvidia-cg-dev:amd64 3.1.0013-1 amd64 Cg Toolkit - GPU Shader
  Authoring Language (headers)
|  ii nvidia-cg-toolkit 3.1.0013-1 amd64 Cg Toolkit - GPU Shader
  Authoring Language
|  ii nvidia-driver 331.67-1 amd64 NVIDIA metapackage
|  ii nvidia-installer-cleanup 20131102+1 amd64 cleanup after driver
  installation with the nvidia-installer
|  ii nvidia-kernel-common 20131102+1 amd64 NVIDIA binary kernel module
  support files
|  ii nvidia-kernel-dkms 331.67-2 amd64 NVIDIA binary kernel module DKMS
  source
|  ii nvidia-settings 331.67-1 amd64 tool for configuring the NVIDIA
  graphics driver
|  ii nvidia-support 20131102+1 amd64 NVIDIA binary graphics driver
  support files
|  ii nvidia-vdpau-driver:amd64 331.67-1 amd64 NVIDIA vdpau driver
|  ii nvidia-xconfig 331.67-1 amd64 X configuration tool for non-free
  NVIDIA drivers
|  ii xserver-xorg-video-nvidia 331.67-1 amd64 NVIDIA binary Xorg driver

 

With a reasonable performance on Kerbal Space.

But, as things that are working are boring, there's a 10GB SSD sleeping,
unused, both in Windows and Linux. Boy, it would be fun to run /usr/bin
from there!

fdisk tells me

| Disk /dev/sda: 16.0 GB, 16013942784 bytes
|  255 heads, 63 sectors/track, 1946 cylinders, total 31277232 sectors
|  Units = setores of 1 \* 512 = 512 bytes
|  Sector size (logical/physical): 512 bytes / 512 bytes
|  I/O size (minimum/optimal): 512 bytes / 512 bytes
|  Disk identifier: 0x00090bd1

Dispositivo Boot      Start         End      Blocks   Id  System

no partition.

| sudo file -s /dev/sda
|  /dev/sda: DOS/MBR boot sector

So there's my MBR, exactly as my sdb. What now?

As soon I gather courage - and time - I'll try to reinstall the system
there.
