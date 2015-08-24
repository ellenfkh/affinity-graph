# operations for updating and loading data
import json


def load_from_file(filename):
    print "loading " + filename
    with open(filename, 'r') as f:
        json_data = json.loads(f.read())
        print json_data

    return json_data


def write_to_file(filename, graph):
    # graph is dict
    # may overwrite (ask for confirmation?)
    pass
