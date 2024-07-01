import logging

import networkx as nx

from src.DataReciver import DataReciver


class PrivelageGraph:

def __init__(self):

self.logger = logging.getLogger("PrivelageGraph")

self.logger.info("Creating Privelage Graph")

self.raw_data = []

self.graph = nx.DiGraph()

  

def add_data(self, data):

if isinstance(data, DataReciver):

self.logger.info(f"Adding Data reciver object to Privelage Graph")

self.raw_data.append(data)

else:

raise TypeError("Data object must be instance of DataReciver")

  

def add_edges_from_source(self):

self.logger.info("Adding edges from source")

for data_objects in self.raw_data:

self.graph.add_edges_from(data_objects.get_edges())

  

def add_nodes_from_source(self):

self.logger.info("Adding nodes from source")

for data_objects in self.raw_data:

self.graph.add_nodes_from(data_objects.get_nodes())

  

def add_node_atributes(self):

for data_objects in self.raw_data:

self.logger.info(f"Adding node attributes")

for node in data_objects.get_nodes():

if isinstance(node, tuple) == True:

continue

self.graph.nodes[node].update(data_objects.get_node_attributes(node))

for node in self.graph.nodes:

self.logger.debug(f"Node {node} attributes: {self.graph.nodes[node]}")

if self.graph.nodes[node].get("type") is None:

self.graph.nodes[node].update({"type": "unknown"})
