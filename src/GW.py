import logging

import networkx as nx


class GraphWarnings:

def __init__(self, graph=None):

self.logger = logging.getLogger("GraphWarnings")

self.logger.info("GraphWarnings object created")

if isinstance(graph, nx.DiGraph):

self.graph = graph

elif graph is None:

self.graph = nx.DiGraph()

else:

raise TypeError("Graph object must be instance of networkx.DiGraph")

  

def circularity(self):

self.logger.info("Checking for circularity")

self.circularity_nodes = []

circularity_check = nx.simple_cycles(self.graph)

for circle in circularity_check:

self.logger.debug(f"Circularity detected: {circle}")

self.circularity_nodes.append(circle)

self.logger.debug(f"Circularity nodes: {self.circularity_nodes}")

if len(list(self.circularity_nodes)) > 0:

return True

else:

return False

  

def add_graph(self, graph):

self.logger.info("Adding graph")

if isinstance(graph, nx.DiGraph):

self.graph = graph

else:

raise TypeError("Graph object must be instance of networkx.DiGraph")
