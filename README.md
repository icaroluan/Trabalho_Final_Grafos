# Trabalho Final Grafos

## Passo para execução
- Primeiro tenha uma versão python instalado [link tutorial](https://realpython.com/installing-python/)
- Depois de o comando no pip install -r requirements.txt
- Compile o arquivo como o comando python gerador_modelo_ba.py

## Bibliotecas e Pacotes
- Preve introdução

### Tkinter
- O pacote tkinter (“interface Tk”) é a interface Python padrão para o kit de ferramentas Tk GUI. Tanto o Tk quanto o tkinter estão disponíveis na maioria das plataformas Unix, bem como em sistemas Windows. (Tk em si não faz parte do Python; é mantido no ActiveState.)

[Link para documentação Tkinter](https://docs.python.org/3/library/tkinter.html)

### Matplotlib
- Matplotlib é uma biblioteca abrangente para a criação de visualizações estáticas, animadas e interativas em Python.

[Link para documentação Matplotlib](https://matplotlib.org/stable/contents.html)

### Community
- Este pacote implementa detecção de comunidade.
- O nome do pacote é comunidade, mas refere-se a python-louvain em pypi
- Utilizo esse pacote para obter a partição dos nós do gráfico que maximiza a modularidade, utilizando as heuristicas de Louvain. Sendo a partição de maior modularidade, ou seja, a partição mais alta do dendrograma gerado pelo algoritmo Louvain.

[Link para documentação Community](https://python-louvain.readthedocs.io/en/latest/api.html)

### Networkx
- NetworkX é um pacote Python para a criação, manipulação e estudo da estrutura, dinâmica e funções de redes complexas.

Software para redes complexas:
 * Estruturas de dados para gráficos, dígrafos e multigrafos
 * Muitos algoritmos gráficos padrão
 * Estrutura de rede e medidas de análise
 * Geradores para gráficos clássicos, gráficos aleatórios e redes sintéticas
 * Os nós podem ser "qualquer coisa" (por exemplo, texto, imagens, registros XML)
 * As bordas podem conter dados arbitrários (por exemplo, pesos, séries temporais)
 * Licença BSD de código aberto com 3 cláusulas
 * Bem testado com mais de 90% de cobertura de código
 * Os benefícios adicionais do Python incluem prototipagem rápida, fácil de ensinar e multiplataforma

[Link para documentação Networkx](https://networkx.org/documentation/stable/tutorial.html)

Na implementação da ferramenta foi usado o gerador de grafo do pacote Networkx [barabasi_albert_graph](https://networkx.org/documentation/stable/_modules/networkx/generators/random_graphs.html#barabasi_albert_graph)

## Introdução sobre Modelo Barabási-Albert


O tema de redes complexas podem ser aplicados em varios estudos com na area de transporte, tecnologia a de saúde.
Um dos mais famosos modelos de redes complexas e do de Barabási-Albert, seu proposito inicialmente foi para a reprodução das prorpiedades da rede mundial de computadores. A partir desse modelo é contruido redes atráves de sucessias adições de nós, utiizando o princípio da adesão preferencial. O principio afirma que a probabilidade de um nó receber um vizinho é proporcional ao seu número de vizinhos que esse nó já possui. O resusltado principal do modelo é uma distribuição de grau que segue uma [lei de potência](https://en.wikipedia.org/wiki/Power_law). Quando ocorre que diversas redes reais apresentam distribuições de grau que se aproximan de uma lei de potência o princípio de adesão preferencial do modelo de Barabási-Albert, passou a ser considerado com um pricnipais mecanimos de formação das redes reais.

[Fonte](https://lume.ufrgs.br/handle/10183/150235)

## Corretude

[Link Apresentação Youtube](https://www.youtube.com/)