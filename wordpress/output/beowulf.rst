Beowulf
#######
:date: 2009-04-18 16:07
:author: ispmarin
:category: ciência
:tags: beowulf, computação, computing, hpc
:slug: beowulf
:status: published

| Não, não é o poema. Depois de um longo e tenebroso inverno sem mexer
  com Beowulf, recebi um email via lista debian-amd64 de uma dúvida
  sobre o que eu costumava fazer a tanto tempo (e durante tanto tempo):
  compilar bibliotecas, montar um cluster e rodar programas paralelos
  neles. A dúvida, ao que me parece, era sobre o caminho das bibliotecas
  nos nós. Geralmente um programa paralelo precisa de várias bibliotecas
  (por exemplo, BLAS, LAPACK, ScaLAPACK, GSL, MKL, etc etc etc), que
  precisam ser linkadas com o binário. Os nós, geralmente, não tem uma
  instalação completa, o que é bom - facilita muito a manutenção, entre
  outras coisas que ficam em outro post. Então existem dois jeitos de se
  executar um programa paralelo, via mpi (ch, ch2, lam, open) em um
  cluster: ou se compila de forma estática ou se distribui as
  bibliotecas via NFS, por exemplo (ou GPFS, Lustre, o que seja.).
|  O compilador da Intel é um pouco mais chato, mas no fundo se resume a
  ou distribuir as bibliotecas, ou se compila estático. E claro,
  assumindo que o ssh entre os nós é sem senha, usando o ssh-keygen.
