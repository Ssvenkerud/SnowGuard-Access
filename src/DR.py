import logging


class DataReciver:

def __init__(self, spec=None, data=None, schema=None):

self.logger = logging.getLogger("DataReciver")

self.logger.info("DataReciver object created")

self.raw_data = data

self.schema = schema

self.spec = spec

self.node_map = {}

self.edge_map = {}

self.logger.debug(f"Spec: {self.spec}")

self.logger.debug(f"Schema: {self.schema}")

  

def extract_nodes(self):

self.logger.info("Extracting nodes from spec")

for column in self.spec["nodes"]:

self.logger.debug(f"Column: {column}")

self.node_map[column] = []

  

self.logger.info("Extracting nodes from raw data")

for row in self.raw_data:

self.logger.debug(f"Row: {row}")

for column in self.spec["nodes"]:

self.logger.debug(f"Column: {column}")

node = row[self.schema.index(column)]

self.logger.debug(f"Node: {node}")

self.node_map[column].append(node) if node not in self.node_map[

column

] else None

self.logger.debug(

f"Nuber of nodes in {column}: {len(self.node_map[column])}"

)

self.logger.info("Nodes extracted")

  

def extract_edges(self):

self.logger.info("Extracting edges from spec")

for edge_spec in self.spec["edges"]:

self.logger.debug(f"Edge spec: {edge_spec}")

edge_name = "-".join(edge_spec)

self.edge_map[edge_name] = []

self.logger.debug(f"Edge name: {edge_name}")

  

self.logger.info("Extracting edges from raw data")

for row in self.raw_data:

self.logger.debug(f"Row: {row}")

for edge_spec in self.spec["edges"]:

self.logger.debug(f"Edge spec: {edge_spec}")

  

edge_name = "-".join(edge_spec)

self.logger.debug(f"Edge name: {edge_name}")

edge = tuple(

[row[self.schema.index(column.upper())] for column in edge_spec]

)

self.logger.debug(f"Edge: {edge}")

self.edge_map[edge_name].append(edge)

self.logger.debug(

f"Nuber of edges in {edge_name}: {len(self.edge_map[edge_name])}"

)

self.logger.info("Edges extracted")

  

def get_edges(self):

self.logger.info("Serving edges from edge map to networkx graph")

edges = []

for edge_name in self.edge_map:

edges += self.edge_map[edge_name]

self.logger.debug(f"nuber of edges served: {len(edges)}")

self.logger.info("Edges served")

return edges

  

def get_nodes(self):

self.logger.info("Serving nodes from node map to networkx graph")

nodes = []

for node_name in self.node_map:

nodes += self.node_map[node_name]

self.logger.debug(f"nuber of nodes served: {len(nodes)}")

self.logger.info("Nodes served")

return nodes

  

def attach_node_atributes(self):

self.logger.info("Attaching node attributes to networkx graph")

for node_type in self.node_map:

self.logger.debug(f"Node type: {node_type}")

for node in self.node_map[node_type]:

self.logger.debug(f"Node: {node}")

node_attribute = self.get_node_attributes(node)

self.logger.debug(f"Node with attributes: {(node,node_attribute)}")

node_possition = self.node_map[node_type].index(node)

self.node_map[node_type][node_possition] = (node, node_attribute)

  

def get_node_attributes(self, node):

node_attribute = {}

for node_name in self.node_map:

if node in self.node_map[node_name]:

node_attribute = self.spec["nodes"][node_name]

self.logger.debug(f"Attributes for node {node} : {node_attribute}")

return node_attribute

  

def _alter_name_by_attribute(self, node_type, on_attribute):

self.logger.debug(f"Node type: {node_type}")

for node in self.node_map[node_type]:

self.logger.debug(f"Node: {node}")

name_alter = node[1][on_attribute]

self.logger.debug(f"Name alter: {name_alter}")

node_possition = self.node_map[node_type].index(node)

self.node_map[node_type][node_possition] = (

f"{node[0]}-{name_alter}",

node[1],

)

self.logger.debug(

f"Node with altered name: {self.node_map[node_type][node_possition]}"

)

  

def alter_node_name(self, node_type=None, on_attribute=None):

self.logger.info("Altering node names")

if node_type is None:

node_type = self.node_map.keys()

for node_type_item in node_type:

self._alter_name_by_attribute(node_type_item, on_attribute)

self.logger.info("Node names altered")

  

for edge_name in self.edge_map:

self.logger.debug(f"Edge name: {edge_name}")

start, end = edge_name.split("-")

self.logger.debug(f"Start: {start}, End: {end}")

self.logger.debug(f"Node type: {node_type}")

  

for edge in self.edge_map[edge_name]:

self.logger.debug(f"Edge: {edge}")

edge_possition = self.edge_map[edge_name].index(edge)

if start in node_type:

name_alter = self.spec["nodes"][start][on_attribute]

self.logger.debug(f"value to be altered: {edge[0]}")

self.logger.debug(f"Name alter: {name_alter}")

start_alteration = f"{edge[0]}-{name_alter}"

else:

start_alteration = edge[0]

  

if end in node_type:

name_alter = self.spec["nodes"][end][on_attribute]

self.logger.debug(f"value to be altered: {edge[1]}")

self.logger.debug(f"Name alter: {name_alter}")

end_alteration = f"{edge[1]}-{name_alter}"

else:

end_alteration = edge[1]

  

self.edge_map[edge_name][edge_possition] = (

start_alteration,

end_alteration,

)

  

self.logger.debug(

f"Edge with altered name: {self.edge_map[edge_name][edge_possition]}"

)
