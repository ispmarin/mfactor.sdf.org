Using Kwallet to store credentials for git
##########################################

:date: 2017-02-02
:tags: os
:category: debian
:slug: 2017_02_02_kwallet_git
:authors: Ivan Marin
:summary: How to avoid typing your password for git HTTPS

I switched my repos to Gogs and now I'm using HTTPS to push. 
The thing is that I can't use my ssh keys for that, so I have to type the password.
There is a way to use the KWallet to store these credentials and tell Git to use KWallet for them:

```
sudo apt-get install ksshaskpass
```

and then configure git as

```
git config --global core.askpass /usr/bin/ksshaskpass
```

and done. Quite helpful. 
