Setting up shop with Pelican, Gogs and SDF
##########################################

:date: 2010-10-03 10:20

:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds
:status: draft

- ssh configuration
- pelican export wordpress
- pelican configuration
- pelican makefiles
- copy sites
- folder contnet organization
- html
- Gogs installation
    - go compiler installation
    - gogs
- gitea installation
download the source package using

go get -insecure -v -d -u code.gitea.io/gitea

then checkout a stable branch with

git tag -l
git checkout v1.0.1

next build

- generate SSL
- SSL configuration
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mfactor.key -out mfactor.crt
http://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate
