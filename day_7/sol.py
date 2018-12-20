import sys
import networkx as nx
import heapq

G = nx.DiGraph()
for line in sys.stdin:
    source = line[5]
    dest = line[36]
    G.add_edge(source, dest)

heap = []
for node in G:
    if len(list(G.predecessors(node))) == 0:
        heapq.heappush(heap, node)

solution = []
while len(heap) > 0:
    node = heapq.heappop(heap)
    solution.append(node)
    successors = list(G.successors(node))
    G.remove_node(node)
    for successor in successors:
        if len(list(G.predecessors(successor))) == 0:
            heapq.heappush(heap, successor)
print(''.join(solution))
