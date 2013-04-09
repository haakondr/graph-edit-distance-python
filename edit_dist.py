#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import algorithm.graph_edit_dist as g
import utils.json_utils as j


def main(files, pos, deprel, print_details):
    print deprel
    print pos

    result = g.compare(get_graphs(files), print_details)
    print "Normalized graph edit distance = %s" % result


def get_graphs(files):
    g1 = j.parse_json(files[0])
    g2 = j.parse_json(files[1])
    return g1, g2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', type=str,
                        help='Calculates the graph edit distance between \
                        the two given graphs')
    parser.add_argument('--deprel', type=str,
                        default="resources/deprel_weights.json",
                        help="Points to peprel substitution/insert/delete \
                        weights file in json format")
    parser.add_argument('--pos', type=str,
                        default="resources/pos_weights.json",
                        help="Points to pos-tag substitution/insert/delete \
                        weights file in json format")
    parser.add_argument('-d', '--print_details', action='store_true',
                        default=False, help='If set, more verbose details \
                         will be printed')
    args = parser.parse_args()
    main(**args.__dict__)
