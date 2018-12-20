import sys
import networkx as nx
import heapq


G = nx.DiGraph()
for line in sys.stdin:
    source = line[5]
    dest = line[36]
    G.add_edge(source, dest)

nodes = len(G)

incoming = {node: len(list(G.predecessors(node))) for node in G}
candidates = [node for node in G if incoming[node] == 0]
heapq.heapify(candidates)

state = {node: 0 for node in G}
events = []
solution = []
time = 0
available_workers = 5
while len(solution) <= nodes:
    while available_workers > 0 and len(candidates) > 0:
        node = heapq.heappop(candidates)
        heapq.heappush(events, (time + 60 + ord(node) - ord('A') + 1, node))
    if len(events) == 0:
        break
    time, node = heapq.heappop(events)
    available_workers += 1
    solution.append(node)
    successors = list(G.successors(node))
    G.remove_node(node)
    for successor in successors:
        if len(list(G.predecessors(successor))) == 0:
            heapq.heappush(candidates, successor)
print(time)
print(''.join(solution))
