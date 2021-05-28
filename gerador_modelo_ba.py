from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from community import community_louvain
import networkx as nx


def check_N_M(n, m):
    if( m>= 1 and m < n):
        messagebox.showerror('Erro','Modelo deve ter m>=1 e m < n = {0}, m = {1}'.format(n,m))
        return True
    return False


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

def generate_pa(m, n, seed):
    if check_N_M(n,m):
        messagebox.showinfo('Informação','Modelo de entrada padrão n = {0}, m = {1}'.format(1,50))
        return nx.generators.random_graphs.barabasi_albert_graph(50, 1, seed)
    else:
        return nx.generators.random_graphs.barabasi_albert_graph(m, n, seed)

def plot(G, seed):
    plt.clf()
    partition = community_louvain.best_partition(G, random_state=seed)
    pos = community_layout(G, partition, seed)
    nx.draw(G, pos, node_color=list(partition.values()))
    return plt.show()

def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Grafo Modelo BA(Barabási Albert)")
        self.root.geometry('700x100')
        
        self.m = 50.5
        self.n = 1.2
        self.seed = 42
        
        # Quantidade de Nós
        Label(self.root, text = "Quantidade de Nós(n)").grid(row=0, column=0)
        self.n_entry = Entry(self.root, width = 5)
        self.n_entry.grid(row=0, column = 2)
        Label(self.root, text = "O número de Nós não pode ser menor que a quantidade de arestas").grid(row=0, column=3)
        
        # Número de Arestas
        Label(self.root, text = "Número de Arestas(m)").grid(row=1, column=0)
        self.m_entry = Entry(self.root, width = 5)
        self.m_entry.grid(row=1, column=2)
        Label(self.root, text="Número de arestas que seram adicionados para os novos nós").grid(row=1, column=3)
        button2 = Button(self.root, text="Sair", command = self.on_closing).grid(row=5, column=3, pady=10)
        # Botão
        button1 = Button(self.root, text="Criar Grafo", command = self.update_values)
        button1.grid(row=5, column=2, pady=10)
        self.root.bind("<Return>", self.update_values)
        self.plot_values()
        
        pass
            
    def update_values(self, event=None):
        self.n = int(self.n_entry.get())
        self.m = int(self.m_entry.get())
        self.plot_values()
        return None

    def plot_values(self):
        G_pa = generate_pa(self.m, self.n, self.seed)
        chart = FigureCanvasTkAgg(plot(G_pa, self.seed), self.root)
        chart.get_tk_widget().grid(row = 5, column = 0)
        plt.grid()
        return None

    def on_closing(self, event=None):
        plt.close()
        self.root.quit()
        self.root.destroy()

pass

main()