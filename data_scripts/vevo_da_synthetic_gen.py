#INSTALL PACKAGES
!pip install pandas numpy datetime

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuration for Vevo-specific dimensions
np.random.seed(42)
days = 30
platforms = ['YouTube', 'TCLtv+', 'Samsung TV Plus', 'Roku']
campaigns = ['Global_Spring_Launch_2026', 'Luxury_Auto_Evolve']

def generate_vevo_portfolio_data():
    date_range = [datetime(2026, 1, 1) + timedelta(days=x) for x in range(days)]

    # 1. YouTube Performance (Mock API Output)
    yt_records = []
    for d in date_range:
        for artist in ['Taylor Swift', 'SZA', 'Bad Bunny']:
            views = np.random.randint(50000, 150000)
            yt_records.append({
                'date': d, 'platform': 'YouTube', 'artist': artist,
                'views': views, 'impressions': int(views * 1.3), 'revenue': round(views * 0.008, 2)
            })

    # 2. FAST Channel Logs (Mock Partner CSVs - e.g., TCLtv+)
    fast_records = []
    for d in date_range:
        for channel in ['TCLtv+', 'Samsung TV Plus']:
            views = np.random.randint(5000, 20000)
            fast_records.append({
                'report_date': d, 'channel_name': channel, 'content_title': 'Top Hits 2026',
                'total_plays': views, 'ad_count': int(views * 1.1), 'gross_revenue': round(views * 0.035, 2)
            })

    # 3. Vevo Evolve Ad-Tech Logs (Internal Ad Server)
    evolve_records = []
    for d in date_range:
        for strategy in ['Contextual_AI', 'Demographic_Standard']:
            imps = np.random.randint(10000, 30000)
            # Higher CTR for Contextual AI
            ctr = 0.045 if strategy == 'Contextual_AI' else 0.021
            evolve_records.append({
                'log_ts': d, 'strategy': strategy, 'campaign': 'Global_Spring_Launch_2026',
                'impressions': imps, 'clicks': int(imps * ctr * np.random.uniform(0.9, 1.1))
            })

    pd.DataFrame(yt_records).to_csv('yt_raw.csv', index=False)
    pd.DataFrame(fast_records).to_csv('fast_raw.csv', index=False)
    pd.DataFrame(evolve_records).to_csv('evolve_raw.csv', index=False)

generate_vevo_portfolio_data()
