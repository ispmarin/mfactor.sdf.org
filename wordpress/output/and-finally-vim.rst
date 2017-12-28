And finally, Vim
################
:date: 2012-09-18 17:17
:author: ispmarin
:category: ciência
:tags: computadores, config, debian, different computers, linux, science, software científico, vimrc
:slug: and-finally-vim
:status: published

After Eclipse and Eclipse CDT giving me finger again, I thought that
would be nice to ask my fellow programmers for some help, and we had an
interesting discussion on google+ about which editor to use to program.
After much debate (and a few hours struggling with Emacs, oh god why), I
settled with vim. WHAT? VIM? That 30 years old editor that you have to
time crazy commands? Yep. Let me explain why. And PLEAAASE, this is not
\_another\_ vim vs emacs flamewar.

I needed a flexible editor, especially because I sometimes have to work
from different computers and platforms, and very little time to set up
the needed configuration. Eclipse filled this role because it was simply
download it, import the cloned project files, and done. Emacs is a hit
or miss target: there are dozens of versions of it, and it seems that to
configure it in different platforms is a pain in the behind. Vim is
everywhere, and after a clever suggestion to keep my configuration files
in a `git repository <https://github.com/mfactor/vimconfig>`__, I saw
the light. Vim it is!

So, after a recommendation of my fellow programmer @rcalsaverini, I
started populating my .vim with some plugins. First, the colortheme,
molokai. pathogen is a must. Everything running and dandy, and now it
comes the configuration
part. \ https://github.com/mfactor/vimconfig/blob/master/vimrc shows how
it stands so far, and as it is commented, I leave it at that.\ `This
blog <http://nvie.com/posts/how-i-boosted-my-vim/>`__ helped setting
some options.

But now comes the hardest part: retraining all the keystrokes and
movements that I had before with Eclipse, and change them to Vim. This,
I'm still training and learning. So far, :tabnew (:tn with the remap) is
awesome, and CTRL + DOWN and + UP is good too. With vim-fugitive,
:Gwrite, :Gstatus and :Gcommit are awesome.

Need to compile? No fear:

:make

Does the job. Errors? Time to call

:copen

, and it shows all the errors and warnings, jumping to the line where
the error occured.
