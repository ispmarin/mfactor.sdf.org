Different SSH keys for Different Hosts
######################################

:date: 2017-01-10 10:20
:tags: ssh, keys
:category: system
:slug: 2017_01_10_ssh_keys_hosts
:authors: Ivan Marin
:summary: Keep your keys private and separated

The idea is simple: each of the SSH keys should grant access to only one system.
The rationale is that if one of the keys is compromised the other keys are not. Simple, really.

To do it, the first step is to generate the keys separatedely:

.. code:: bash

    ssh-keygen -t rsa -b 4096 -C "yourmail@mail.com" -f ~/.ssh/github


This command generates a key pair with 4096 bits and the email above as signature.
The key will be on the full path and the filename,
something like :code:`/home/user/.ssh/github`.

Now the `config` file for `ssh` must be configured to correspond to the expected keys:

.. code:: bash

    Host github.com
        IdentityFile ~/.ssh/github

    Host bitbucket.com
        IdentityFile ~/.ssh/bitbucket

and that´s it. For each server now a different key is used. A good reference is
`<https://confluence.atlassian.com/bitbucket/configure-multiple-ssh-identities-for-gitbash-mac-osx-linux-271943168.html>`__
