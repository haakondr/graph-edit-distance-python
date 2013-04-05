import pylab
import matplotlib.pyplot as plt
import networkx as nx


def make_graph_fig(graph, filename):
    edges = graph.edges()
    for edge in edges:
        x = [node.attributes[0].var for node in edge]
        y = [node.attributes[1].var for node in edge]
        plt.plot(x,y)
    plt.title(filename)
    plt.savefig(filename)
    plt.close()

