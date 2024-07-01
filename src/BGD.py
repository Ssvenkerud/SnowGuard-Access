import logging

import networkx as nx

from src.DataReciver import DataReciver


class BasicGraphDescription:

def __init__(self, graph=None):

self.logger = logging.getLogger("BasicGraphDescription")

self.logger.info("BasicGraphDescription object created")

if isinstance(graph, nx.DiGraph):

self.logger.info("Graph has been added")

self.graph = graph if graph else nx.DiGraph()

elif graph is None:

self.logger.info("Graph has not been added")

self.graph = nx.DiGraph()

else:

raise TypeError("Graph object must be instance of networkx.DiGraph")

  

def add_graph(self, graph):

if isinstance(graph, nx.DiGraph):

self.logger.info("Graph has been added")

self.graph = graph

else:

raise TypeError("Graph object must be instance of networkx.DiGraph")

  

def number_of_nodes(self):

self.logger.info("Calculating number of nodes")

self.number_of_nodes = self.graph.number_of_nodes()

self.logger.debug(f"Number of nodes: {self.number_of_nodes}")

return self.number_of_nodes

  

def number_of_edges(self):

self.logger.info("Calculating number of edges")

self.number_of_edges = self.graph.number_of_edges()

self.logger.debug(f"Number of edges: {self.number_of_edges}")

return self.number_of_edges

  

def is_complete_graph(self):

self.logger.info("Checking if graph is complete")

N = len(self.graph) - 1

self.is_complete_graph = not any(

n in nbrdict or len(nbrdict) != N for n, nbrdict in self.graph.adj.items()

)

self.logger.debug(f"Graph is complete: {self.is_complete_graph}")

return self.is_complete_graph

  

def exist_isolates(self):

self.logger.info("Checking if graph has isolates")

self.isolates_nodes = list(nx.isolates(self.graph))

if len(self.isolates_nodes) > 0:

self.logger.debug("Graph has isolates")

self.logger.debug(f"Isolates nodes: {self.isolates_nodes}")

self.exist_isolates = True

else:

self.exist_isolates = False

return self.exist_isolates

  

def weakly_connected(self):

self.logger.info("Checking if graph is weakly connected")

self.weakly_connected = nx.is_weakly_connected(self.graph)

self.logger.debug(f"Graph is weakly connected: {self.weakly_connected}")

return self.weakly_connected

  

def run(self):

self.logger.info("Running BasicGraphDescription")

self.number_of_nodes()

self.number_of_edges()

self.is_complete_graph()

self.exist_isolates()

self.weakly_connected()

self.logger.info("BasicGraphDescription has compleeted")
