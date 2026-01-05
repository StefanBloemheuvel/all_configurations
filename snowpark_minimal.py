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
