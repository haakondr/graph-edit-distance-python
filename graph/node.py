# -*- coding: UTF-8 -*-
from utils.misc import list_diff


class Node():

    def __init__(self, id_, attributes):
        self.id_ = id_
        self.attributes = attributes
        self.pos = attributes['pos']
        self.lemma = attributes['lemma']
        self.word = attributes['word']

    def __key(self):
        return self.id_

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return self.word

    def __eq__(self, other):
        if other is None:
            return False
        return self.lemma == other.lemma


def create_from(json_node, selected_attrs):
    attr = {k: json_node[k] for k in selected_attrs if k in json_node}
    return Node(json_node['id'], attr)
