import networkx as nx
import pytest

from src.DenyAccsess import DenyAccsess


def test_DenyAccsess_DB_to_User(privlage_graph_with_atributes):

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result = Deny.DB_to_User()

assert check_result == False

  
  

def test_DenyAccsess_DB_to_User_with_path(privlage_graph_with_atributes):

privlage_graph_with_atributes.graph.add_edge(

"DWH_SAM", "SNAKE.JUNGEL@STOREBRAND.NO"

)

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result = Deny.DB_to_User()

assert check_result == True

assert Deny.database_accsess == [["DWH_SAM", "SNAKE.JUNGEL@STOREBRAND.NO"]]

  
  

def test_DenyAccsess_DB_to_Functional_role(privlage_graph_with_atributes):

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result = Deny.DB_to_Functional_role()

assert check_result == False

assert Deny.database_accsess == []

  
  

def test_DenyAccsess_DB_to_Functional_role_with_path(privlage_graph_with_atributes):

privlage_graph_with_atributes.graph.add_edge("DWH_SAM", "DATA_ANALYST_OPERATIONS")

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result = Deny.DB_to_Functional_role()

assert check_result == True

assert Deny.database_accsess == [["DWH_SAM", "DATA_ANALYST_OPERATIONS"]]

  
  

def test_DenyAccsess_DB_to_User_and_Functional_role(privlage_graph_with_atributes):

privlage_graph_with_atributes.graph.add_edge("DWH_SAM", "DATA_ANALYST_OPERATIONS")

privlage_graph_with_atributes.graph.add_edge(

"DWH_SAM", "SNAKE.JUNGEL@STOREBRAND.NO"

)

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result_user = Deny.DB_to_User()

check_result_functional_role = Deny.DB_to_Functional_role()

assert check_result_user == True

assert check_result_functional_role == True

assert Deny.database_accsess == [

["DWH_SAM", "SNAKE.JUNGEL@STOREBRAND.NO"],

["DWH_SAM", "DATA_ANALYST_OPERATIONS"],

]

  
  

def test_DenyAccsess_Accsess_role_to_User(privlage_graph_with_atributes):

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result = Deny.Accsess_role_to_User()

assert check_result == False

assert Deny.ar_accsess == []

  
  

def test_DenyAccsess_Accsess_role_to_User_with_path(privlage_graph_with_atributes):

privlage_graph_with_atributes.graph.add_edge(

"AR_SCHEMA_DWH_SAM_ESG_R", "SNAKE.JUNGEL@STOREBRAND.NO"

)

Deny = DenyAccsess(privlage_graph_with_atributes)

check_result = Deny.Accsess_role_to_User()

assert check_result == True

assert Deny.ar_accsess == [

["AR_SCHEMA_DWH_SAM_ESG_R", "SNAKE.JUNGEL@STOREBRAND.NO"]

]

  

def test_DenyAccsess_with_Exception(privlage_graph_with_atributes, exception_list):

privlage_graph_with_atributes.graph.add_edge(

"AR_SCHEMA_DWH_SAM_ESG_R", "ELEFANT.JUNGEL@STREOBRAND.NO")

privlage_graph_with_atributes.graph.add_edge(

"DDS_SAM", "DATA_ENGINEER_PLATFORM")

Deny = DenyAccsess(privlage_graph_with_atributes, exceptions=exception_list)

ar_check_result = Deny.Accsess_role_to_User()

assert ar_check_result == False

assert Deny.ar_accsess == []

db_check_result = Deny.DB_to_Functional_role()

assert Deny.database_accsess == []

assert db_check_result == False
