# Sumerian-network-graph-data

1. File flow: main.py -> node_creator.py, node_merger.py, data_handler.py, dge_creator.py
2. node_creator.py: holds the Node class and reads "full_roles_profs.csv", creating a node per row in there 
3. node_merger.py: traverse through the newly created nodes and merges nodes that have the same "(person, profession)" -> 
   puts this into a new node list ("new_nodes.csv")
4. data_handler.py: handles miscellaneous data creation
5. dge_creator.py: takes the new node list and creates edges based on the transactions and the roles involved in them
