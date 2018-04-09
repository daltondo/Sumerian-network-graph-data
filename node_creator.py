import csv
import node_merger
import data_handler
import edge_creator
from collections import defaultdict


# key: (person, profession), value: list of Nodes
person_to_info = defaultdict(list)


# container to store row data
class Node:
    def __init__(self, name, role, profession, family, p_index, year, processed):
        self.name = name
        self.role = role
        self.profession = profession
        # added in family variable to Node
        self.family = family
        self.p_index = p_index
        self.year = year
        self.processed = processed
        self.id = None

    def add_id(self, id):
    	self.id = id


### OPEN full_roles_profs.csv TO READ ###
# traverses through names_roles_professions to create a node per row
def create_nodes_list():
    # changed csv file from full_roles_profs to people.csv
    # added in an encoding
    with open('people.csv', 'rt', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            role = row['roles']
            profession = row['profession']
            family = row['family']
            p_index = row['p index']
            year = row['date name']
            processed = row['processed date']

            person = (name, profession)
            node = Node(name, role, profession, family, p_index, year, processed)
            person_to_info[person].append(node)
