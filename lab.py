from igraph import Graph, plot
import re

class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self._find(p) == self._find(q)

    # quick union two component
    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

def kruskal(graph):
    # initialize MST
    adj = graph.get_adjacency()
    MST = set()
    edges = set()
    # collect all edges from graph G
    for j in range(graph.vcount()):
        for k in range(graph.vcount()):
            if adj[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort all edges in graph G by weights from smallest to largest
    sorted_edges = sorted(edges, key=lambda e:adj[e[0]][e[1]])
    uf = UF(graph.vcount())
    for e in sorted_edges:
        u, v = e
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        MST.add(e)
    return MST



def main():

    # Create a random Graph
    g = Graph.Erdos_Renyi(n=10, m=20, directed=True)

    # Return a minimum spanning tree for a graph
    agm = g.spanning_tree(weights=None, return_tree=True)
    kr = kruskal(g)
    agmk = Graph(n=10, edges=list(kr))
    # plot Graph
    plot(g)
    plot(agm)
    plot(agmk)



if __name__ == '__main__':
    main()
