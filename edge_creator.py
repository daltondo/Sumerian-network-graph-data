import csv
import node_creator
import node_merger
import data_handler
from collections import defaultdict


# want edge file to hae a few more rows, lets have like source -> recipeint or source -> intermediarary
### Source -> recipient, source -> intermediary -> recipient, source -> representative -> recipient
### OPEN new_edges.csv TO WRITE ###
def create_edge_list():
	with open('new_edges.csv', 'w') as csvfile:
		fieldnames = ['id', 'source', 'target', 'p_index', 'year', 'type', 'source\'s role', 'target\'s role']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()

		curr_id = 1
		count = 0 # can move this around in the control flow to count how many transactions are of a certain type
		for key, value in node_merger.p_indexes_to_people.items():
			# removing multiple transactions: this thins it down from 11384 edges to 9069 edges
			if len(value) > 1 and len(value) < 5:
				### FOR NOW JUST CREATE EDGES WITH WHAT YOU KNOW
				### 1. source -> recipient (Done)
				### 2. source -> interm -> recipient (Done)
				### 3. source -> recipient, source -> interm, interm -> recipient (Done)

				# only looking at transactions where there are only 2 people involved
				# there are 5912 transactions where there are only 2 people involved
				if len(value) == 2:
					list_of_roles = []
					role_to_node = {}
					node1 = None
					node2 = None

					for node in value:
						list_of_roles.append(node[1])
						role_to_node[node[1]] = node

					# there are 5176 transactions between "source" -> some other person("recipient", "intermediary", "representative", etc.)
					# thus this creates 5176 edges
					if "['source']" in list_of_roles:
						role1 = "['source']"
						person1 = role_to_node[role1][0]
						node1 = node_merger.new_person_to_info[person1]
						id1 = node1.id

						list_of_roles.remove("['source']")

						role2 = list_of_roles[0]
						person2 = role_to_node[list_of_roles[0]][0]
						node2 = node_merger.new_person_to_info[person2]
						id2 = node2.id

						edge_type = "Directed"

					# there are 456 transactions between other person -> "recipient"
					# thus this creates 456 edges
					# sometimes there are "recipients" -> "recipients" in a transactions, so the edge is chose arbitrarily
					elif "['recipient']" in list_of_roles:
						role2 = "['recipient']"
						person2 = role_to_node[role2][0]
						node2 = node_merger.new_person_to_info[person2]
						id2 = node2.id

						list_of_roles.remove("['recipient']")

						role1 = list_of_roles[0]
						person1 = role_to_node[list_of_roles[0]][0]
						node1 = node_merger.new_person_to_info[person1]
						id1 = node1.id

						edge_type = "Directed"

					# there are 280 transactions where there are neither a source nor a recipient
					# thus this creates 280 edges
					else:
						role1 = list_of_roles[0]
						person1 = role_to_node[role1][0]
						node1 = node_merger.new_person_to_info[person1]
						id1 = node1.id

						role2 = list_of_roles[1]
						person2 = role_to_node[role2][0]
						node2 = node_merger.new_person_to_info[person2]
						id2 = node2.id

						edge_type = "Undirected"

					edge_id = curr_id
					curr_id += 1
					p_index = key
					index_of_year = node1.p_index.index(p_index)
					year = node1.year[index_of_year]

					writer.writerow({
						'id': edge_id,
						'source': id1,
						'target': id2,
						'p_index': p_index,
						'year': year,
						'type': edge_type,
						'source\'s role': role1,
						'target\'s role': role2
						})

				### Some common structures:
				### - source, recipient1, recipient2: source -> recipient1, source -> recipient2
				### - source, something, recipient: source -> something, something -> recipient, source -> recipient
				### - if neither of these structures, just make triangular undirected edges
				if len(value) == 3:
					list_of_roles = []
					role_to_node_list = defaultdict(list)
					node1 = None
					node2 = None
					node3 = None

					for node in value:
						list_of_roles.append(node[1])
						role_to_node_list[node[1]].append(node)


					if "['source']" in list_of_roles and "['recipient']" in list_of_roles:
						# source, recipient1, recipient2: source -> recipient1, source -> recipient2 (creates 2 edges)
						# there are 196 transactions of this structure
						# thus this creates 392 edges
						if list_of_roles.count("['recipient']") == 2:
							role1 = "['source']"
							person1 = role_to_node_list[role1][0][0]
							node1 = node_merger.new_person_to_info[person1]
							id1 = node1.id

							role2 = "['recipient']"
							person2 = role_to_node_list[role2][0][0]
							node2 = node_merger.new_person_to_info[person2]
							id2 = node2.id

							role3 = "['recipient']"
							person3 = role_to_node_list[role2][1][0]
							node3 = node_merger.new_person_to_info[person3]
							id3 = node3.id

							edge_type = "Directed"
							edge_id = curr_id
							curr_id += 1
							p_index = key
							index_of_year = node1.p_index.index(p_index)
							year = node1.year[index_of_year]

							writer.writerow({
								'id': edge_id,
								'source': id1,
								'target': id2,
								'p_index': p_index,
								'year': year,
								'type': edge_type,
								'source\'s role': role1,
								'target\'s role': role2
								})
							edge_id = curr_id
							curr_id += 1
							writer.writerow({
								'id': edge_id,
								'source': id1,
								'target': id3,
								'p_index': p_index,
								'year': year,
								'type': edge_type,
								'source\'s role': role1,
								'target\'s role': role3
								})

						# source, something, recipient: source -> something, something -> recipient, source -> recipient (creates 3 edges)
						# there are 208 transactions of this structure
						# thus this creates 624 edges
						else:
							role1 = "['source']"
							person1 = role_to_node_list[role1][0][0]
							node1 = node_merger.new_person_to_info[person1]
							id1 = node1.id

							list_of_roles.remove("['source']")
							list_of_roles.remove("['recipient']")

							role2 = list_of_roles[0]
							person2 = role_to_node_list[role2][0][0]
							node2 = node_merger.new_person_to_info[person2]
							id2 = node2.id

							role3 = "['recipient']"
							person3 = role_to_node_list[role3][0][0]
							node3 = node_merger.new_person_to_info[person3]
							id3 = node3.id

							edge_type = "Directed"
							edge_id = curr_id
							curr_id += 1
							p_index = key
							index_of_year = node1.p_index.index(p_index)
							year = node1.year[index_of_year]

							writer.writerow({
								'id': edge_id,
								'source': id1,
								'target': id2,
								'p_index': p_index,
								'year': year,
								'type': edge_type,
								'source\'s role': role1,
								'target\'s role': role2
								})
							edge_id = curr_id
							curr_id += 1
							writer.writerow({
								'id': edge_id,
								'source': id1,
								'target': id3,
								'p_index': p_index,
								'year': year,
								'type': edge_type,
								'source\'s role': role1,
								'target\'s role': role3
								})
							edge_id = curr_id
							curr_id += 1
							writer.writerow({
								'id': edge_id,
								'source': id2,
								'target': id3,
								'p_index': p_index,
								'year': year,
								'type': edge_type,
								'source\'s role': role2,
								'target\'s role': role3
								})

					# if neither of these structures, just make triangular undirected edges (creates 3 edges)
					# there are 685 transactions of this structure
					# thus this creates 2055 edges
					else:
						count += 1
						list_of_roles = []
						node_list = []
						for node in value:
							list_of_roles.append(node[1])
							node_list.append(node)

						role1 = list_of_roles[0]
						person1 = node_list[0][0]
						node1 = node_merger.new_person_to_info[person1]
						id1 = node1.id

						role2 = list_of_roles[1]
						person2 = node_list[1][0]
						node2 = node_merger.new_person_to_info[person2]
						id2 = node2.id

						role3 = list_of_roles[2]
						person3 = node_list[2][0]
						node3 = node_merger.new_person_to_info[person3]
						id3 = node3.id

						edge_type = "Undirected"
						edge_id = curr_id
						curr_id += 1
						p_index = key
						index_of_year = node1.p_index.index(p_index)
						year = node1.year[index_of_year]

						writer.writerow({
							'id': edge_id,
							'source': id1,
							'target': id2,
							'p_index': p_index,
							'year': year,
							'type': edge_type,
							'source\'s role': role1,
							'target\'s role': role2
							})
						edge_id = curr_id
						curr_id += 1
						writer.writerow({
							'id': edge_id,
							'source': id1,
							'target': id3,
							'p_index': p_index,
							'year': year,
							'type': edge_type,
							'source\'s role': role1,
							'target\'s role': role3
							})
						edge_id = curr_id
						curr_id += 1
						writer.writerow({
							'id': edge_id,
							'source': id2,
							'target': id3,
							'p_index': p_index,
							'year': year,
							'type': edge_type,
							'source\'s role': role2,
							'target\'s role': role3
							})

			# if len(value) == 4:
			# 	print("HERE")
			# 	with open('4_people_transactions.csv', 'w') as csvfile:
			# 		filednames = ['p_index', 'people involved', 'roles involved']
			# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			# 		writer.writeheader()
			#
			# 		count += 1
			# 		list_of_roles = []
			# 		role_to_node = {}
			# 		for node in value:
			# 				list_of_roles.append(node[1])
			# 				role_to_node[node[1]] = node
			# 		# print(key, list_of_roles)
			# 		csvfile.close()

		csvfile.close()
