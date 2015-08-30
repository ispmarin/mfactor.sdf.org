Inacreditável
#############
:date: 2009-04-15 11:51
:author: ispmarin
:category: rede, segurança
:tags: again!, net, security
:slug: inacreditavel
:status: published

Um user no blog do Rafael percebeu de novo que o DNS do Virtua foi
comprometido (http://stoa.usp.br/calsaverini/weblog/47528.html). Olha o
comentário:

`Aivuk (AKA Walrus) <http://stoa.usp.br/walrus/>`__ escreveu:

| Pelo vistoo pessoal da Net não resolveu o problema ainda de forma
  definitiva. Olha a resposta do fatídico servidor DNS às 21:00 de
  terça:
|  [/home/walrus] dig @201.6.0.43 www.bradesco.com.br

| ; <<>> DiG 9.6.0-P1 <<>> @201.6.0.43 www.bradesco.com.br
|  ; (1 server found)
|  ;; global options: +cmd
|  ;; Got answer:
|  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 55339
|  ;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL:
  1

| ;; QUESTION SECTION:
|  ;www.bradesco.com.br.        IN    A

| ;; ANSWER SECTION:
|  www.bradesco.com.br.    5    IN    A    210.205.6.46

| ;; AUTHORITY SECTION:
|  bradesco.com.br.    5    IN    NS    dns1.virtua.com.br.

| ;; ADDITIONAL SECTION:
|  dns1.virtua.com.br.    2417    IN    A    201.6.0.100

| ;; Query time: 18 msec
|  ;; SERVER: 201.6.0.43#53(201.6.0.43)
|  ;; WHEN: Tue Apr 14 18:01:34 2009
|  ;; MSG SIZE  rcvd: 95

Ou seja, tem um novo IP, do mesmo ISP sul coreano, comprometido. E o DNS
do Virtua (201.6.0.43) foi de novo comprometido.

# ENGLISH

| KRNIC is not an ISP but a National Internet Registry similar to APNIC.
|  The IPv4 address is allocated and still held by the following ISP,
|  or its Whois information is not updated after assigned to end users.

Please contact following ISP for further information.

| [ ISP Organization Information ]
|  Org Name      : SK Broadband Co Ltd
|  Service Name  : broadNnet
|  Org Address   : SK NamsanGreen Bldg. Jung-gu Namdaemunno 5(o)-ga
  Seoul

| [ ISP IPv4 Admin Contact Information ]
|  Name          : IP manager
|  Phone         : +82-2-106-2
|  E-Mail        : ip-adm@skbroadband.com

| [ ISP IPv4 Tech Contact Information ]
|  Name          : IP manager
|  Phone         : +82-2-106-2
|  E-mail        : ip-adm@skbroadband.com

| [ ISP Network Abuse Contact Information ]
|  Name          : manager
|  Phone         : +82-2-106-2
|  E-mail        : abuse@skbroadband.com

Estou tentando conseguir acesso a uma máquina no range de IPs do Virtua
em SP, com o Rafael, para testar esse DNS. E vou enviar mais uma vez um
relatório para o CAIS...
