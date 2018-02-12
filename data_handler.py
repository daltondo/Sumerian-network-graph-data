import csv
import node_creator
import node_merger
import edge_creator
from collections import defaultdict


# traverses through new_person_to_info to fill out p_indexes_to_people (a dict of p_indexes to people in the p_indexes)
def fill_new_person_to_info():
	for person, node in node_merger.new_person_to_info.items():
		roles = node.role
		p_indexes = node.p_index
		years = node.year

		for i in range(len(roles)):
			curr_p_index = p_indexes[i]
			curr_role = roles[i]
			container = (person, curr_role, i)
			node_merger.p_indexes_to_people[curr_p_index].append(container)


# acquires list of texts where there were only 1 participants
def find_single_participant_texts():
	list_of_single_participant_texts = []
	for key, value in node_merger.p_indexes_to_people.items():
		if len(value) == 1:
			list_of_single_participant_texts.append(key)
	return list_of_single_participant_texts


# finds p_indexes where there are more than 5 people involved in the transaction
def find_multiple_transactions():
	with open('multiple_transactions.csv', 'w') as csvfile:
		fieldnames = ['p_index', 'people_involved']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for key, value in node_merger.p_indexes_to_people.items():
			if len(value) >= 5:
				p_index = key
				people_involved = value
				
				writer.writerow({
				'p_index': p_index, 
				'people_involved': people_involved
				})