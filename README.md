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

** Sera alterado com minha compreenssão do tema 

Redes Complexas podem ser utilizadas para estudar uma variedade de assuntos, desde problemas
tecnológicos a de saúde pública. Um dos modelos de redes complexas mais famoso é o modelo de
Barabási-Albert, proposto inicialmente para reproduzir propriedades da rede mundial de computadores. Este modelo constrói redes através da sucessiva adição de nós, seguindo o princípio da
adesão preferencial. Este princípio afirma que a probabilidade de um nó receber um vizinho é proporcional ao número de vizinhos que esse nó já possui. O principal resultado deste modelo é uma
distribuição de grau que segue uma lei de potência. Uma vez que diversas redes reais apresentam
distribuições de grau que se aproximam de uma lei de potência o princípio de adesão preferencial
do modelo de Barabási-Albert passou a ser considerado como um dos principais mecanismos por
trás da formação das redes reais. A comparação dessas redes com o modelo de Barabási-Albert é
controversa, uma vez que suas distribuições de grau não são perfeitamente aproximadas por uma
lei de potência. Entretanto, redes geradas atráves do próprio modelo apresentam desvios devido
a efeitos de tamanho finito. Nesse contexto, soluções analíticas capazes de descrever o modelo de
Barabási-Albert para redes pequenos são bem vindas, pois permitiriam compreender a extensão
dos efeitos de tamanho finito e, portanto, poderiam ser comparadas com redes reais pequenas.

[Fonte](https://lume.ufrgs.br/handle/10183/150235)

## Corretude

[Link Apresentação Youtube](https://www.youtube.com/)