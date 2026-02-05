CREATE OR REPLACE VIEW `driiiportfolio.vevo_omni_performance.v_unified_revenue_efficiency` AS
WITH youtube_union AS (
  SELECT 
    date AS report_date,
    platform,
    artist AS content_identity,
    views,
    impressions,
    revenue,
    SAFE_DIVIDE(revenue, impressions) * 1000 AS cpm
  FROM `driiiportfolio.vevo_omni_performance.stg_youtube_performance`
),
fast_union AS (
  SELECT 
    report_date,
    channel_name AS platform,
    content_title AS content_identity, -- Dynamic: Uses the actual data from the table
    total_plays AS views,
    ad_count AS impressions,
    gross_revenue AS revenue,
    SAFE_DIVIDE(gross_revenue, ad_count) * 1000 AS cpm
  FROM `driiiportfolio.vevo_omni_performance.stg_fast_channel_logs`
)
SELECT * FROM youtube_union
UNION ALL
SELECT * FROM fast_union;
