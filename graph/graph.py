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
        self.nodes[node.id_] = node

    def add_edge(self, edge):
        return self.edges[edge.start.node_id].append(edge)

    def edges(self, node_id):
        return self.edges[node_id]

    def nodes(self):
        return self.nodes.items()

    def remove_node(self, node_id):
        del self.nodes[node_id]

    def node(self, node_id):
        return self.nodes[node_id]


def create_from(json_graph, sel_node_attrs):
    import json
    import node
    import edge

    data = json.loads(json_graph)

    graph = Graph(
        data['filename'],
        int(data['sentenceNumber']),
        int(data['offsett']),
        int(data['length']))

    for token in data['tokens']:
        graph.add_node(node.create_from(token, sel_node_attrs))
        graph.add_edge(edge.create_from(token))

    return graph
