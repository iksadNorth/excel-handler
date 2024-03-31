from config.config import CONFIG
from pathlib import Path
import pandas as pd
from pandas import DataFrame

from utils.trimmer import extract_each_part
from utils.merge_order import get_merge_order
from utils.properties import transfer_as_properties

from typing import List, Dict


# 환경 변수 정의
EACH_RANGE = CONFIG['part']
EACH_RANGE = transfer_as_properties(EACH_RANGE)
NAME_CONCATED = CONFIG['output_name']

ROOT_EXCEL = CONFIG['src']
ROOT_EXCEL = Path(ROOT_EXCEL)

FILENAME_CONCATED = ROOT_EXCEL / f'{NAME_CONCATED}.xlsx'


# Key:Value = [작업자명]:[작업된 EXCEL DataFrame]
# {김철수 : DataFrame1, 이영희 : DataFrame2, 박갑수 : DataFrame3}
def extract(filename):
    return extract_each_part(filename, EACH_RANGE)

table_df = ROOT_EXCEL.iterdir()
table_df = map(extract, table_df)
table_df : Dict[str, DataFrame] = {name:df for name,df in table_df}

# 병합할 작업자 순서
# 김철수, 이영희, 박갑수
merge_order : List[str] = get_merge_order(EACH_RANGE)

# 순서대로 병합
arr_df = (table_df[key] for key in merge_order)
df_concat = pd.concat(arr_df)

# 통합된 엑셀 생성.
df_concat.to_excel(FILENAME_CONCATED, index=False)
