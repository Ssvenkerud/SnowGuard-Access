import pytest


def test_raw_data_touple(raw_snowflake_data):

assert isinstance(raw_snowflake_data, list)

assert isinstance(raw_snowflake_data[0], tuple)

  
  

def test_raw_data_touple_len(raw_snowflake_data):

assert len(raw_snowflake_data[0]) == 7

  
  

def test_raw_data_touple_content(raw_snowflake_data):

assert raw_snowflake_data[0] == (

"SAM",

"DWH_SAM",

"DATA_ANALYST_OPERATIONS",

"AR_SCHEMA_DWH_SAM_ESG_R",

"Read",

"EMAIL.EMAIL@STOREBRAND.NO",

"EMAIL.EMAIL@STOREBRAND.NO",

)

  
  

def test_raw_data_touple_indexable(raw_snowflake_data):

assert raw_snowflake_data[0][0] == "SAM"
