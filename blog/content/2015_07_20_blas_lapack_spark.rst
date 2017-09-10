A history of packages and libraries or: how Spark and Hadoop are doing the same mistake as BLAS and LAPACK
##########################################################################################################
:date: 2015-07-20 09:33
:author: Ivan Marin
:category: data science 
:tags: beowulf, big data, debian, haddop, openstack, spark
:slug: 2015_07_20_blas_lapack_spark
:status: published

A long time ago, on a land of big iron and MPI, there were some
libraries that were used everywhere. The libraries were fundamental to
most of the important computation that was done, they were open source
and all the cool kids on the block knew them. They also rarely were
distributed by the Linux distributions, and several versions needed to
coexist to support all the high performance software that needed to be
run. They needed to be compiled, and different versions of compilers and
libraries and binaries kept spiralling out of control. Keeping them
working was already a huge task, and working well was even harder. And
yes, I'm talking about BLAS and LAPACK.

`BLAS <http://www.netlib.org/blas/>`__ (Basic Linear Algebra Suprograms)
and `LAPACK <http://www.netlib.org/lapack/>`__ (Linear Algebra PACKAge),
from `Netlib <http://www.netlib.org/>`__, were fundamental on the HPC
era as the backbone of inumerous projects. The stack on those days had
one flavour or another of
`MPI <https://en.wikipedia.org/wiki/Message_Passing_Interface>`__ to run
the parallel jobs in huge clusters, together with
`ScaLAPACK <http://www.netlib.org/scalapack/>`__. And the job of keeping
these libraries working with several different compilers (mainly
`GCC <https://gcc.gnu.org/>`__,
`Intel <https://software.intel.com/en-us/intel-compilers>`__ and
`Portland Group <http://www.pgroup.com/>`__ compilers ) and linking
binaries objects were the nightmare of any sysadmin. Written mainly in
Fortran, with wrappers for C and C++, a sysadmin had to keep the entire
stack compiled with the right version of compilers and linked with the
right libraries. Projects like `ATLAS <http://www.netlib.org/atlas/>`__
tried to help a bit on the side of performance optimization, while
vendors had their own binary distribution, tuned to their processors
(`MKL <https://software.intel.com/en-us/intel-mkl>`__ for Intel and
`ACML <http://developer.amd.com/tools-and-sdks/cpu-development/amd-core-math-library-acml/>`__
for AMD).

A sysadmin on the HPC world had to know all these libraries, how to
deploy them to the users that wanted to compile their own programs, and
how to make all of them play nice with each other on the same cluster.
It was hard to keep track of what was breaking, with lots of non
standard paths and binary objects, name mangling, and users trying to do
things that you never imagined possible. The HPC sysadmin also needed to
know the underlying architecture very well, including the network and
storage structures, the physical layout of the cables, so he or she
could have a chance to know what was breaking or lagging.  Slowly, these
tools started to be better organized, with practices like module loading
and the linux distributions creating packages to the basic libraries,
even if the performance was not the best possible. And then the Cloud
happened.

(I'm not going to dwelve on the HPC vs Cloud debate, not even try to
touch the Big Data vs BI vs computing debates, and try to focus on the
tools that make all these acronyms possible, otherwise this would be a
very long post.)

I have some time now on my hands and decided to check how the deployment
and configuration of a Spark cluster is being done on
`Debian <https://spark.apache.org/docs/latest/>`__. And boy, `what a
surprise <http://spark.apache.org/docs/latest/building-spark.html>`__.
I've been seeing several posts from sysadmins complaining about the
dockerization of applications and the mirage of the devops, but was
taken aback with the state of how Spark is suposed to be deployed on a
Debian (`or any other
linux <http://bigtop.apache.org/book/apache-bigtop-user-guide/apache-bigtop-user-guide.html>`__)
installation. There are several binaries spread out, with
interdependencies, depending on the compiler version or library version,
without standard paths, and users making a even larger mess... where did
I hear about it before?

I expected that with the amout of resources that are being poured on the
cloud projects, some form of organization or standardization would have
happened. But no luck: all is still downloading binaries and compiling
tons of disconnected but interdependent libraries, only with more levels
of abstraction. Yes, the abstraction levels help the user, as he doesn't
need anymore to know about if the processor has SSE3 or SSE4.2. Yes, now
devops can be both programmers and sysadmins. Yes, you don't have to buy
new machines, install them, plug the cables - you can just go to the AWS
console and click moar instances. But someone, on the end, has to move
all this to production, keep it working, plan on how this will grow, and
fix it when it breaks - and it will break, trust me.

Oh, but there's `OpenStack <https://www.openstack.org/>`__\ to the
rescue! Well, not really. I'm also not going to go deep into OpenStack,
but suffice to say that OpenStack is more an orchestration service than
what I'm looking into here.

And oh, there's Docker/Vagrant/CoreOS/etc containers! Well, that's also
an issue that I think is not the focus of this discussion. During the
HPC era, usually the application deployment consisted of: configuring
the computing nodes to communicate, share the data using a dedicated
network connected to a RAID server and running a binary on a NFS share.
Things got way more complicated because they are more complicated:
connection to several databases, web services, what not. But in the end
the problem is the same: how to deploy an environment that you can
maintain and fix? These technologies help immensely on empowering the
developer to create more complex solutions and abstract more, especially
parallel computations, but they actually make the maitain and fix part
way more complicated, from the sysadmin perspective. That's why I'm not
trying to address again these tools: they solve another problem, and
anyway, you have to configure these containers with the same binaries
and libraries, that need to be compiled, going back to the initial
problem!

So, is there a way to solve this mess? Unfortunately, I don't know. I've
been sidelining all these issues on the day to day at work, adding
binaries and virtualenvs when needed, but this will explode soon or
later. I just think that this problem is not being looked with much
care, especially on the startup world, or just being pushed to the new
`shiny new
thing <https://anotherlifeform.files.wordpress.com/2015/07/7d267-11359006_420191058182770_2015412754_n.jpg>`__\ that
will solve everything with more abstraction. What to do? Maybe to think
about these points when deploying your cluster, playing better with the
basic distributions and contributing more, and the distros trying not to
suffer from NIH syndrome would help.

I'm all ears for suggestions!
