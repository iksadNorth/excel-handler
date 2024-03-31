# 무조건 name, start, end 형태로 내뱉어야 함.
def define_properties(item):
    name, [start, end] = item
    return name, start, end

def transfer_as_properties(table : dict):
    return [define_properties(item) for item in table.items()]
