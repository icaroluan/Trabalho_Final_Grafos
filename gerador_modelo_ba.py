from tkinter import *
from tkinter import messagebox
import tkinter as tk
from matplotlib import pyplot as plt
from community import community_louvain
import networkx as nx


def check_N_M(n, m):
    if(  m>= 1 and m < n ):
        return False
    messagebox.showerror('Erro','Modelo deve ter m>=1 e m < n = {0}, m = {1}'.format(n,m))
    return True


def community_layout(g, partition, seed=42):
    pos_communities = _position_communities(g, partition, scale=3., seed=seed)
    pos_nodes = _position_nodes(g, partition, scale=1., seed=seed)
    pos = dict()
    for node in g.nodes():
        pos[node] = pos_communities[node] + pos_nodes[node]
    return pos

def _position_communities(g, partition, **kwargs):
    between_community_edges = _find_between_community_edges(g, partition)
    communities = set(partition.values())
    hypergraph = nx.DiGraph()
    hypergraph.add_nodes_from(communities)
    for (ci, cj), edges in between_community_edges.items():
        hypergraph.add_edge(ci, cj, weight=len(edges))

    pos_communities = nx.spring_layout(hypergraph, **kwargs)

    pos = dict()
    for node, community in partition.items():
        pos[node] = pos_communities[community]
    return pos

def _find_between_community_edges(g, partition):
    edges = dict()
    for (ni, nj) in g.edges():
        ci = partition[ni]
        cj = partition[nj]
        
        if ci != cj:
            try:
                edges[(ci, cj)] += [(ni, nj)]
            except KeyError:
                edges[(ci, cj)] = [(ni, nj)]
    return edges

def _position_nodes(g, partition, **kwargs):
    communities = dict()
    for node, community in partition.items():
        try:
            communities[community] += [node]
        except KeyError:
            communities[community] = [node]
        
    pos = dict()
    for ci, nodes in communities.items():
        subgraph = g.subgraph(nodes)
        pos_subgraph = nx.spring_layout(subgraph, **kwargs)
        pos.update(pos_subgraph)

    return pos

def generate_ba(n, m, seed):
    if check_N_M(n,m):
        messagebox.showinfo('Informação','Modelo de entrada padrão n = {0}, m = {1}'.format(50,1))
        return nx.generators.random_graphs.barabasi_albert_graph(50, 1, seed)
    else:
        return nx.generators.random_graphs.barabasi_albert_graph(n, m, seed)

def plot(G, seed, n, m):
    fig = plt
    fig.close()
    fig = plt.figure(num='Modelo BA n={0} e m={1}'.format(n, m))
    partition = community_louvain.best_partition(G, random_state=seed)
    pos = community_layout(G, partition, seed)
    nx.draw(G, pos, with_labels=True, node_color=list(partition.values()))
    # Sem o uso da heuristicas de Louvain para as partições
    #nx.draw(G, with_labels=True)
    return fig.show()

def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Grafo Modelo BA(Barabási Albert)")
        self.root.geometry('500x200')
        
        # Valores iniciais setados
        self.m = 1
        self.n = 50
        self.seed = 50
        
        frame_inputs = Frame(self.root)
        frame_labels = Frame(self.root)

        # Quantidade de Nós
        Label(frame_inputs, text = "Quantidade de Nós(n)").grid(row=0, column=0)
        self.n_entry = Entry(frame_inputs, width = 5)
        self.n_entry.grid(row=0, column = 2)
        Label(frame_labels, text = "O número de Nós(n) não pode ser menor que a quantidade de arestas").grid(row=0, column=0)
        
        # Número de Arestas
        Label(frame_inputs, text = "Número de Arestas(m)").grid(row=1, column=0)
        self.m_entry = Entry(frame_inputs, width = 5)
        self.m_entry.grid(row=1, column=2)
        Label(frame_labels, text="Número de arestas(m) tem que ser maior igual a 1 é menor que número de nos").grid(row=1, column=0)
        
        # Labels
        Label(frame_labels, text="Grafo com entrada padrão Número de nós = {0} e Número des arestas = {1}".format(self.n, self.m)).grid(row=3, column=0)

        # Botão
        button1 = Button(frame_inputs, text="Criar Grafo", command = self.update_values)
        button1.grid(row=3, column=0, pady=10)
        
        button2 = Button(frame_inputs, text="Sair", command = self.on_closing).grid(row=3, column=2)

        frame_inputs.pack()
        frame_labels.pack()

        self.root.bind("<Return>", self.update_values)
        self.plot_values()

        
        
        pass

    def validation_entry(self):
        if( self.n_entry.get().isdigit() and self.m_entry.get().isdigit()):
            return True
        else:
            messagebox.showerror('Erro','Entre apenas com números inteiros')
            return False

            
    def update_values(self, event=None):
        if self.validation_entry() == False:
            return None
        else:
            self.n = int(self.n_entry.get())
            self.m = int(self.m_entry.get())
            self.plot_values()
            return None

    def plot_values(self):
        G_pa = generate_ba(self.n, self.m, self.seed)
        plot(G_pa, self.seed, self.n, self.m)

        return None

    def on_closing(self, event=None):
        plt.close()
        self.root.quit()
        self.root.destroy()

pass

main()