from config.config import CONFIG
from pathlib import Path
import pandas as pd


EACH_RANGE = CONFIG['part']
NAME_CONCATED = CONFIG['output_name']

ROOT_EXCEL = CONFIG['src']
ROOT_EXCEL = Path(ROOT_EXCEL)

FILENAME_CONCATED = ROOT_EXCEL / f'{NAME_CONCATED}.xlsx'


def extract_slice_from_config(start, end):
    return start-2, end-1

def analyze_filename(filename):
    for name, [start, end] in EACH_RANGE.items():
        if name in str(filename): break
    return name, start, end

def extract_each_part(filename):
    name, start, end = analyze_filename(filename)
    start, end = extract_slice_from_config(start, end)
    
    df = pd.read_excel(filename)
    return name, df[start:end]


table_df = ROOT_EXCEL.iterdir()
table_df = map(extract_each_part, table_df)
table_df = {k:v for k,v in table_df}


def sort_by(item):
    k, [start, end] = item
    return start
def extract_key(item):
    k, [start, end] = item
    return k


merge_order = sorted(EACH_RANGE.items(), key=sort_by)
merge_order = map(extract_key, merge_order)

arr_df = (table_df[key] for key in merge_order)
df_concat = pd.concat(arr_df)

df_concat.to_excel(FILENAME_CONCATED, index=False)
