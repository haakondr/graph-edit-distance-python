def chunks(l, n):
    """ Yield n successive chunks from l.
    """
    newn = int(len(l) / n)
    for i in xrange(0, n-1):
        yield l[i*newn:i*newn+newn]
    yield l[n*newn-newn:]

def setup_logging(log_level):
    import logging
    import sys
    logger = logging.getLogger('plagiarism')
    hdlr = logging.FileHandler('output/plagiarism.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    
    levels = {0:logging.CRITICAL, 1:logging.ERROR, 2:logging.WARNING, 
    3:logging.DEBUG, 4:logging.INFO}
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(levels[log_level])
    logger.addHandler(console)

    return logger

def print_results(results, folder, k, logger):
    logger.info("Classification done") 
    correct = results[0] 
    wrongs = results[1] 
    logger.info("correct: \t%i " % correct)
    n_wrongs = len(wrongs)
    logger.info("wrongs: \t%i " % n_wrongs)
    logger.info("accuracy: \t%f " % (correct/ float(n_wrongs+correct)))
    logger.info("wrongly classified instances: "+ ", ".join(wrongs))

def list_diff(list1, list2):
    list2 = set(list2)
    return [x for x in list1 if x not in list2]
