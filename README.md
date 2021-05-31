# Trabalho Final Grafos

## Passo para execução

#### Windows
- Primeiro tenha uma versão python instalada [link tutorial](https://realpython.com/installing-python/)
- Depois de o comando pip install -r requirements.txt
- Compile o arquivo com o comando python gerador_modelo_ba.py

#### Linux
 - Após o primeiro passo de instalação do python
 - Para instalar o Tkinter de o comando sudo apt-get install python3-tk
 - Para instalação da Matplotlib de o comando sudo apt-get install python3-matplotlib [link para pacotes linux](https://matplotlib.org/stable/users/installing.html#linux-package-manager)
 - Para instalar o pacote Python-louven de o comando pip3 install python-louvain
 - Para instalar o pacote NetworkX de o comando pip3 install networkx

* Obs1: Ocorrendo problemas na instalação do tkinter para a versão linux [Link stackoverflow com explicação](https://stackoverflow.com/questions/4783810/install-tkinter-for-python)

* Obs2: Ocorrendo erro na instalação do tkinter seguir tutorial neste [link](https://tkdocs.com/tutorial/install.html)

## Bibliotecas e Pacotes
- Breve introdução

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
Um dos mais famosos modelos de redes complexas é a de Barabási-Albert, seu proposito inicialmente foi para a reprodução das propriedades da rede mundial de computadores. A partir desse modelo é construido redes atráves de sucessivas adições de nós, utilizando o princípio da adesão preferencial. O principio afirma que a probabilidade de um nó receber um vizinho é proporcional ao seu número de vizinhos que esse nó já possui. O resusltado principal do modelo é uma distribuição de grau que segue uma [lei de potência](https://en.wikipedia.org/wiki/Power_law). Quando ocorre que diversas redes reais apresentam distribuições de grau que se aproxima de uma lei de potência o princípio de adesão preferencial do modelo de Barabási-Albert, passou a ser considerado com um dos principais mecanimos de formação das redes reais.

[Fonte](https://lume.ufrgs.br/handle/10183/150235)

## Corretude

### Algoritmo

Para o seu processo de crescimento inicia-se com uma rede arbitrária de n0 nós. Então novos nós são adicionados a rede, um a um, e cada um desses novos nós faz conexões com outros x nós já existentes, onde x é uma variável que pertence ao modelo. A probabilidade do novo nó se conectar a um outro nó i qualquer já presente na rede é proporcional ao número de ligações que o nó i possui. Formalmente, a probabilidade pi de que o novo nó irá se conectar a um vértice i que já existe é representado na imagem abaixo.
Sendo o valor de ki o grau do nó i e a soma no denominador, realizada sobre todos os nós j já existentes na rede, é a normalização da probabilidade. Esse processo de escolha de conexão é repetido para cada uma das ligações x que o novo nó irá fazer.

![Formula de pi](https://github.com/icaroluan/Trabalho_Final_Grafos/blob/main/algoritmo1.PNG)

Este formato os nós com o grau maior, sendo aqueles com muitas conexões, tendem a acumular rapidamente ainda mais ligações, enquanto nós com grau baixo, contendo poucas ligações, tendo uma baixa probabilidade de serem escolhidos como o destino para um novo link. Assim, os novos nós tem uma preferência para unir-se aos nós já fortemente ligadas. Note também que há um valor mínimo para o grau de um nó, sendo ele igual ao parâmetro x. O grau médio <k> da rede pode ser calculado analiticamente, sendo <k> = 2x.

[Fonte modelo Barabási Albert](https://pt.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model)

[Link Apresentação Youtube](https://youtu.be/Nevv6gcbm8k)