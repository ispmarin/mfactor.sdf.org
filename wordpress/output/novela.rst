Novela
######
:date: 2009-04-12 23:02
:author: ispmarin
:category: rede, segurança, Uncategorized
:tags: history, net, security
:slug: novela
:status: published

A história do DNS do Virtua comprometido continua. Eis um scan das
portas da famigerada máquina na Coréia:

++++++++++++++++++++++++

nostromo:~$ nmap -P0 210.205.6.50

Starting Nmap 4.68 ( http://nmap.org ) at 2009-04-12 22:51 BRT

ispmarin@nostromo:~$ nmap 210.205.6.50

| Starting Nmap 4.68 ( http://nmap.org ) at 2009-04-12 22:52 BRT
|  Interesting ports on 210.205.6.50:
|  Not shown: 1698 closed ports
|  PORT      STATE    SERVICE
|  21/tcp    open     ftp
|  22/tcp    open     ssh
|  25/tcp    open     smtp
|  80/tcp    open     http
|  110/tcp   open     pop3
|  135/tcp   filtered msrpc
|  136/tcp   filtered profile
|  137/tcp   filtered netbios-ns
|  138/tcp   filtered netbios-dgm
|  139/tcp   filtered netbios-ssn
|  199/tcp   open     smux
|  445/tcp   filtered microsoft-ds
|  3128/tcp  filtered squid-http
|  3306/tcp  open     mysql
|  4444/tcp  filtered krb524
|  9876/tcp  open     sd
|  17300/tcp filtered kuang2

Nmap done: 1 IP address (1 host up) scanned in 141.190 seconds

++++++++++++++++++++

Com um sd aberto, há uma chance muito boa de ser uma máquina invadida. É
Windows, para variar...

Edit 23:39: kuang2 é uma espécie de vírus modificada para pegar senhas.
Lame. Resta saber o que vai virar a partir de agora. Sitrep agora está
em compasso de espera. Qualquer novidade, posto.
