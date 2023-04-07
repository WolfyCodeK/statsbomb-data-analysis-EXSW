import json
import os

def process_jsonl_file(filename):
    data_list = []
    with open(filename, 'r') as file:
        for line in file:
            data = json.loads(line)
            data_list.append(data)
    return data_list

directory = "largefiles"
filenames = [
    "g2312135_SecondSpectrum_tracking-produced.jsonl",
    "g2312213_SecondSpectrum_tracking-produced.jsonl",
    "g2312152_SecondSpectrum_tracking-produced.jsonl",
    "g2312166_SecondSpectrum_tracking-produced.jsonl",
    "g2312183_SecondSpectrum_tracking-produced.jsonl"
]

data_variables = []

for filename in filenames:
    filepath = os.path.join(directory, filename)
    data = process_jsonl_file(filepath)
    data_variables.append(data)

data1, data2, data3, data4, data5 = data_variables
