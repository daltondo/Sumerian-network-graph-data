import csv
from collections import defaultdict

p_index_dict = defaultdict(list)

class Node:
    def __init__(self, id, role):
        self.id = id
        self.role = role

# read though nodes.csv to store nodes in a dictionary
with open('nodes.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        # [id, name, role, profession, p_index]
        row_list = row[0].split(',')
        id = row_list[0]
        role = row_list[2]
        p_index = row_list[4]

        # store nodes together that have the same p_index
        p_index_dict[p_index].append(Node(id, role))


# traverse through the dictionary to create edge list
with open('edges.csv', 'w') as csvfile:
    fieldnames = ['source', 'target']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for p_index, nodes in p_index_dict.items():
        source = ''
        target = ''

        # iterate through p_indexes to match up nodes with each other
        for node in nodes:
            if node.role == "source":
                source = node.id
            elif node.role == "reciever":
                target = node.id
        writer.writerow({'source': source, 'target': target})

	
