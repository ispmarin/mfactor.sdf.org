Atendentes no incidente de poisoning do NET Virtua - 6
######################################################
:date: 2009-04-14 00:12
:author: Ivan Marin
:category: network
:tags: call center, dns, internet, net, security, virtua
:slug: 2009_04_14_operators
:status: published

Uma das coisas mais incríveis do evento de ontem à noite (O DNS
Poisoning) do Virtua foi o tipo de resposta que obtive das atendentes
dos SACs. A primeira atitute, como pode ser visto abaixo no sitrep, foi
tentar descobrir e confirmar o que estava ocorrendo, e tentar ver se
algo mais estava afetado. Após isso, comecei a ligar para os serviços de
atendimento. Primeiro foi o email para a RNP, confirmando o incidente de
segurança e enviando os logs produzidos por mim e pelo Rafael Walrus.
Esse é o procedimento padrão nesses casos, já que fica meio difícil
enviar um log via telefone.

Logo após isso, comecei, junto com o Walrus, a procurar um telefone para
entrar em contato com o Bradesco. Afinal, era o site deles que estava
sendo clonado... consegui depois de uma ligação falar com uma atendente.
Ela não pareceu surpresa, mas não sabia sobre o que eu estava falando.
Ela conseguiu entender que tinha a ver com o site do netbanking, e
tentou me transferir para o setor, mas este só funciona de segunda a
sábado. Como assim? Um incidente de segurança desse nível, não um spam
qualquer de clique aqui, mas um nome legítimo sendo desviado,  e não
havia ninguém que poderia me entender? Deixei, no final, meu nome e
todas as informações que consegui passar para ela. Ela disse que iria
encaminhar para o departamento responsável. Hum.

Em seguida, começou a novela da NET. Imagina-se que uma empresa
prestadora de serviços de internet tenha um setor responsável pela
segurança da rede. E afinal, era o servidor de DNS *deles* que estava
comprometido. A primeira mulher que me atendeu não acreditava no que eu
estava falando. Ela ria, sem saber o que estava acontecendo. Eu tentava
falar para ela que queria ser transferido para o setor de segurança, de
incidentes de segurança, no desespero apelei até para me transferir para
o setor de pirataria, mas nada. Ela simplesmente não conseguia entender
o que eu estava falando, coisas como DNS, página clonada. E eles são
*provedores de internet*.

A segunda ligação para a NET foi um pouco pior: depois da mulher não
entender mais uma vez o que eu estava falando, ela disse que ia falar
com o superior e desligou na minha cara. Simples assim. Desligou.

Na terceira vez eu consegui falar com o setor técnico. A moça pareceu me
entender melhor o que estava ocorrendo, mas mesmo assim, não sabia
direito. Foi perguntar para o supervisor, e voltou, depois de alguns
minutos, dizendo que as providências já estavam sendo tomadas. Ufa.

Logo após isso, o Walrus testou mais uma vez o dig no DNS deles, e ele
ainda estava de pé, *com o endereço errado de ip ainda.* Grandes
providências estavam sendo tomadas!

Na manhã seguinte, o pessoal do CAIS respondeu dizendo que ia entrar em
contato com o Bradesco sobre o site. Não entendi muito bem, pois o
problema estava no DNS do virtua, mas achei que pelo menos alguma
providência iria ser tomada. O servidor coreano saiu do ar, e o DNS do
Virtua voltou a apontar para o endereço certo.

Fico na dúvida sobre o que estava acontecendo, e por que demorou tanto
tempo para ter alguma ação. Será que estavam investigando a origem do
ataque? Será que estavam tentando pegar quem tinha feito isso, e
precisavam deixar o DNS intacto? Coletando evidências? Acordando o
responsável? Consertando a falha sem derrubar um servidor DNS? E os
outros servidores de backup? Iriam ser inundados se desligassem o
servidor comprometido? Será que acharam que era fraude ou trote?

Fico sem saber.
