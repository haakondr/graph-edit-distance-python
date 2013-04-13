#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import json


def main(tags, pos_file, deprel_file, outfile, sub_weights):
    weights = {}
    weights['pos_tags'] = generate_tags(pos_file)
    weights['deprel_tags'] = generate_tags(deprel_file)

def generate_tags(tags):
    weights = {}

    for tag1 in tags:
        weights[tag1] = insdel_weight(tag1)
        for tag2 in tags:
            weights[tag1+"-"+tag2] = sub_weight(tag1, tag2)

    f = open(outfile, 'w')
    f.write(json.dumps(weights))
    f.close()

    print "Wrote weights to %s" % outfile


def insdel_weight(tag):
    return 1.


def sub_weight(tag1, tag2):
    if tag1[1:2] == tag2[1:2]:
        return 0.25

    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('tags', nargs='*', type=str)
    parser.add_argument('-s', '--sub_weights', action="store_true",
                        default=False)
    parser.add_argument('-of', '--outfile', type=str, default="out.json")
    args = parser.parse_args()
    generate_json(**args.__dict__)
