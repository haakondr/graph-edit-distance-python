#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import utils.parser as p
import algorithm.graph_edit_dist as g 
import utils.misc
import time

def main(files, log_level, print_details):
    start_time = time.time()
    logger = utils.misc.setup_logging(log_level)

    g1, g2= get_graphs(files)
    
    result = g.compare(g1, g2, print_details)
    logger.info("compared graphs %s & %s"  % (files[0], files[1]))
    logger.info("Distance \t %f" % result)

    execution_time = time.time() - start_time
    logger.info("Execution time\t %s" % str(execution_time))

    
def get_graphs(files):
    g1 = p.parse_file(files[0])
    g2 = p.parse_file(files[1])
    return g1, g2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', type=str,
    default=['data/Letter/LOW/AP1_0000.gxl', 'data/Letter/LOW/AP1_0005.gxl'],
    help='Calculates the graph edit distance between the two given graphs')
    parser.add_argument('-l', '--log_level', type=int, 
    help='Sets log level; INFO=4, DEBUG=3, WARNING=2, ERROR=1, CRITICAL=0',
    default=3)
    parser.add_argument('-d', '--print_details', action='store_true',
    default=False, help='If set, more verbose details will be printed')
    args = parser.parse_args()
    main(**args.__dict__)
