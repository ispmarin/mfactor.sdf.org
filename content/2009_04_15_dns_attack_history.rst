Histórico de ataques a DNS - 7
##############################
:date: 2009-04-15 17:19
:author: Ivan Marin
:category: network
:tags: fail, net, security, dns
:slug: 2009_04_15_dns_attack_history
:status: published

O Gustavo acabou de relatar um post em um fórum
(http://macmagazine.com.br/forum/index.php?showtopic=10070) dizendo que
aconteceu antes. Mesmo comportamento do que ocorreu agora, troca direta
do DNS. E com o Virtua, mas agora com outro DNS, os 201.6.0.112 ou
201.6.0.113. O post é de novembro do ano passado. O Rafael, que tem
acesso aos DNS do Virtua por estar em SP, acabou de testar tanto
www.bradesco.com.br quanto www.bradescoprime.com.br no 112 e 113 e disse
que está ok. Mas o 43...

17:12 o Rafael constatou que o .43 está retornando SERVER FAIL para
www.bradesco.com.br:

<<>> DiG 9.5.0-P2 <<>> @201.6.0.43
`http://www.bradesco.com.br <http://www.bradesco.com.br/>`__

; (1 server found)

;; global options: printcmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 30233

;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:

;www.bradesco.com.br. IN A

;; Query time: 45 msec

;; SERVER: 201.6.0.43#53(201.6.0.43)

;; WHEN: Wed Apr 15 17:11:07 2009

;; MSG SIZE rcvd: 37

bradescoprime.com.br no 112 e 113 e disse que está ok. Mas o 43... o
www.bradesco.com.br não está sendo retornado agora, 17:16, ou seja,
estão removendo a entrada e colocando o novo. Mas estão consertando a
falha de segurança que está permitindo isso?
