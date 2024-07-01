import logging

import pytest

from src.DataReciver import DataReciver


def test_DataReciver_init():

Data = DataReciver()

assert Data.raw_data == None

  
  

def test_DataReciver_init_with_data(raw_snowflake_data, dbt_privelage_spec):

Data = DataReciver(dbt_privelage_spec, raw_snowflake_data)

assert Data.raw_data == raw_snowflake_data

assert Data.spec == dbt_privelage_spec

  
  

def test_DataReciver_nodes(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema, node_map

):

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_nodes()

assert Data.node_map["BUISNESS_UNIT"] == node_map["BUISNESS_UNIT"]

assert Data.node_map["DATABASE"] == node_map["DATABASE"]

assert Data.node_map["FUNCTIONAL_ROLE"] == node_map["FUNCTIONAL_ROLE"]

assert Data.node_map["ACCSESS_ROLE"] == node_map["ACCSESS_ROLE"]

assert Data.node_map["NAME"] == node_map["NAME"]

  
  

def test_DataReciver_edges(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema, edge_map

):

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_edges()

assert Data.edge_map["DATABASE-ACCSESS_ROLE"] == edge_map["DATABASE-ACCSESS_ROLE"]

assert (

Data.edge_map["ACCSESS_ROLE-FUNCTIONAL_ROLE"]

== edge_map["ACCSESS_ROLE-FUNCTIONAL_ROLE"]

)

assert Data.edge_map["FUNCTIONAL_ROLE-NAME"] == edge_map["FUNCTIONAL_ROLE-NAME"]

  
  

def test_DataReciver_get_edges(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema, edge_map

):

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_edges()

edges = Data.get_edges()

assert isinstance(edges, list)

assert isinstance(edges[0], tuple)

assert (

edges

== edge_map["DATABASE-ACCSESS_ROLE"]

+ edge_map["ACCSESS_ROLE-FUNCTIONAL_ROLE"]

+ edge_map["FUNCTIONAL_ROLE-NAME"]

)

  
  

def test_DataReciver_get_edges_empty():

Data = DataReciver()

edges = Data.get_edges()

assert isinstance(edges, list)

assert edges == []

  
  

def test_DataReciver_get_nodes(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema, node_map

):

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_nodes()

nodes = Data.get_nodes()

assert isinstance(nodes, list)

assert isinstance(nodes[0], str)

assert (

nodes

== node_map["BUISNESS_UNIT"]

+ node_map["DATABASE"]

+ node_map["FUNCTIONAL_ROLE"]

+ node_map["ACCSESS_ROLE"]

+ node_map["NAME"]

)

  
  

def test_DataReciver_get_node_attribute_static(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema

):

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_nodes()

atribute = Data.get_node_attributes("DWH_SAM")

assert atribute == {"type": "database"}

  
  

def test_DataReciver_attach_node_atributes(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema, caplog

):

caplog.set_level(logging.DEBUG)

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_nodes()

Data.attach_node_atributes()

assert Data.node_map["DATABASE"][0][1] == {"type": "database"}

  
  

def test_DataReciver_alter_node_name(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema, caplog

):

caplog.set_level(logging.DEBUG)

Data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

Data.extract_nodes()

Data.extract_edges()

Data.attach_node_atributes()

Data.alter_node_name(on_attribute="type")

  

assert Data.node_map["DATABASE"][0][0] == "DWH_SAM-database"

assert Data.node_map["NAME"][0][0] == "EMAIL.EMAIL@STOREBRAND.NO-user"

assert Data.edge_map["DATABASE-ACCSESS_ROLE"][0][0] == "DWH_SAM-database"

assert (

Data.edge_map["DATABASE-ACCSESS_ROLE"][0][1]

== "AR_SCHEMA_DWH_SAM_ESG_R-accsess_role"

)
