-- 1. YouTube Staging Table
CREATE OR REPLACE TABLE `driiiportfolio.vevo_omni_performance.stg_youtube_performance` (
    event_date DATE,
    platform STRING,
    artist STRING,
    views INT64,
    impressions INT64,
    revenue FLOAT64
);

-- 2. FAST Channel Staging Table
CREATE OR REPLACE TABLE `driiiportfolio.vevo_omni_performance.stg_fast_channel_logs` (
    report_date DATE,
    channel_name STRING,
    content_title STRING,
    total_plays INT64,
    ad_count INT64,
    gross_revenue FLOAT64
);

-- 3. Vevo Evolve Staging Table
CREATE OR REPLACE TABLE `driiiportfolio.vevo_omni_performance.stg_vevo_evolve_logs` (
    log_ts TIMESTAMP,
    strategy STRING,
    campaign STRING,
    impressions INT64,
    clicks INT64
);
