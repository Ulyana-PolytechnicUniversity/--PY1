import json

INPUT_FILE = "input1.csv"

def csv_to_list_dict(input_file, delim = ",") -> list[dict]:
    list_ = []
    with open(input_file) as f:
        for line in f:
            list_.append(line.rstrip().split(delim))
    headers_list = list_[0]
    value_list = list_[1:]
    res = []
    for i in value_list:
        res.append(dict(zip(headers_list, i)))
    return res

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
