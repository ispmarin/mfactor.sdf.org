PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=/home/ispmarin/profissional/projetos/mfactor.sdf.org
INPUTDIR=$(BASEDIR)/html
OUTPUTDIR=$(BASEDIR)/html
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
STATICDIR=$(BASEDIR)/assets

SSH_HOST=ma.sdf.org
SSH_PORT=22
SSH_USER=mfactor
SSH_TARGET_DIR=/meta/m/mfactor/html/

BLOGDIR=$(BASEDIR)/blog
ESPODIR=$(BASEDIR)/espondilite

MAKE=make
CP=cp

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '   make s3_upload                      upload the web site via S3         '
	@echo '   make cf_upload                      upload the web site via Cloud Files'
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish:
	$(CP) -rf $(STATICDIR)/* $(OUTPUTDIR)
	@echo ' '
	$(MAKE) -C $(BLOGDIR) html
	@echo ' '
	$(MAKE) -C $(ESPODIR) html

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate serve serve-global devserver stopserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
