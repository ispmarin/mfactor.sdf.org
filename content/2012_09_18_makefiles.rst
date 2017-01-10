Fiddling with Makefiles, for the last time
##########################################
:date: 2012-09-18 16:11
:author: Ivan Marin
:category: tools
:tags: compilation, computational physics, science
:slug: 2012_09_18_makefiles
:status: published

I was struggling with writing another makefile in my life, but it seems
that if you want to automate some tasks in vim, you have to write one.
I'll also use several compilers to check interoperability of the new
code that I'll be working, so creating a makefile, even if just for one
file, is worthwhile. But of course I never properly learned how to write
one by myself, so here is my post. First, automatic variables, directly
from the
`manual <http://www.gnu.org/software/make/manual/make.html#Automatic-Variables>`__:

``$@``\ The file name of the target of the rule. If the target is an
archive member, then ‘$@’ is the name of the archive file. In a pattern
rule that has multiple targets (see `Introduction to Pattern
Rules <http://www.gnu.org/software/make/manual/make.html#Pattern-Intro>`__),
‘$@’ is the name of whichever target caused the rule's recipe to be run.

``$%``\ The target member name, when the target is an archive member.
See \ `Archives <http://www.gnu.org/software/make/manual/make.html#Archives>`__.
For example, if the target is foo.a(bar.o) then ‘$%’ is bar.o and ‘$@’
is foo.a. ‘$%’ is empty when the target is not an archive member.

``$<``\ The name of the first prerequisite. If the target got its recipe
from an implicit rule, this will be the first prerequisite added by the
implicit rule (see `Implicit
Rules <http://www.gnu.org/software/make/manual/make.html#Implicit-Rules>`__).

| ``$?``\ The names of all the prerequisites that are newer than the
  target, with spaces between them. For prerequisites which are archive
  members, only the named member is used
  (see `Archives <http://www.gnu.org/software/make/manual/make.html#Archives>`__). 
|  ``$^``\ The names of all the prerequisites, with spaces between them.
  For prerequisites which are archive members, only the named member is
  used
  (see `Archives <http://www.gnu.org/software/make/manual/make.html#Archives>`__).
  A target has only one prerequisite on each other file it depends on,
  no matter how many times each file is listed as a prerequisite. So if
  you list a prerequisite more than once for a target, the value
  of \ ``$^`` contains just one copy of the name. This list
  does \ **not** contain any of the order-only prerequisites; for those
  see the ‘$\|’ variable, below. 
|  ``$+``\ This is like ‘$^’, but prerequisites listed more than once
  are duplicated in the order they were listed in the makefile. This is
  primarily useful for use in linking commands where it is meaningful to
  repeat library file names in a particular order.

``$|``\ The names of all the order-only prerequisites, with spaces
between them.

``$*``\ The stem with which an implicit rule matches (see `How Patterns
Match <http://www.gnu.org/software/make/manual/make.html#Pattern-Match>`__).
If the target is dir/a.foo.b and the target pattern is a.%.b then the
stem is dir/foo. The stem is useful for constructing names of related
files. In a static pattern rule, the stem is part of the file name that
matched the ‘%’ in the target pattern.

So the most used ones in the makefiles that I've seen are $@, $> and $^.
So, $@ means the name of the compilation rule, $^ means the source
files. For example,

::

    FC = gfortran
    FCFLAGS = -g -fbounds-check
    FCFLAGS = -O2
    IFC = ifort
    IFCFLAGS = -g 
    #FCFLAGS += -I/usr/include
    #LDFLAGS =
    SRC = bio-f.f
    bio-gfortran: $(SRC)
     $(FC) $(FCFLAGS) -o $@ $^ $(LDFLAGS)
    bio-ifort: $(SRC)
     $(IFC) $(IFCFLAGS) -o $@ $^ $(IFCFLAGS)
    gf: bio-gfortran
    ifort: bio-ifort
    # Utility targets
    .PHONY: clean veryclean
    clean:
     rm -f *.o *.mod *.MOD

What I'm doing basically is to tell to compile in this fashion: for the
rule bionapl-gfortran, $@ means this name and $^ means the source files.
So this line,

$(FC) $(FCFLAGS) -o $@ $^ $(LDFLAGS)

is use the compiler defined by FC with the compiler flags FCFLAGS using
the output name (-o $@) bio-gfortran and the source file ($^) that SRC
tells you to use. The line below is the same thing.

Note the line gf: bio-gfortran and the one below. This is just a
convenient renaming: instead of calling

make bio-gfortran

I can call and etc.

make gf

The meaning for the $@ and $^ can be a little more complicated with
build dependencies, but this is enough for now. I'm sure the programmers
on standby will provide better options and how to save changing the name
for each compilation, etc. Feel free to contribute!
