import json

INPUT_FILE = "input1.csv"

def csv_to_list_dict(input_file, delim = ",") -> list[dict]:
    with open(input_file) as f:
        list_ = [line.rstrip().split(delim) for line in f]
        
    result = [dict(zip(list_[0], i)) for i in list_[1:]]

    return result

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
