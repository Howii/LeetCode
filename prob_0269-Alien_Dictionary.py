def buildGraph(words: list) -> tuple:
    # build graph as dictionary of sets
    graph = {}
    reverse_graph = {}
    # register all nodes
    for word in words:
        for c in word:
            if c not in graph:
                graph[c] = set()
                reverse_graph[c] = set()
    # establish edges by lexicographical order
    for i in range(len(words) - 1):
        low_word = words[i]
        high_word = words[i+1]
        if len(low_word) > len(high_word):
            if low_word[:len(high_word)] == high_word:
                return {}, {} # invalid ordering
        for x, y in zip(low_word, high_word):
            if x != y:
                graph[x].add(y)
                reverse_graph[y].add(x)
                break
    return graph, reverse_graph

def alienOrder(words: list) -> str:
    out_list = []
    graph, reverse_graph = buildGraph(words)
    # Kahn's algorithm for topological sort
    # may be optimized here
    while graph:
        terminal_nodes = []
        for x, children in graph.items():
            if len(children) == 0:
                terminal_nodes.append(x)
        if len(terminal_nodes) == 0:
            return ""
        out_list += terminal_nodes
        # remove terminal nodes from both graphs
        for n in terminal_nodes:
            del graph[n]
            tmp_nodes = reverse_graph.pop(n)
            for m in tmp_nodes:
                graph[m].remove(n)

    out_list.reverse()
    return "".join(out_list)

## Test
words = ["wrt", "wrf", "er", "ett", "rftt"]
order = alienOrder(words)
print(order)
