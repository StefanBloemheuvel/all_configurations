from snowflake.snowpark import Session
import snowflake.snowpark.functions as F

config = {
    'account': 'bkng-bdx',
    'user': 'stefan.bloemheuvel@booking.com',
    'database': 'BDX_DATALAKE',
    'authenticator': 'externalBrowser',
}
 
spark = Session.builder.configs(config).create()



spark.table('personal_workspaces.sbloemheuvel.booker_preds_v1').show()



#### OR #####
from snowflake.snowpark import Session
import snowflake.snowpark.functions as F
import bkng
from bkng.bdx.context import Context
from bkng.bdx.snowflake import connect as bdx_snowflake_connect

ctx = Context.build()                          
sf_conn = bdx_snowflake_connect(ctx)           

snowpark_session = Session.builder.configs({"connection": sf_conn}).getOrCreate()

df = snowpark_session.table("fpa_sagemaker_bdx_dev.expt.utilization_preds_v2").toPandas()
