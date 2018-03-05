import csv
import node_merger
import data_handler
import edge_creator
from collections import defaultdict


# key: (person, profession), value: list of Nodes
person_to_info = defaultdict(list)


# container to store row data
class Node:
    def __init__(self, name, role, profession, p_index, year):
        self.name = name
        self.role = role
        self.profession = profession
        self.p_index = p_index
        self.year = year
        self.id = None

    def add_id(self, id):
    	self.id = id


### OPEN full_roles_profs.csv TO READ ###
# traverses through names_roles_professions to create a node per row
def create_nodes_list():
	with open('full_roles_profs.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			name = row['name']
			role = row['role']
			profession = row['profession']
			p_index = row['p id']
			year = row['year']

			person = (name, profession)
			node = Node(name, role, profession, p_index, year)
			person_to_info[person].append(node)
