import pandas as pd
from typing import List, Tuple


def extract_slice_from_config(start, end):
    return start-2, end-1

def analyze_filename(filename, each_range : List[Tuple]):
    for name, start, end in each_range:
        if name in str(filename): break
    return name, start, end

def extract_each_part(filename, each_range):
    name, start, end = analyze_filename(filename, each_range)
    start, end = extract_slice_from_config(start, end)
    
    df = pd.read_excel(filename)
    return name, df[start:end]
