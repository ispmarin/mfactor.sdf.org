Novidades do DNS poisoning do Virtua - 5
########################################
:date: 2009-04-14 20:47
:author: Ivan Marin
:category: network
:tags: dns, net, security, segurança
:slug: 2009_04_14_aftermath
:status: published

Acabou de sair um artigo na Folha Online sobre o ataque no DNS do Virtua
(o que vem sendo postado aqui no anotherlifeform:)

http://www1.folha.uol.com.br/folha/informatica/ult124u550572.shtml

"A reportagem teve acesso a um e-mail no qual os ataques são confirmados
pela equipe de segurança do banco. "Temos recebido relatos desse mesmo
problema de usuários do Vírtua que o sistema desse provedor está sendo
abusado [sic] para ataque a nossa instituição. Já acionamos nossos
colegas da NET para que solucionem o problema o quanto antes.""

Por que isso não foi informado aos usuários, tanto da NET quanto do
Bradesco? Porque não pudemos falar diretamente com o pessoal do banco ou
da NET, ou pelo menos informados que eles sabiam? E quanto tempo isso
levou? Outro dado interessante: quantos usuários Virtua usam esse DNS em
São Paulo?

Se você quiser checar, dê uma olhada na sua conexão com o Virtua e veja
qual é o DNS que você usa. No linux é fácil:  no terminal digite

cat /etc/resolv.conf

deve aparecer algo como

nameserver 200.202.17.1

veja se este número acima bate com o servidor DNS afetado: 201.6.0.43.
Se bater, você estava usando este servidor de DNS. No Windows, clique em
Propriedades de Rede-> Conexão (alguma coisa)-> TCP/IP -> E veja o DNS. 
Segundo a reportagem da Folha, a falha já foi corrigida. Mas afinal,
qual foi a falha? O Virtua atualizou seus servidores de DNS com os
updates do BIND, se é que eles usam BIND? (na noite de domingo, o Daniel
fez um nmap e descobriu que os servidores DNS do Virtua rodam Windows
Server...........)

Como já postado aqui também, a Telefônica foi alvo de ataque em seus
DNS. Mas enquanto o ataque na Telefônica foi um provável DOS (Denial Of
Service), que os usuários podem sentir diretamente, o ataque no servidor
DNS do Virtua é muito mais sutil. Há quanto tempo ele estava
comprometido? Há alguma relação?
