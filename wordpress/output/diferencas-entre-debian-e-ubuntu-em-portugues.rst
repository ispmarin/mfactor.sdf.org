Diferenças entre Debian e Ubuntu, em Português
##############################################
:date: 2009-07-09 17:00
:author: ispmarin
:category: debian
:tags: debian, tradução, translation, ubuntu
:slug: diferencas-entre-debian-e-ubuntu-em-portugues
:status: published

Como prometido, aqui está a tradução em Português to texto do AndyC. Ele
educadamente permitiu que fosse traduzido. Qualquer erro ou omissão é de
minha inteira responsabilidade!

++++++++++++++++++++

Muitas diferenças: algumas grandes, algumas pequenas, mas todas podem
ser significantes. Eu \_NÃO\_ estou falando com direito oficial pelo
projeto Debian, ou mesmo o Ubuntu, de qual projeto eu também sou
contribuinte.

Quando o Ubuntu começou, um de seus desenvolvedores disse para mim "se
pudéssemos ter chamado de Debian para desktops, nós o teríamos feito."
Este era o foco deles naquela época; desde então ele aumentou
significativamente. Mas o foco principal do Ubuntu continua sendo a
experiência do usuário e um pequeno núcleo de aplicações.

Grandemente subjetivo, feito o mais distanciado quanto eu posso! :)

++Razões/Objetivos de Projeto++

Pacotes no Ubuntu main são altamentes polidos (trabalhados)[ed], muito
bem mantidos e a Canonical/Ubuntu fazem um esforço ímpar em garantir que
a experiência seja fácil para o usuário. Isto proporciona um ou mais dos
seguintes custos:

++Escolha++

Falta de escolha - você ganha um cliente de email ao invés de uma
escolha de vários "out of the box", por exemplo. Escolhas são feitas
para você - é um problema de suportabilidade. Debian fornece uma maior
flexibilidade pelo preço de maior complexidade ou a vontade de suportar
suas próprias decisões.

++Arquiteturas++

Falta de arquiteturas: se você não estiver usando Intel/AMD64 or,
possivelmente, ARM/Sparc/PPC (dependendo do release) - você não pode
rodar Ubuntu.  O Debian rodar em mais ou menos 11 arquiteturas significa
que a) o processo às vezes é lento b) o código é debugado c) é feito de
forma portável/consertos são contribuídos upstream.

++Relação Desenvolvedores/Usuários++

Canonical tem relativamente poucos desenvolvedores pagos, uma comunidade
de desenvolvedores voluntários altamente motivada, uma comunidade de
divulgação e um orçamento de propaganda e um número vasto de novos
usuários. Isto significa que seus desenvolvedores estão em uma
desvantagem numérica massiva com relação aos usuários e portanto
prioridades devem ser escolhidas. Pacotes no universe/multiverse podem
portanto receber menos atenção que aqueles no main do Ubuntu.

Na teoria, pelo menos, cada pacote Debian é igual e tem um mantenedor
conhecido e denomeado que tem interesse :) Isto significa que o Debian
faz o trabalho pesado de empacotar e suporte inicial para pacotes não
tão comuns - isto também significa que, se eu quero suporte para o R ou
CRAN, por exemplo, eu iria diretamente para o Debian por quê o
mantenedor tem um interesse pessoal ou profissional em vê-lo funcionar
bem como um sistema integrado.

++ Ciclos de Release++

"Nós demandamos áreas rigidamente definidas de dúvida e incertezas" -
Canonical tem estas áreas porque solta releases a cada seis meses. Esta
consistência tem um preço: usuários esperam novas features
(características, coisas)[ed] brilhantes e superbacanas a cada release e
o ciclo de desenvolvimento é bem curto mesmo. As edições com Suporte de
Longa Vida (Long Term Support, LTS)[ed] são lançadas a cada 18 meses e
são suportadas por três anos no desktop e cinco nas de servidor. Isto é
difícil. É \_muito\_ difícil suportar novo hardware com as edições de
longa vida. Releases "normais" podem misturar pacotes do Debian estável
com o testing, instável ou até mesmo experimental (características
superbacanas) mas ganham um tempo de teste bem curto.

Debian "lança quando pronto" mas depois suporta esta release até um ano
após o lançamento do \_próximo\_ release. 22 meses para lançar o Etch,
22 meses para lançar o Lenny + 12 meses = 56 meses. Progresso lento
através do testing até o release, com atualizações regulares com
consertos de segurança.

++Liberdade vs. Pragmatismo++

O Ubuntu às vezes toma uma atitude pragmática para o "software que
funciona" para os usuários. Eles também tem a habilidade, que o Debian
não tem, de entrar em acordos comerciais com outras companhias por ex.
Oracle/VMWare. [DFSG - não "licença apenas para o Debian"]. A Canonical
se beneficia do idealismo do Debian, mas o fluxo não pode escoar no
outro sentido :(

++Atualizações entre releases++

Você pode escutar muitas visões sobre isso. OPINIÃO SUBJETIVA A SEGUIR:
SENTIMENTO DE DENTRO E EXPERIÊNCIA EM PARTES IGUAIS. Ubuntu é mais
difícil de se atualizar limpamente entre as releases e pode ser na
verdade mais rápido se reinstalar. Você certamente pode pular uma
release portanto você não precisaria ir do 8.04, 8.10, 9.04, 9.10 (por
exemplo). Isto é parcialmente uma consequência do ciclo de
desenvolvimento curto visto acima. O Debian é \_muito\_ mais polido aqui
/SUBJETIVO

++Sumário++

Tudo isto é bem explicado no The Official Ubuntu Book e na entrevista
deMark Shuttleworth para a revista "Linux Format". Também vale a pena
ler newsgroups/fora e o planet.debian.org/planet.ubuntu.com para se
apreciar melhor as abordagens semelhantes e diferentes. Debian e Ubuntu
ambos tem pontos positivos: sua (algumas vezes complicada) simbiose -
ambas as distribuições compartilham desenvolvedores, por exemplo, mas
não necessariamente objetivos - mas o Debian ganha tanto quanto o Ubuntu
se eles conseguirem consertar o maldito bug #1 :)

Espero que ajude,

AndyC

++++++++++

E aí está. Os comentários em parêntesis com um [ed] depois foram termos
que acrescentei para tentar fazer um entendimento melhor. Mantive alguns
termos em inglês pelo uso corrente deles na área, ou para facilitar
mesmo (como o termo release).

Por favor, enviem correções/omissões/barbaridades que eu tenha feito!
