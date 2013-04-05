# -*- coding: UTF-8 -*-
from utils.misc import list_diff

class Node():
    def __init__(self, id_, attributes):
        self.id_ = id_
        self.attributes = attributes

    def __key(self):
        return self.id_

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return self.id_
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.id_ == other.id_

    def eq_attrs(self, other):
        if other == None:
            return False
        return self.attributes == other.attributes

    def diff(self, other):
        diff = len(list_diff(self.attributes, other.attributes))

        if diff == 0:
            return 0.
        return len(self.attributes) / float(diff)
        


class Edge():
    def __init__(self, start, end, attributes):
        self.start = start
        self.end = end
        self.attributes = attributes


class Attribute():
    def __init__(self, name, var, vartype):
        self.name = name
        if vartype == 'float':
            self.var = float(var)
        elif vartype == 'int':
            self.var = int(var)
        else:
            self.var = var
        self.vartype = vartype

    def __repr__(self):
        return self.name + ":" + str(self.var) + " " + self.vartype

    def __key(self):
        return self.name, self.var, self.vartype

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if other == None:
            return False
        if (self.name == other.name and
            self.var == other.var and
            self.vartype == other.vartype):
            return True
        return False
