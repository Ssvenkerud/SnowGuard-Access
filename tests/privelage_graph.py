import logging

import networkx as nx
import pytest

from src.PrivelageGraph import PrivelageGraph


def test_PrivelageGraph_init():

Privelage = PrivelageGraph()

assert isinstance(Privelage.graph, nx.DiGraph)

  
  

def test_PrivelageGraph_init_data_none():

Privelage = PrivelageGraph()

assert Privelage.raw_data == []

  
  

def test_PrivelageGraph_add_data(privlage_data):

Privelage = PrivelageGraph()

Privelage.add_data(privlage_data)

assert Privelage.raw_data[0] == privlage_data

  
  

def test_PrivelageGraph_add_data_not_data_reciver():

Privelage = PrivelageGraph()

with pytest.raises(TypeError):

Privelage.add_data("not_data_reciver")

  
  

def test_PrivelageGraph_add_edges_from_source(privlage_data):

Privelage = PrivelageGraph()

Privelage.add_data(privlage_data)

Privelage.add_edges_from_source()

assert set(Privelage.graph.edges) == set(privlage_data.get_edges())

  
  

def test_PrivelageGraph_add_edges_from_source_empty():

Privelage = PrivelageGraph()

Privelage.add_edges_from_source()

assert set(Privelage.graph.edges) == set([])

  
  

def test_PrivelageGraph_add_nodes_from_source(privlage_data):

Privelage = PrivelageGraph()

Privelage.add_data(privlage_data)

Privelage.add_nodes_from_source()

assert set(Privelage.graph.nodes) == set(privlage_data.get_nodes())

  
  

def test_PrivelageGraph_add_nodes_from_source_empty():

Privelage = PrivelageGraph()

Privelage.add_nodes_from_source()

assert set(Privelage.graph.nodes) == set([])

  
  

def test_PrivelageGraph_add_nodes_and_edges_from_source(privlage_data):

Privelage = PrivelageGraph()

Privelage.add_data(privlage_data)

Privelage.add_edges_from_source()

Privelage.add_nodes_from_source()

assert set(Privelage.graph.nodes) == set(privlage_data.get_nodes())

assert set(Privelage.graph.edges) == set(privlage_data.get_edges())

  
  

def test_PrivelageGraph_node_attribute_type(privlage_data):

Privelage = PrivelageGraph()

Privelage.add_data(privlage_data)

Privelage.add_edges_from_source()

Privelage.add_nodes_from_source()

Privelage.add_node_atributes()

assert Privelage.graph.nodes["DWH_SAM"]["type"] == "database"

assert Privelage.graph.nodes["DDS_SAM"]["type"] == "database"

assert Privelage.graph.nodes["DATA_ANALYST_OPERATIONS"]["type"] == "functional_role"

assert Privelage.graph.nodes["DATA_ENGINEER_SAM"]["type"] == "functional_role"

assert Privelage.graph.nodes["AR_SCHEMA_DWH_SAM_ESG_R"]["type"] == "accsess_role"

assert Privelage.graph.nodes["AR_SCHEMA_DWH_SAM_PRICE_R"]["type"] == "accsess_role"

assert Privelage.graph.nodes["AR_DB_DDS_CORE_W"]["type"] == "accsess_role"

assert Privelage.graph.nodes["MONKEY.JUNGLE@STOREBRAND.NO"]["type"] == "user"

assert Privelage.graph.nodes["COW.FARM@STOREBRAND.NO"]["type"] == "user"

  
  

def test_PrivelageGraph_node_attribute_type_empty(privlage_data):

Privelage = PrivelageGraph()

Privelage.add_data(privlage_data)

Privelage.add_edges_from_source()

Privelage.add_nodes_from_source()

Privelage.graph.add_node("test_node")

Privelage.add_node_atributes()

assert Privelage.graph.nodes["DWH_SAM"]["type"] == "database"

assert Privelage.graph.nodes["DDS_SAM"]["type"] == "database"

assert Privelage.graph.nodes["DATA_ANALYST_OPERATIONS"]["type"] == "functional_role"

assert Privelage.graph.nodes["DATA_ENGINEER_SAM"]["type"] == "functional_role"

assert Privelage.graph.nodes["AR_SCHEMA_DWH_SAM_ESG_R"]["type"] == "accsess_role"

assert Privelage.graph.nodes["AR_SCHEMA_DWH_SAM_PRICE_R"]["type"] == "accsess_role"

assert Privelage.graph.nodes["AR_DB_DDS_CORE_W"]["type"] == "accsess_role"

assert Privelage.graph.nodes["test_node"]["type"] == "unknown"

  
  

def test_PrivelageGraph_artibuted_nodes(attributed_privlage_data, caplog):

caplog.set_level(logging.DEBUG)

Privelage = PrivelageGraph()

Privelage.add_data(attributed_privlage_data)

Privelage.add_edges_from_source()

Privelage.add_nodes_from_source()

Privelage.graph.add_node("test_node")

Privelage.add_node_atributes()

  

assert Privelage.graph.nodes["DWH_SAM"]["type"] == "database"

assert Privelage.graph.nodes["DDS_SAM"]["type"] == "database"

assert Privelage.graph.nodes["DATA_ANALYST_OPERATIONS"]["type"] == "functional_role"

assert Privelage.graph.nodes["DATA_ENGINEER_SAM"]["type"] == "functional_role"

assert Privelage.graph.nodes["AR_SCHEMA_DWH_SAM_ESG_R"]["type"] == "accsess_role"

assert Privelage.graph.nodes["AR_SCHEMA_DWH_SAM_PRICE_R"]["type"] == "accsess_role"

assert Privelage.graph.nodes["AR_DB_DDS_CORE_W"]["type"] == "accsess_role"

assert Privelage.graph.nodes["test_node"]["type"] == "unknown"
