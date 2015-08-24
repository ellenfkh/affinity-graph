# operations for updating and loading data
import json
import os.path


def load_from_file(filename):
    with open("data/" + filename, 'r') as infile:
        json_data = json.loads(infile.read())

    return json_data


# TODO hasn't been used/tested yet
def write_to_file(filename, graph, overwrite=True):
    if os.path.isfile(filename) and not overwrite:
        return graph

    else:
        with open(filename, 'w') as outfile:
            json.dumps(graph, outfile)

    return graph
