# -*- coding: UTF-8 -*-


class Graph():

    def __init__(self, filename, sent_number, offset, length):
        self.filename = filename
        self.sent_number = sent_number
        self.offset = offset
        self.length = length
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        if node.id_ not in self.edges:
            self.edges[node.id_] = []
        self.nodes[node.id_] = node

    def add_edge(self, edge):
        return self.edges[edge.start.id_].append(edge)

    def edges(self, node_id):
        return self.edges[node_id]

    def node_list(self):
        return [v for k, v in self.nodes.items()]

    def remove_node(self, node_id):
        del self.nodes[node_id]

    def node(self, node_id):
        return self.nodes[node_id]

    def size(self):
        return len(self.nodes)


def create_from(graph_data, sel_node_attrs):
    import node
    import edge

    graph = Graph(
        graph_data['filename'],
        int(graph_data['sentenceNumber']),
        int(graph_data['offset']),
        int(graph_data['length']))

    for token in graph_data['tokens']:
        graph.add_node(node.create_from(token, sel_node_attrs))

    for token in graph_data['tokens']:
        if token['rel'] != '0':
            graph.add_edge(edge.create_from(token, graph))

    return graph
