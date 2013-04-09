# -*- coding: UTF-8 -*-
from utils.misc import list_diff


class Node():

    def __init__(self, id_, **attributes):
        self.id_ = id_
        self.attributes = attributes

    def __key(self):
        return self.id_

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return self.attributes['word']

    def __eq__(self, other):
        if other is None:
            return False
        return self.id_ == other.id_

    def eq_attrs(self, other):
        if other is None:
            return False
        return self.attributes == other.attributes

    def diff(self, other):
        diff = len(list_diff(self.attributes, other.attributes))

        if diff == 0:
            return 0.
        return len(self.attributes) / float(diff)


class Edge():

    def __init__(self, start, end, **attributes):
        self.start = start
        self.end = end
        self.attributes = attributes

    def __repr__(self):
        return self.attributes['deprel']

    def __hash__(self):
        return hash(self.attributes)

    def __eq__(self, other):
        return self.attributes == other.attributes
