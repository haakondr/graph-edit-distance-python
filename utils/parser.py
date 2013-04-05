# -*- coding: UTF-8 -*-
import utils.xml_parser as xmlp
import utils.conll_parser as conllp

def parse_file(filename):
    if filename.endswith(".xml") or filename.endswith(".gxl"):
        return xmlp.parse(filename)
    elif filename.endswith(".txt") or filename.endswith(".conll"):
        return conllp.parse(filename)
    else:
        print "invalid file: "+filename
        raise Exception

def retrieve_graphs(path):
    import os.path
    if os.path.isfile(path+"train.cxl"):
        return xmlp.retrieve_graphs(path)
    else:
        return conllp.retrieve_graphs(path)
