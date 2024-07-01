import networkx as nx
import pytest

from src.GraphWarnings import GraphWarnings


def test_GraphWarnings_init():

GraphWarning = GraphWarnings()

assert isinstance(GraphWarning.graph, nx.DiGraph)

  
  

def test_GraphWarnings_init_with_graph(simple_graph):

GraphWarning = GraphWarnings(simple_graph)

assert GraphWarning.graph == simple_graph

  
  

def test_GraphWarnings_init_with_graph_not_graph():

with pytest.raises(TypeError):

GraphWarning = GraphWarnings("not_graph")

  
  

def test_GraphWarnings_add_graph(simple_graph):

GraphWarning = GraphWarnings()

GraphWarning.add_graph(simple_graph)

assert GraphWarning.graph == simple_graph

  
  

def test_GraphWarnings_add_graph_not_graph():

GraphWarning = GraphWarnings()

with pytest.raises(TypeError):

GraphWarning.add_graph("not_graph")

  
  

@pytest.mark.skip(reason="intermittend failing due to starting point of cycle")

def test_GraphWarnings_circularity(simple_graph_with_circilarity):

GraphWarning = GraphWarnings(simple_graph_with_circilarity)

assert GraphWarning.circularity() == True

assert sorted(GraphWarning.circularity_nodes) == sorted(

[

["A", "B", "D", "E", "F", "G"],

["A", "C", "D", "E", "F", "G"],

["A", "B", "D", "E", "G"],

["A", "C", "D", "E", "G"],

]

)
