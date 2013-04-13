# -*- coding: UTF-8 -*-


class EdgeGraph():

    def __init__(self, nodes):
        self.nodes = nodes

    def node_list(self):
        return self.nodes

    def size(self):
        return len(self.nodes)
