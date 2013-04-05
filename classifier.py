#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import time
import utils.parser as p
import multiprocessing
import algorithm.graph_edit_dist as g
import utils.misc
import algorithm.knn as classifier
import itertools


def main(folder, k, log_level, n_cases, cpu_count):
    start_time = time.time()
    logger = utils.misc.setup_logging(log_level)
    
    logger.info("classifying folder %s." % folder)
    
    results = classify(folder, k, n_cases, cpu_count)
    utils.misc.print_results(results, folder, k, logger)

    execution_time = time.time() - start_time
    logger.info("Execution time: %s" % str(execution_time))

def classify(folder, k, n_cases, cpu_count):
    """
    Splits the test set into n (amount of CPU's available) chunks, and spawns n processes which predicts the
    label for each test case.
    """
    data_sets = p.retrieve_graphs(folder)        
    
    if cpu_count == 1:
        return classify_singlecore(k, data_sets, n_cases)
    else:
        pool_size = multiprocessing.cpu_count() if cpu_count == -1 else cpu_count
        return classify_multicore(data_sets , k, n_cases, pool_size)

def classify_singlecore(k, data_sets, n_cases):
    return test((k, data_sets['train'], data_sets['test'][:n_cases]))
        

def classify_multicore(data_sets, k, n_cases, pool_size):
    print 'using %d processes' % pool_size
    chunks = utils.misc.chunks(data_sets['test'][:n_cases], pool_size)
    pool = multiprocessing.Pool(processes=pool_size)
    inputs = [(k, data_sets['train'], c) for c in chunks]
    
    r = pool.map_async(test, inputs)
    r.wait()
    results = r.get()
     
    return flatten_results(results)


def flatten_results(results):
    correct, wrongs = zip(*results)
    return sum(correct), list(itertools.chain(*wrongs))

                                                                         
def test(args):                                                          
    """
    Predicts the label for each test case. Should be spawned as a separate
    process, in order to utilize multicore processors. 
    The arguments is entered as a list because I was unable to enter them
    otherwise while using the process pool.

    Keyword arguments:

    args -- [k, training_set, test_set]
    """
#    knn = classifier.nlp_knn(args[0], args[1], 10, dist_fn=g.compare)
    knn = classifier.knn(args[0], args[1], dist_fn=g.compare)
    correct = 0
    wrongs = []

    for instance in args[2]:
        pred_label = knn.classify(instance[1])
        if pred_label == instance[2]:
            correct +=1
        else:
            wrongs.append(instance[0])
    
    return (correct, wrongs)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', nargs='?', type=str,
    default='data/Letter/LOW/',
    help='Runs the graph edit distance classification on the specified folder')
    parser.add_argument('-k', '--k', type=int, default=10, 
    help='sets the k for k-nearest-neighbours classification')
    parser.add_argument('-l', '--log_level', type=int, 
    help='Sets log level; INFO=4, DEBUG=3, WARNING=2, ERROR=1, CRITICAL=0',
    default=3)
    parser.add_argument('-n', '--n_cases', type=int, 
    help='Limits the amount of test cases to n cases', default=-1)
    parser.add_argument('-cpu', '--cpu_count', type=int, default=-1)
    args = parser.parse_args()
    main(**args.__dict__)
