import json
from ast import literal_eval

def process_json(json_data):
    taken_list = []
    #parsed_json = (json.loads(json_data))
    for i in json_data:
        if type(literal_eval(json_data[i])) == list: 
            taken_list += literal_eval(json_data[i])
        else: 
            taken_list.append(int(json_data[i]))
    taken_list.sort()
    return taken_list

