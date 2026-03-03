------- combine 1d time series from two tables

WITH T_TOTAL AS (
SELECT
  WEEK_START,
  REGION,
  CC1,
  prediction as merchant_adjusted
FROM fpa_sagemaker_bdx_dev.expt.utilization_preds_hotel_v4_adj
WHERE RUN_TYPE = 'INFERENCE' AND SCENARIO = 'Q2F_2026'
),

T_MERCHANT AS (
SELECT
  WEEK_START,
  YEAR_WEEK,
  REGION,
  CC1,
  PREDICTION as merchant
FROM 
fpa_sagemaker_bdx_dev.expt.utilization_preds_hotel_v4
WHERE RUN_TYPE = 'INFERENCE' AND SCENARIO = 'Q2F_2026' 
)

SELECT 
  REGION,
  CC1,
  YEAR_WEEK,
  WEEK_START::date  AS WEEK_START,
  merchant,
  merchant_adjusted
FROM T_MERCHANT JOIN T_TOTAL USING(WEEK_START, REGION,CC1 )
WHERE cc1 = 'fr'
ORDER BY REGION, CC1, WEEK_START
;



