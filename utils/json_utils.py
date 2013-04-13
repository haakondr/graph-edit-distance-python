# -*- coding: UTF-8 -*-
import json


def parse_json(filename):
    with open(filename) as json_data:
        return json.load(json_data)


def edit_weights(filename):
    json = parse_json(filename)
    return json['pos_weights'], json['deprel_weights']
