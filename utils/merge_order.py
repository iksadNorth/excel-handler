from typing import List, Tuple


def sort_by(item):
    name, start, end = item
    return start

def extract_key(item):
    name, start, end = item
    return name

def get_merge_order(each_range : List[Tuple]):
    merge_order = sorted(each_range, key=sort_by)
    merge_order = map(extract_key, merge_order)
    return merge_order
