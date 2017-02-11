Self signed certificate with Git
##########################################

:date: 2017-02-03
:tags: os
:category: debian
:slug: 2017_02_03_self_sign_git
:authors: Ivan Marin
:summary: How to work with a self signed certificate and Git
:status: published

After setting up Gogs with a self signed certificate, I needed to commit using HTTPS now. To do that, Git must be instructed to ignore the certificate signature with

```
git config http.sslVerify false
```

that will disable the SSL verification for this session. An one-liner is 

```
git -c http.sslVerify=false clone https://domain.com/path/to/git
```

This `post <http://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate>`_ has more information about it. 
