Managing passwords with `pass`
==============================

:date: 2016-07-31 09:25
:modified: 2016-07-31 09:25
:tags: security, passwords
:category: Linux
:slug: 2016_07_31_manage_pass
:authors: Ivan Marin
:summary: How I stopped using LastPass and love pass

I've been thinking about dumping LastPass for a while now, especially after it was bought by
some company whatever. But the way that LastPass is useful is quite awesome:

- can generate passwords
- stores all passwords
- fill login forms automatically (the best feature for me)

So how can I replace it with something with at least similar functionalities but
under my control?

The answer to that is `pass <https://www.passwordstore.org/>`_. It stores the
passwords as encrypted text with `GPG <https://www.gnupg.org/>`_ on the local filesystem.
The feedback was so good that other people started using it and developed more
resources for it, as a `GUI <https://qtpass.org/>`_ and a `Firefox extension <https://github.com/jvenant/passff#>_`.

I'll describe how I managed to set it up.

GPG
----

First, let's set up the GPG key::

    sudo apt-get install gpgv2

and generate a key::

    gpg --gen-key

If the key process takes it too long because of the entropy generation,

    **We need to generate a lot of random bytes. It is a good idea to perform
    some other action (type on the keyboard, move the mouse, utilize the
    disks) during the prime generation; this gives the random number
    generator a better chance to gain enough entropy.
    Not enough random bytes available.  Please do some other work to give
    the OS a chance to collect more entropy! (Need 210 more bytes)**

install the `rng-tools`:

    sudo apt-get install rng-tools

and generate entropy using the `command <http://serverfault.com/questions/214605/gpg-not-enough-entropy>`_

    sudo rngd -r /dev/urandom

to generate enough entropy for GPG.

pass
----

So now let's install `pass`:

    sudo apt-get instal pass

and create a password store:

    pass init <email used to generate the GPG key>

You can now start adding passwords. As I said, I used LassPass heavily, so I had tons of
passwords stored. To convert them I exported on LastPass my passwords to a CSV and used
`this tool <https://git.zx2c4.com/password-store/tree/contrib/importers/lastpass2pass.rb>`_
to import the passwords to pass. I now could access all my passwords from the command line.

pass with git
-------------

But one of the nicest things about Lastpass is be able to synchronize the passwords over the web.
pass can manage the passwords as a git repository, so that's the route I chose. After importing
the passwords I initialized the password store as a git repository:

    pass git init

Now the changes on the password file would be automatically commited. Using my `meta array <http://sdf.org/?tutorials/metaarray>`_
account on `SDF <http://sdf.org>`_, I created a bare remote repository on it (git init --bare) and added as a remote repository
on my pass folder:

    pass git remote add origin ma.sdf.org:~/git/pass

where the bare git repository is at `~/git/pass`. After that a simple

    pass git push -u --all

commited all passwords to the repo.

Alternatives to access the passwords
-------------------------------------

There is a Firefox `extension <https://addons.mozilla.org/pt-BR/firefox/addon/passff/>`_ that can access
the stored passwords. It's almost as good as Lastpass, but only for Firefox.
