Core-Node
#########
:date: 2009-05-06 19:56
:author: ispmarin
:category: productive
:tags: beowulf, hpc, linux
:slug: core-node
:status: published

Lendo hoje a lista do pessoal do beowulf.org, veio uma discussão
interessante, pelo menos no âmbito de computação paralela: a diferença
entre nó e núcleo, *node* e *core.* A discussão segue mais ou menos
desta forma: qual é a fronteira entre um núcleo e um nó? Um núcleo de um
processador com vários é um nó ou não?

Algumas definições: core, em português núcleo, é como são chamados os
elementos de processamento completos que integram um processador (um
chip). Um processador Intel QuadCore é um processador com quatro núcleos
independentes (mas que compartilham o cache L2, no esquema 2x6M, por
exemplo. O cache L1 é independente para cada núcleo). A saída do
processador com quatro cores para o barramento e acesso à memória é
única para os quatro núcleos (ou com caminhos iguais, como faz o
HyperTransport da AMD e os novos i7 da Intel). Mais sobre isso mais
tarde.

Processador então vira um termo híbrido, podendo significar cada unidade
de processamento completa (um núcleo, por exemplo) ou um chip, que pode
ter um ou mais núcleos.

Pensando em processos
`MPI <http://www.mcs.anl.gov/research/projects/mpi/>`__, cada processo
faz a completa comunicação, com o seu conjunto de dados. Mais de um
processo pode ser executado em um mesmo núcleo, e a comunicação entre
processos pode variar de  o que torna definir via número de processos em
execução algo indefinido. Portanto, no nível de abstração do MPI, um
core é abstrato, e um node pode ter mais de um processo MPI rodando.

Pensando então em comunicação dentro de uma pastilha, um core é um node
- ou seja, cada núcleo de um processador via um node de um processo
paralelo. Lembrando, inclusive, que problemas que ocorrem em um esquema
mais "tradicional" - computadores ligados via rede, digamos, 10 GbE -
como congestionamento do bus  - ocorre mesmo em um esquema core-núcleo.

Para tratar esta possível heterogeneidade - a latência entre uma
mensagem entre núcleos é diferente da latência entre um nó e outor
conectado via rede, etc - uma abordagem mista vem sendo desenvolvida:
threads, ou OpenMP, para comunicação "local" - dentro de uma pastilha,
entre cores - e Message Passing entre nós - computadores ligados através
de uma rede.

O importante no projeto de uma aplicação é esta diferença estar clara e
o projeto a levá-la em conta quando for considerar tanto a localidade
dos dados quanto à comunicação e limites nos mesmos.
