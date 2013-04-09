# -*- coding: UTF-8 -*-


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
