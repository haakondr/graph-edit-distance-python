# -*- coding: UTF-8 -*-


def list_diff(list1, list2):
    list2 = set(list2)
    return [x for x in list1 if x not in list2]
