Y500, Nvidia and kernel 3.9
###########################
:date: 2013-12-20 06:13
:author: ispmarin
:category: ciência
:tags: debian, lenovo, nvidia, y500
:slug: y500-nvidia-and-kernel-3-9
:status: published

The love story with the Y500 does not end yet. The note is working very
well - I can play Borderlands 2 on it! - but on the Linux side I'm stuck
to Kernel 3.9 because some brouhaha between the X API and the Nvidia
driver with Optimus systems. What, you say, the Y500 does not have an
Intel card! Nope, it does, it's just deactivated. There is a very long
forum post on `Nvidia
devtalk <https://devtalk.nvidia.com/default/topic/567297/linux-3-10-driver-crash/>`__
with people reporting the same problem up to kernel 3.12. I tested the
3.12 trunk from Debian with no luck. So, what can we do about it?
