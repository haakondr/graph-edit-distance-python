# -*- coding: UTF-8 -*-

class Node():
    def __init__(self, id_, word, pos):
        self.id_ = id_
        self.word = word
        self.pos = pos

    def __key(self):
        return self.id_

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return self.id_+":"+self.word

    def diff(self, other):
        diff = 0
        if self.word != other.word:
            diff += 0.5 
        if self.pos != other.pos:
            diff += 0.5
        return diff
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.pos == other.pos
