import logging
import warnings

import networkx as nx

from src.PrivelageGraph import PrivelageGraph


class DenyAccsess:

def __init__(self, privelage_graph, exceptions=[]):

self.logger = logging.getLogger("DenyAccsess")

self.logger.info("DenyAccsess object created")

self.privelage_graph = privelage_graph

self.exceptions = exceptions

self.database_accsess = []

self.ar_accsess = []

  

def __atribute_based_direct_path(self, start_node_type, end_note_type):

self.logger.debug(

f"Checking for direct path between {start_node_type} and {end_note_type}"

)

path_exists = False

detected_paths = []

start_nodes = [

node

for node, attribute in self.privelage_graph.graph.nodes(data=True)

if attribute["type"] == start_node_type

]

self.logger.debug(f"Start nodes: {start_nodes}")

end_nodes = [

node

for node, attribute in self.privelage_graph.graph.nodes(data=True)

if attribute["type"] == end_note_type

]

self.logger.debug(f"End nodes: {end_nodes}")

for start_node in start_nodes:

for end_node in end_nodes:

self.logger.debug(

f"Checking for path between {start_node} and {end_node}"

)

if [start_node, end_node] in self.exceptions:

self.logger.debug(

f"Path between {start_node} and {end_node} is an exception"

)

continue

else:

paths = nx.all_simple_paths(

self.privelage_graph.graph, start_node, end_node, cutoff=1

)

flattend_paths = [item for sublist in list(paths) for item in sublist]

self.logger.debug(

f"Paths for {start_node} to {end_node}: {flattend_paths}"

)

if len(flattend_paths) > 0:

path_exists = True

detected_paths.append(flattend_paths)

self.logger.debug(f"Detected paths: {detected_paths}")

self.logger.debug(f"Path exists: {path_exists}")

return path_exists, detected_paths

  

def DB_to_User(self):

self.logger.info("Checking for direct path between database and user")

path_exists, detected_paths = self.__atribute_based_direct_path(

"database", "user"

)

self.logger.debug(f"pre append database accsess: {self.database_accsess}")

self.database_accsess += detected_paths

self.logger.debug(f"post append database accsess: {self.database_accsess}")

self.logger.debug(f"Database to user paths tested, path exists: {path_exists}")

return path_exists

  

def DB_to_Functional_role(self):

self.logger.info(

"Checking for direct path between database and functional role"

)

path_exists, detected_paths = self.__atribute_based_direct_path(

"database", "functional_role"

)

self.logger.debug(f"pre append database accsess: {self.database_accsess}")

self.database_accsess += detected_paths

self.logger.debug(f"post append database accsess: {self.database_accsess}")

self.logger.debug(

f"Database to functional role paths tested, path exists: {path_exists}"

)

return path_exists

  

def Accsess_role_to_User(self):

self.logger.info("Checking for direct path between accsess role and user")

path_exists, detected_paths = self.__atribute_based_direct_path(

"accsess_role", "user"

)

self.logger.debug(f"pre append ar accsess: {self.ar_accsess}")

self.ar_accsess += detected_paths

self.logger.debug(f"post append ar accsess: {self.ar_accsess}")

self.logger.debug(

f"Accsess role to user paths tested, path exists: {path_exists}"

)

return path_exists
