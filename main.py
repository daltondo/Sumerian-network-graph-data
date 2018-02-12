import node_creator
import node_merger
import data_handler
import edge_creator


def main():
	# traversing through names_roles_professions to create a node per row
	node_creator.create_nodes_list()

	# traversing through all the newly created persons, each a person has more than 1 node, merge those nodes
	number_of_nodes_merged = node_merger.merge_nodes()
	# writing the new persons (merged nodes) into a nodes list
	node_merger.create_new_nodes_list()

	# traversing through new_person_to_info to fill out p_indexes_to_people (a dict of p_indexes to people in the p_indexes)
	data_handler.fill_new_person_to_info()

	# creates the edge list from new_person_to_info
	edge_creator.create_edge_list()


	# ##### DISPLAYING OUTPUT #####
	# # displaying the amount of nodes merged
	print("AMOUNT OF NODES MERGED: ", number_of_nodes_merged)

	# # acquiring list of texts where there were only 1 participants
	# list_of_single_participant_texts = data_handler.find_single_participant_texts()
	print("LIST OF SINGLE PARTICIPANT TEXTS: ", list_of_single_participant_texts)
	# ##### END DISPLAYING OUTPUT #####


if __name__ == "__main__":
    main()