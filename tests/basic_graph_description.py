import networkx as nx
import pytest

from src.BasicGraphDescription import BasicGraphDescription


def test_BGD_init_with_graph(simple_graph):

BGD = BasicGraphDescription(simple_graph)

assert BGD.graph == simple_graph

  
  

def test_BGD_init_with_graph_not_graph():

with pytest.raises(TypeError):

BGD = BasicGraphDescription("not_graph")

  
  

def test_BGD_init_without_graph():

BGD = BasicGraphDescription()

assert isinstance(BGD.graph, nx.DiGraph)

  
  

def test_BGD_add_graph(simple_graph):

BGD = BasicGraphDescription()

BGD.add_graph(simple_graph)

assert BGD.graph == simple_graph

  
  

def test_BGD_add_graph_not_graph():

BGD = BasicGraphDescription()

with pytest.raises(TypeError):

BGD.add_graph("not_graph")

  
  

def test_number_of_nodes(simple_graph):

BGD = BasicGraphDescription(simple_graph)

assert BGD.number_of_nodes() == 7

  
  

def test_number_of_nodes_empty():

BGD = BasicGraphDescription()

assert BGD.number_of_nodes() == 0

  
  

def test_number_of_edges(simple_graph):

BGD = BasicGraphDescription(simple_graph)

assert BGD.number_of_edges() == 8

  
  

def test_number_of_edges_empty():

BGD = BasicGraphDescription()

assert BGD.number_of_edges() == 0

  
  

def test_is_complete_graph(simple_graph):

BGD = BasicGraphDescription(simple_graph)

assert BGD.is_complete_graph() == False

  
  

def test_exist_isolates(simple_graph):

BGD = BasicGraphDescription(simple_graph)

assert BGD.exist_isolates() == False

  
  

def test_exist_isolates_with_isolates(simple_graph_with_isolates):

BGD = BasicGraphDescription(simple_graph_with_isolates)

assert BGD.exist_isolates() == True

assert set(BGD.isolates_nodes) == set(["H", "I"])

  
  

def test_weakly_connected(simple_graph):

BGD = BasicGraphDescription(simple_graph)

assert BGD.weakly_connected() == True

  
  

def test_full_analysis(simple_graph):

BGD = BasicGraphDescription(simple_graph)

BGD.run()

assert BGD.number_of_nodes == 7

assert BGD.number_of_edges == 8

assert BGD.is_complete_graph == False

assert BGD.weakly_connected == True

assert BGD.exist_isolates == False

  
  

def test_full_analysis_privlage_graph(privlage_graph):

BGD = BasicGraphDescription(privlage_graph.graph)

BGD.run()

assert BGD.number_of_nodes == 31

assert BGD.number_of_edges == 33

assert BGD.is_complete_graph == False

assert BGD.weakly_connected == False

assert BGD.exist_isolates == True

assert BGD.isolates_nodes == ["SAM", "CORE"]
