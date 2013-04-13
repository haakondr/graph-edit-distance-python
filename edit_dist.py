#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import algorithm.graph_edit_dist as ged
import utils.json_utils as j
import graph.graph as g


def main(files, edit_weights, print_details):
    pos, deprel = j.edit_weights(edit_weights)
    g1 = create_graph(files[0])
    g2 = create_graph(files[1])

    result = ged.compare(g1, g2, pos, deprel, print_details)
    print "Normalized graph edit distance = %s" % result


def create_graph(filename):
    json = j.parse_json(filename)
    return g.create_from(json, ['word', 'lemma', 'pos'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', type=str,
                        help='Calculates the graph edit distance between \
                        the two given graphs')
    parser.add_argument('-ew', '--edit_weights', type=str,
                        default="resources/edit_weights.json",
                        help="Points to edit weight costs \
                        json filet")
    parser.add_argument('-d', '--print_details', action='store_true',
                        default=False, help='If set, more verbose details \
                         will be printed')
    args = parser.parse_args()
    main(**args.__dict__)
