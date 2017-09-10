Good-bye pass, hello Enpass
###########################

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds
:status: draft

Objetivo: explorar o conjunto de dados para

- Aumentar o entendimento do conjunto de dados
- identificar a estrutura subjacente
- identificar e filtrar quais variáveis são relevantes ao problema
- detectar outliers e anormalidades
- sumarizar os valores das variáveis e sua possível estrutura
- apresentar possíveis modelos de descrição das variáveis

Dados estes objetivos, os resultados esperados (entregáveis) da análise exploratória são
- Descrição do comportamento, de forma geral, dos dados e do fenômeno subjacente
- Parâmetros e modelos inferidos dos dados

Abordagens:
- Gráfica: tipos diferentes de gráficos (linha, boxplot, histograma, scatter, etc) dos dados brutos
- Sumária: gráficos e números de estatísticas (mínimo, máximo, média, mediana, maior e menor quartil, desvio padrão)

Sequência de etapas:
Problema => Dados => Análise => Modelo => Conclusões

Problema:
Definição do problema a ser abordado a partir dos dados.

Dados:
Dados a serem explorados. Preferencialmente devem ser conjuntos completos, não amostras.

Análise:
A análise deve conter as transformações de dados necessárias e cumprir os objetivos descritos acima.

Modelo:
Não se impôe um modelo a priori nos dados. Os dados devem fornecer a base para a inferência de um modelo. Após a identificação de um modelo, o mesmo dever ser usado para obter mais entendimento do processo sendo estudado e avaliar a consistência de algumas predições simples, com resíduos, por exemplo.

Métodos:
- Estatísticas descritivas do conjunto das 7
- Análise de correlação entre variáveis
- Redução de dimensionalidade por clusterização
- Gráficos, agrupados por variável e por descrição
- Comentários do analista

Especificamente para séries temporais,
- Autocorrelação
- Detecção de sazonalidade
- Tendência e inclinação
- plot de atraso (lag plot)
- plot por índice
- plot espectral

Referências:
http://users.ics.aalto.fi/sami/thesis/node7.html
http://edutechwdefaultiki.unige.ch/en/Methodology_tutorial_-_exploratory_data_analysis
https://en.wikipedia.org/wiki/Exploratory_data_analysis
http://cll.stanford.edu/~langley/cogsys/behrens97pm.pdf
http://www.stat.cmu.edu/~hseltman/309/Book/chapter4.pdf
http://www.rug.nl/research/portal/files/10217489/c4.pdf
http://trrjournalonline.trb.org/doi/10.3141/1926-14
http://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm
http://www.amazon.com/Exploratory-Data-Analysis-John-Tukey/dp/0201076160
