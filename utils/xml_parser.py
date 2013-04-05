# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import argparse
import networkx as nx
from classes.models import Node, Edge, Attribute
import os

def populate_collection(filename, col, category):
    if col == None:
        col = {}
    root = ET.parse(filename).getroot()
    
    for fingerprint in root:
        for entry in fingerprint.findall('print'):
            col[entry.attrib['file']] = entry.attrib['class'], category
    return col

def retrieve_graphs(folder):
    col = {}
    populate_collection(folder+'train.cxl', col, 'train')
    populate_collection(folder+'test.cxl', col, 'test')
    populate_collection(folder+'validation.cxl', col, 'val')
     
    data_sets = {'train':[], 'test':[], 'val':[]}
    for fname in os.listdir(folder):
        if '.gxl' in fname:
            graph_info = col[fname] 
            data_sets[graph_info[1]].append((fname, parse(folder+fname),
            graph_info[0])) 

    return data_sets

def parse(filename):
    """
    TODO: returns only one graph. Might be more than one
    gc.collect() is called due to ElementTree does not explicitly close the
    file handles, leading to too many files open
    """
    #TODO: returns only one graph. Might be more than one
    root = ET.parse(filename).getroot()
    graphs = [populate_graph(raw_graph) for raw_graph in root]
    
    return graphs[0]

def populate_graph(raw_graph):
    g = create_graph_obj(raw_graph)
    g.name = get_name(raw_graph)
    
    g.add_nodes_from(find_nodes(raw_graph))

    for edge in find_edges(raw_graph):
        g.add_edge(get_node(edge.start, g), get_node(edge.end, g),
        attr=edge.attributes)
    
    g.graph['mode'] = get_mode(g)
    
    return g

def get_mode(graph):
    try:
        node = graph.nodes()[0]
    except IndexError:
        print "graph %s does not have any nodes." % graph.graph['name']
        return "symbolic"
    for attr in node.attributes:
        if attr.vartype == "string":
            return "symbolic"
    return "numeric"

def get_node(id_, graph):
    """
    TODO: find a way to lookup the dict with id key.
    Shouldnt need to iterate through like this
    """
    for node in graph.nodes():
        if node.id_ == id_:
            return node
    raise KeyError

def get_name(raw_graph):
    return raw_graph.attrib['id']

def create_graph_obj(raw_graph):
    try:
        edgemode = raw_graph.attrib['edgemode']
    except KeyError:
        return nx.graph()
    if edgemode == 'undirected':
        return nx.Graph()
    elif edgemode == 'directed':
        return nx.DiGraph()

def find_nodes(graph):
    return [Node(node.attrib['id'], find_attributes(node)) for node 
    in graph.findall('node')]

def find_edges(graph):
    return [Edge(edge.attrib['from'], edge.attrib['to'], find_attributes(edge))
    for edge in graph.findall('edge')]

def find_attributes(node):
    return [Attribute(attr.attrib['name'], str.text, str.tag) for attr in node for str in attr]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, 
    default='data/AIDS/data/5.gxl')
    args = parser.parse_args()
    graphs = parse(**args.__dict__)
    
