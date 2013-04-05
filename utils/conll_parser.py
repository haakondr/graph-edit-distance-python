# -*- coding: UTF-8 -*-

import csv
import networkx as nx
from classes.linguistic_models import Node 
import os


def retrieve_graphs(rootdir):
    #TODO: randomize test/val ?
    col = {}
    col['train'] = parse_files(rootdir+"/source-documents/")
    suspicious_documents = parse_files(rootdir+"/suspicious-documents/")
    col['test'] = suspicious_documents[:len(suspicious_documents)/2]
    col['val'] = suspicious_documents[len(suspicious_documents)/2:]

    return col

def parse_files(path):
    files = os.listdir(path) 
    
    return [parse(path, f) for f in files]

def parse(filepath):
    """
    TODO: rewrite maltparser to not reset token id for each sentence? That way
    node id's are simpler

    """
    f = open(filepath, 'r')
    reader = csv.reader(f,dialect='excel-tab',quoting=csv.QUOTE_NONE)
    tokens = [token for token in reader]
    orig_text = " ".join(w[1] for w in tokens)
    graph = nx.DiGraph(name=filepath.split("/")[-1], original = orig_text) 
    nodes = dict()
    sentence = 1 

    for token in tokens:
        if token[0] == "1":
            sentence += 1
        node_id = get_id(token[0], sentence)
        node = Node(node_id, token[1], [token[4]])
        nodes[node_id] = node
        graph.add_node(node)

    sentence = 1 
    for token in tokens:
        if token[0] == "1":
            sentence += 1
        if (token[6] != "0" and token[0] != "0"):
            graph.add_edge(nodes[get_id(token[0], sentence)],
                    nodes[get_id(token[6], sentence)], attr=[token[7]])
    
    f.close()
    
    return graph

def get_id(token_id, sentence):
    return str(sentence)+"_"+token_id

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', type=str)
    args = parser.parse_args()
    parse(**args.__dict__)
