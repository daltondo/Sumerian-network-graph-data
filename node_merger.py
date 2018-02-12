import csv
import node_creator
import data_handler
import edge_creator
from collections import defaultdict


# key: p_index, value: list of (name of person, role in this p_index)
p_indexes_to_people = defaultdict(list)
# key: (person, profession), value: Node
new_person_to_info = {}


# traverses through all the newly created persons, each a person has more than 1 node, merge those nodes
def merge_nodes():
	number_of_nodes_merged = 0
	for key, value in node_creator.person_to_info.items():
		if len(value) > 1:
			merge_nodes_helper(key, value)
			number_of_nodes_merged += 1
	return number_of_nodes_merged


# the ith role, profession, p_id all coreespond with each other
def merge_nodes_helper(person, list_of_nodes):
	roles = []
	p_indexes = []
	years = []

	for node in list_of_nodes:
		roles.append(node.role)
		p_indexes.append(node.p_index)
		years.append(node.year)

	node = node_creator.Node(person[0], roles, person[1], p_indexes, years)
	new_person_to_info[person] = node


### OPEN new_nodes.csv TO WRITE ###
# writes the new persons (merged nodes) into a nodes list
def create_new_nodes_list():
	with open('new_nodes.csv', 'w') as csvfile:
		fieldnames = ['id', 'name', 'role', 'profession', 'p_index', 'year']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()

		curr_id = 1

		for person, node in new_person_to_info.items():
			name = person[0]

			if type(node) is list:
				node = node[0]

			role = node.role
			profession = node.profession
			p_index = node.p_index
			year = node.year
			node.add_id(curr_id)

			writer.writerow({
				'id': curr_id, 
				'name': name, 
				'role': role, 
				'profession': profession, 
				'p_index': p_index,
				'year': year
				})
			curr_id += 1


