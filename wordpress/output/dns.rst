DNS
###
:date: 2009-04-12 20:13
:author: ispmarin
:category: rede, segurança, Uncategorized
:tags: dns, dns poisoning, net, net security, sitrep, third post
:slug: dns
:status: published

Alerta: Walrus acabou de achar um provável DNS Poisoning no DNS do
Virtua **201.6.0.43. O post dele está em
http://stoa.usp.br/walrus/weblog/47454.html.**

****Estou confirmando agora as informações usando o dig nesse DNS contra
as informações do whois da RNP. Vou atualizar conforme mais informações
forem chegando.****

****Atualmente este DNS está derrubado! - correção 22:31: ainda está de
pé!!!
****

| ****Edit 20:16: o DNS 201.6.0.43 está derrubado, e o outro DNS para
  SP, 201.6.0.113, está recusando acessos via dig.****
|  **Se você estiver no linux, teste os seus dns da seguinte forma:**

dig @<nameserver> <site de banco>

**assim:** dig @189.7.80.15 www.bradesco.com.br

**e vejam se a informação bate com a do whois brasileiro:**

whois www.bradesco.com.br

| **Edit 20:22: esse erro continua sendo confirmado por Walrus a partir
  de um virtua de SP. Estamos montando os logs para enviar para a RNP**
|  **Edit 20:32: confirmado que o IP é sul-coreano, e o site é uma
  reprodução fiel do site do bradesco - Walrus está checando outros
  sites nesse DNS, eu estou tentando, mas aqui de SC está dando time
  out**

| **Edit 21:40: Report de segurança foi enviado para a RNP, estou
  tentando entrar em contato com o SAC do Bradesco, e não tem
  ninguém!!!**
|  **Edit 21:44: Consegui entrar em contato com uma atendente do
  Bradesco. Ela anotou os dados que eu passei e disse que a equipe do
  internet banking funciona de segunda  a sábado (!!!). Pelo menos ela
  anotou, e disse que vai retornar com informações. Agora, passo de
  aguardo.**

**Edit 22:16: O Daniel sugeriu ligar para a Net. No telefone com eles
agora.**

**Edit 22:21: O Rafael Walrus postou algo mais detalhado em
http://stoa.usp.br/calsaverini/weblog/47461.html.Email para a Folha foi
enviado.
**

**Edit 22:27: a atendente da NET não consegue me transferir para alguém
que saiba o que é um incidente de segurança!**

**Edit 22:33: A mulher do setor técnico da NET DESLIGOU na minha cara.**

**Edit 22:45: consegui falar com uma atendente da NET, e ela disse que
este assunto está sendo verificado. Mas o Rafael ainda consegue fazer
dig no DNS comprometido, e o ip errado continua lá.**
