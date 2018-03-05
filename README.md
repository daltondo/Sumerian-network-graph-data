# Sumerian-network-graph-data

1. File flow: main.py -> node_creator.py, node_merger.py, data_handler.py, edge_creator.py
2. node_creator.py: holds the Node class and reads * *full_roles_profs.csv* *, creating a node per row in there
3. node_merger.py: traverse through the newly created nodes and merges nodes that have the same "(person, profession)" ->
   puts this into a new node list (* *new_nodes.csv* *)
4. data_handler.py: handles miscellaneous data creation
5. edge_creator.py: takes the new node list and creates edges based on the transactions and the roles involved in them


# To Run
1. cd to the folder containing all your files
2. python3 main.py
3. the script will output * *new_nodes.csv* * and * *new_edges.csv* * which correspond to the node and edge list respectively


# What is Node?
It is a class that contains information about each person in the graph. It has the name,
role, profession, p_index, year the text was written in, and an arbitrary id.


# How are Nodes created?
Nodes are created by iterating row by row in * *full_roles_profs.csv* * where each information needed for a node
is obtained. Each row will create exactly one node. Nodes may not contain unique people.


# How are Nodes merged?
At this stage the previously created nodes will be merged so that each node will contain a "unique" person.
The way that we define "unique" is such that each node will have a different name and profession. <br />
**We are currently working on different attributes we can look at to merge nodes** <br />
In the previous step, we created a mapping of {(name, profession): nodes associated}. We can iterate through this mapping,
looking at each key, and if the value associated to the key is greater than one, we merge those values.
Then, the nodes will have lists for the following attributes: role, p_index, year. The ith index in role will correspond to
the ith index in p_index and year.


# How to count Nodes that are merged
The script already has a built in variable * *number_of_nodes_merged* * that will increment every time a node is merged inside
node_merger.py. Printing this variable will yield how many nodes were merged.


# How are edges weighed?
Currently, edges have no weight assigned to them. In the future, we will decided how to weigh edges.
