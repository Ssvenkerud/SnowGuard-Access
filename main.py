import datetime
import json
import logging
import os

from src.BasicGraphDescription import BasicGraphDescription
from src.DataReciver import DataReciver
from src.DenyAccsess import DenyAccsess
from src.PrivelageGraph import PrivelageGraph


def privelage_spec(file_path):

with open(file_path, "r") as file:

spec = json.load(file)

return spec

  
  

def main(snowflake_connection, logger):

logger = logger

database_query = "SELECT PRIVILEGE, GRANTED_ON, NAME as DATABASE, GRANTEE_NAME FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES WHere (PRIVILEGE!='OWNERSHIP') AND (GRANTED_ON in ('DATABASE')) AND (NAME NOT LIKE('SB_%')) AND (DELETED_ON is null)"

accsess_roles_query = "SELECT PRIVILEGE, GRANTED_ON, NAME as AR_ROLE, GRANTEE_NAME FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES WHERE (PRIVILEGE!='OWNERSHIP') AND (NAME LIKE '%AR_%')AND (GRANTED_ON in ('ROLE')) AND (DELETED_ON is null)"

functional_roles_query = "SELECT PRIVILEGE, GRANTED_ON, NAME as FUNCTIONAL_ROLE, GRANTEE_NAME FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES WHERE (PRIVILEGE!='OWNERSHIP') AND (NAME NOT LIKE '%AR_%')AND (GRANTED_ON in ('ROLE')) AND (DELETED_ON is null)"

users_query = "select ROLE, GRANTEE_NAME as USERS from SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_USERS WHERE (DELETED_ON is null)"

  

try:

logger.info("Querying snowflake for databases")

  

sf_databases = (

snowflake_connection.cursor()

.execute(database_query)

.fetchall()

)

sf_databases_metadata = snowflake_connection.cursor().describe(database_query)

sf_databases_schema = [col.name for col in sf_databases_metadata]

  

logger.info(f"Snowflake databases retrived")

  

logger.info("Querying snowflake for accsess roles")

sf_accsess_roles = (

snowflake_connection.cursor()

.execute(accsess_roles_query )

.fetchall()

)

sf_accsess_roles_metadata = snowflake_connection.cursor().describe(accsess_roles_query)

sf_accsess_roles_schema = [col.name for col in sf_accsess_roles_metadata]

  

logger.info(f"Snowflake accsess roles retrived")

  

logger.info("Querying snowflake for functional roles")

sf_functional_roles = (

snowflake_connection.cursor()

.execute(functional_roles_query)

.fetchall()

)

sf_functional_roles_metadata = snowflake_connection.cursor().describe(functional_roles_query)

sf_functional_roles_schema = [col.name for col in sf_functional_roles_metadata]

logger.info(f"Snowflake functional roles retrived")

  

logger.info("Querying snowflake for users")

sf_users = (

snowflake_connection.cursor()

.execute(users_query)

.fetchall()

)

sf_users_metadata = snowflake_connection.cursor().describe(users_query)

sf_users_schema = [col.name for col in sf_users_metadata]

  

logger.info(f"Snowflake users retrived")

  

finally:

snowflake_connection.close()

logger.info(f"Snowflake connection closed")

  

try:

logger.info(f"Loading graph specs")

sf_databases_spec = privelage_spec("spec/sf_databases.json")

sf_accsess_roles_spec = privelage_spec("spec/sf_ar_roles.json")

sf_functional_roles_spec = privelage_spec("spec/sf_functional_roles.json")

sf_users_spec = privelage_spec("spec/sf_users.json")

exception_spec = privelage_spec("spec/exceptions.json")["exceptions"]

logger.info(f"Graph specs loaded")

  

except:

logger.info(f"Privelage spec failed to load.")

raise Exception("Privelage spec failed to load.")

  

cleaned_databases = DataReciver(

sf_databases_spec, sf_databases, sf_databases_schema

)

cleaned_databases.extract_edges()

cleaned_databases.extract_nodes()

cleaned_databases.attach_node_atributes()

logger.info(f"Databases extracted")

  

cleaned_accsess_roles = DataReciver(

sf_accsess_roles_spec, sf_accsess_roles, sf_accsess_roles_schema

)

cleaned_accsess_roles.extract_edges()

cleaned_accsess_roles.extract_nodes()

cleaned_accsess_roles.attach_node_atributes()

logger.info(f"Accsess roles extracted")

  

cleaned_functional_roles = DataReciver(

sf_functional_roles_spec, sf_functional_roles, sf_functional_roles_schema

)

cleaned_functional_roles.extract_edges()

cleaned_functional_roles.extract_nodes()

cleaned_functional_roles.attach_node_atributes()

logger.info(f"Functional roles extracted")

  

cleaned_users = DataReciver(sf_users_spec, sf_users, sf_users_schema)

cleaned_users.extract_edges()

cleaned_users.extract_nodes()

cleaned_users.attach_node_atributes()

cleaned_users.alter_node_name(on_attribute="type")

logger.info(f"Users extracted")

  

Privelages = PrivelageGraph()

for Cleaned_Privelage_data in [

cleaned_databases,

cleaned_accsess_roles,

cleaned_functional_roles,

cleaned_users,

]:

Privelages.add_data(Cleaned_Privelage_data)

  

Privelages.add_edges_from_source()

Privelages.add_nodes_from_source()

Privelages.add_node_atributes()

logger.info(f"Privelage graph Compleeted")

  

Basic_description = BasicGraphDescription(Privelages.graph)

Basic_description.run()

logger.info(f"Basic graph description compleeted")

  

Error_monitor = DenyAccsess(Privelages, exceptions=exception_spec)

DB_User_Check = Error_monitor.DB_to_User()

DB_Functional_Check = Error_monitor.DB_to_Functional_role()

Accsess_User_Check = Error_monitor.Accsess_role_to_User()

logger.info(f"Accsess monitor compleeted")

  
  

logger.info(f"Run compleeted, start reporting")

logger.info("")

logger.info("")

logger.info("")

logger.info("================== Basic information =========================")

logger.info(f"Graph is complete: {Basic_description.is_complete_graph}")

logger.info(f"Graph has isolates: {Basic_description.exist_isolates}")

if Basic_description.exist_isolates == True:

logger.info(f"Isolates: {Basic_description.isolates_nodes}")

logger.info(f"Graph is weakly connected: {Basic_description.weakly_connected}")

logger.info(f"Number of nodes: {Basic_description.number_of_nodes}")

logger.info(f"Number of edges: {Basic_description.number_of_edges}")

logger.info("==============================================================")

notifiation_sting =""

if (

(DB_User_Check == True)

or (DB_Functional_Check == True)

or (Accsess_User_Check == True)

):

notifiation_sting = f"""

"Accsess error detected"

==================== Type of access error =======================

"DB_User_Check: {DB_User_Check}"

"DB_Functional_Check: {DB_Functional_Check}"

"Accsess_User_Check: {Accsess_User_Check}"

"""

  

logger.error("")

logger.error(f"Accsess error detected")

logger.error(

"==================== Type of access error ======================="

)

logger.error(f"DB_User_Check: {DB_User_Check}")

logger.error(f"DB_Functional_Check: {DB_Functional_Check}")

logger.error(f"Accsess_User_Check: {Accsess_User_Check}")

if (DB_User_Check == True) or (DB_Functional_Check == True):

notifiation_sting += f"""

==================== Data bases can be accsessed directly!! =======================

Detected Paths: {Error_monitor.database_accsess}

===========================================

"""

  

if Accsess_User_Check == True:

notifiation_sting +=f"""

==================== Users Granted accsess roles!! =======================

Detected Paths: {Error_monitor.ar_accsess}

===========================================

"""

if notifiation_sting != "":

logger.error(notifiation_sting)

  

return notifiation_sting
