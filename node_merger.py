import csv
import node_creator
import data_handler
import edge_creator
from collections import defaultdict


# key: p_index, value: list of (name of person, role in this p_index)
p_indexes_to_people = defaultdict(list)
# key: (person, profession), value: Node
new_person_to_info = {}


# traverses through all the newly created persons, in each person has more than 1 node, merge those nodes
def merge_nodes():
	number_of_nodes_merged = 0
	for key, value in sorted(node_creator.person_to_info.items(), key = lambda x:x[0][0]):
		if len(value) > 1:
			merge_nodes_helper(key, value)
			number_of_nodes_merged += 1
	return number_of_nodes_merged


# the ith role, profession, p_id all correspond with each other
def merge_nodes_helper(person, list_of_nodes):
	roles = []
	p_indexes = []
	years = []
	family = []
	processed=[]

	for node in list_of_nodes:
		roles.append(node.role)
		p_indexes.append(node.p_index)
		years.append(node.year)
		family.append(node.family)
		if node.processed != '':
			processed.append(node.processed)
	node = node_creator.Node(person[0], roles, person[1], family, p_indexes, years, processed)
	new_person_to_info[person] = node


### OPEN new_nodes.csv TO WRITE ###
# writes the new persons (merged nodes) into a nodes list
def create_new_nodes_list():
	with open('new_nodes.csv', 'w') as csvfile:
		fieldnames = ['id', 'name', 'role', 'profession', 'processed year', 'family', 'p_index', 'date name', 'maxYear', 'minYear']

		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()

		curr_id = 1

		for person, node in new_person_to_info.items():
			name = person[0]

			if type(node) is list:
				node = node[0]

			role = node.role
			profession = node.profession
			family = node.family
			p_index = node.p_index
			year = node.year
			processed = node.processed
			if len(processed)>0:
				maxYear = max(processed)
				minYear = min(processed)
			else:
				maxYear = 0
				minYear = 0
			node.add_id(curr_id)

			writer.writerow({
				'id': curr_id,
				'name': name,
				'role': role,
				'profession': profession,
				'family': family,
				'p_index': p_index,
				'maxYear': maxYear,
				'minYear': minYear,
				'date name': year,
				'processed year': processed
				})
			curr_id += 1

		csvfile.close()
