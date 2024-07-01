import json

import networkx as nx
import pytest

from src.DataReciver import DataReciver


@pytest.fixture

def raw_snowflake_data():

data = []

with open("tests/data/sf_user_privlage_table.txt") as load_file:

for line in load_file.readlines():

split_values = line.split(",")

clean_line = []

for value in split_values:

value = (

value.strip()

.replace("'", "")

.replace('"', "")

.replace("(", "")

.replace(")", "")

)

clean_line.append(value)

data.append(tuple(clean_line))

return data

  
  

@pytest.fixture

def graph_base_data(raw_snowflake_data):

from src.DataReciver import DataReciver

return DataReciver(raw_snowflake_data)

  
  

@pytest.fixture

def node_map():

with open("tests/data/node_map.json", "r") as file:

data = json.load(file)

return data

  
  

@pytest.fixture

def dbt_privelage_spec():

with open("tests/data/dbt_privelage_specification.json", "r") as file:

spec = json.load(file)

return spec

  
  

@pytest.fixture

def dbt_privlage_snowflake_schema():

schema = [

"BUISNESS_UNIT",

"DATABASE",

"FUNCTIONAL_ROLE",

"ACCSESS_ROLE",

"ACCSESS_TYPE",

"EMAIL",

"NAME",

]

return schema

  
  

@pytest.fixture

def edge_map():

data = {

"DATABASE-ACCSESS_ROLE": [

("DWH_SAM", "AR_SCHEMA_DWH_SAM_ESG_R"),

("DWH_SAM", "AR_SCHEMA_DWH_SAM_ESG_R"),

("DWH_SAM", "AR_SCHEMA_DWH_SAM_PRICE_R"),

("DWH_SAM", "AR_SCHEMA_DWH_SAM_FUND_ADMIN_R"),

("DDS_SAM", "AR_DB_DDS_SAM_R"),

("DDS_SAM", "AR_DB_DDS_SAM_R"),

("DDS_SAM", "AR_DB_DDS_SAM_R"),

("DEV_DDS_SAM", "DEV_AR_DB_DDS_SAM_R"),

("DEV_DDS_SAM", "DEV_AR_DB_DDS_SAM_W"),

("DWH_SAM", "AR_DB_DWH_SAM_R"),

("DEV_DWH_SAM", "DEV_AR_DB_DWH_SAM_R"),

("DEV_DWH_SAM", "DEV_AR_DB_DWH_SAM_W"),

("DDS_CORE_DATA_PLATFORM", "AR_DB_DDS_CORE_R"),

("DDS_CORE_DATA_PLATFORM", "AR_DB_DDS_CORE_W"),

("LANDING_MONITORING", "AR_DB_LANDING_MONITORING_R"),

],

"ACCSESS_ROLE-FUNCTIONAL_ROLE": [

("AR_SCHEMA_DWH_SAM_ESG_R", "DATA_ANALYST_OPERATIONS"),

("AR_SCHEMA_DWH_SAM_ESG_R", "DATA_ANALYST_OPERATIONS"),

("AR_SCHEMA_DWH_SAM_PRICE_R", "DATA_ANALYST_OPERATIONS"),

("AR_SCHEMA_DWH_SAM_FUND_ADMIN_R", "DATA_ANALYST_OPERATIONS"),

("AR_DB_DDS_SAM_R", "DATA_ANALYST_OPERATIONS"),

("AR_DB_DDS_SAM_R", "DATA_ANALYST_OPERATIONS"),

("AR_DB_DDS_SAM_R", "DATA_ENGINEER_SAM"),

("DEV_AR_DB_DDS_SAM_R", "DATA_ENGINEER_SAM"),

("DEV_AR_DB_DDS_SAM_W", "DATA_ENGINEER_SAM"),

("AR_DB_DWH_SAM_R", "DATA_ENGINEER_SAM"),

("DEV_AR_DB_DWH_SAM_R", "DATA_ENGINEER_SAM"),

("DEV_AR_DB_DWH_SAM_W", "DATA_ENGINEER_SAM"),

("AR_DB_DDS_CORE_R", "DATA_ENGINEER_PLATFORM"),

("AR_DB_DDS_CORE_W", "DATA_ENGINEER_PLATFORM"),

("AR_DB_LANDING_MONITORING_R", "DATA_ENGINEER_PLATFORM"),

],

"FUNCTIONAL_ROLE-NAME": [

("DATA_ANALYST_OPERATIONS", "EMAIL.EMAIL@STOREBRAND.NO"),

("DATA_ANALYST_OPERATIONS", "MONKEY.JUNGLE@STOREBRAND.NO"),

("DATA_ANALYST_OPERATIONS", "SNAKE.JUNGEL@STOREBRAND.NO"),

("DATA_ANALYST_OPERATIONS", "BEAR.JUNGEL@STOREBRAND.NO"),

("DATA_ANALYST_OPERATIONS", "MONKEY.JUNGEL@STOREBRAND.NO"),

("DATA_ANALYST_OPERATIONS", "SNAKE.JUNGEL@STOREBRAND.NO"),

("DATA_ENGINEER_SAM", "ELEFANT.JUNGEL@STREOBRAND.NO"),

("DATA_ENGINEER_SAM", "ELEFANT.JUNGEL@STREOBRAND.NO"),

("DATA_ENGINEER_SAM", "ELEFANT.JUNGEL@STREOBRAND.NO"),

("DATA_ENGINEER_SAM", "ELEFANT.JUNGEL@STREOBRAND.NO"),

("DATA_ENGINEER_SAM", "ELEFANT.JUNGEL@STREOBRAND.NO"),

("DATA_ENGINEER_SAM", "ELEFANT.JUNGEL@STREOBRAND.NO"),

("DATA_ENGINEER_PLATFORM", "COW.FARM@STOREBRAND.NO"),

("DATA_ENGINEER_PLATFORM", "COW.FARM@STOREBRAND.NO"),

("DATA_ENGINEER_PLATFORM", "HORSE.FARM@STOREBRAND.NO"),

],

}

return data

  
  

@pytest.fixture

def privlage_data(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema

):

privlage_data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

privlage_data.extract_nodes()

privlage_data.extract_edges()

return privlage_data

  
  

@pytest.fixture

def privlage_graph(privlage_data):

from src.PrivelageGraph import PrivelageGraph

graph = PrivelageGraph()

graph.add_data(privlage_data)

graph.add_edges_from_source()

graph.add_nodes_from_source()

return graph

  
  

@pytest.fixture

def attributed_privlage_data(

raw_snowflake_data, dbt_privelage_spec, dbt_privlage_snowflake_schema

):

privlage_data = DataReciver(

dbt_privelage_spec, raw_snowflake_data, dbt_privlage_snowflake_schema

)

privlage_data.extract_nodes()

privlage_data.extract_edges()

privlage_data.attach_node_atributes()

return privlage_data

  
  

@pytest.fixture

def simple_graph():

graph = nx.DiGraph()

graph.add_edges_from(

[

("A", "B"),

("A", "C"),

("B", "D"),

("C", "D"),

("D", "E"),

("E", "F"),

("E", "G"),

("F", "G"),

]

)

return graph

  
  

@pytest.fixture

def simple_graph_with_isolates():

graph = nx.DiGraph()

graph.add_edges_from(

[

("A", "B"),

("A", "C"),

("B", "D"),

("C", "D"),

("D", "E"),

("E", "F"),

("E", "G"),

("F", "G"),

]

)

graph.add_nodes_from(["H", "I"])

return graph

  
  

@pytest.fixture

def simple_graph_with_circilarity():

graph = nx.DiGraph()

graph.add_edges_from(

[

("A", "B"),

("A", "C"),

("B", "D"),

("C", "D"),

("D", "E"),

("E", "F"),

("E", "G"),

("F", "G"),

("G", "A"),

]

)

return graph

  
  

@pytest.fixture

def privlage_graph_with_atributes(privlage_data):

from src.PrivelageGraph import PrivelageGraph

graph = PrivelageGraph()

graph.add_data(privlage_data)

graph.add_edges_from_source()

graph.add_nodes_from_source()

graph.add_node_atributes()

return graph

  

@pytest.fixture

def exception_list():

exceptions = [

["AR_SCHEMA_DWH_SAM_ESG_R", "ELEFANT.JUNGEL@STREOBRAND.NO"],

["DDS_SAM", "DATA_ENGINEER_PLATFORM"]

]

return exceptions
