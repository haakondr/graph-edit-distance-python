def chunks(l, n):
    """
    Yield n successive chunks from l.
    """
    newn = int(len(l) / n)
    for i in xrange(0, n-1):
        yield l[i*newn:i*newn+newn]
    yield l[n*newn-newn:]


def list_diff(list1, list2):
    list2 = set(list2)
    return [x for x in list1 if x not in list2]
