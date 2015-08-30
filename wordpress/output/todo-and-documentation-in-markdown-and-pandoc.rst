TODO and documentation in markdown and pandoc
#############################################
:date: 2013-02-28 11:27
:author: ispmarin
:category: ciência, computational physics, pesquisa, productive
:tags: code, conversion pdf, doxygen, markdown, pandoc, syntax highlight, todo
:slug: todo-and-documentation-in-markdown-and-pandoc
:status: published

Hi all,

Writing a TODO and some documentation for a code under development can
be a bit jarring at the beginning, especially when there's more than one
developer working on the same code. Things get even more interesting
when the other developer is not using any kind of VCS and we have to use
the good old fashioned code-by-email-what-changed-by-phone. After
working with git for a while, doing that can feel a little bit...
retrograde, but these are the conditions, and sometimes is best if we
don't change them.

So I thought for a long time how to keep track of the changes in this
scenario. Another detail: the code in question is not open source, so I
wouldn't be able to rely on github or other tools. So I decided to
use\ `markdown <http://daringfireball.net/projects/markdown/syntax>`__
to write the changes and
`pandoc <http://johnmacfarlane.net/pandoc/demos.html>`__ to generate a
PDF out of it. markdown syntax is quite simple, and pandoc can generate
very good PDFs out of them, so now is more important to concentrate on
writing the TODO than refining the tools.

The conversion from markdown to PDF is a breeze with pandoc:

    pandoc README -o readme.pdf

Done! What if we have some code in it, and want to highlight it? No
problem. Add a block code delimiter in markdown:

    | \`\`\` {.fortran .numberLines}
    |  call madfunction(i-1, 1, 1.0/dt, c)
    |  write(6,\*) "Running madfunction"
    |  \`\`\`

And convert it with pandoc:

 

    pandoc TODO.md  --highlight-style pygments -o TODO.pdf

And voilá! Code with syntax highlight in the PDF. Very, very, very
helpful. You can also change the syntax colors changing the option
<pygments> and use several different ones, as kate, zenburn, expresso,
etc.

Keeping the doc in markdown will also help when the code, or at least
parts of it, are uploaded to github or any other tracker. In the future,
if the documentation of the code itself is done in doxygen, for example,
the markdown can be included in the doxygen generation file. Neat.

 
