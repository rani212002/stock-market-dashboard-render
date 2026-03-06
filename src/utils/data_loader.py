"""
Data loading and preprocessing utilities
"""

import pandas as pd
import numpy as np
from pathlib import Path
import config

def load_combined_data():
    """Load combined market data from CSV"""
    try:
        df = pd.read_csv(config.COMBINED_DATA_PATH)
        
        # Ensure required time period columns exist
        if 'Year' not in df.columns and df.index is not None:
            df['Year'] = pd.to_datetime(df.index).year
        
        if 'Quarter' not in df.columns and df.index is not None:
            df['Quarter'] = pd.to_datetime(df.index).quarter.map({1:'Q1', 2:'Q2', 3:'Q3', 4:'Q4'})
        
        print(f"✅ Combined data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"❌ Combined data file not found at {config.COMBINED_DATA_PATH}")
        return pd.DataFrame()
    except Exception as e:
        print(f"❌ Error loading combined data: {e}")
        return pd.DataFrame()

def load_training_data():
    """Load training dataset for ML models"""
    try:
        df = pd.read_csv(config.TRAIN_DATA_PATH)
        print(f"✅ Training data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"⚠️ Training data not found at {config.TRAIN_DATA_PATH}")
        return pd.DataFrame()
    except Exception as e:
        print(f"⚠️ Error loading training data: {e}")
        return pd.DataFrame()

def load_test_data():
    """Load test dataset for ML model evaluation"""
    try:
        df = pd.read_csv(config.TEST_DATA_PATH)
        print(f"✅ Test data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"⚠️ Test data not found at {config.TEST_DATA_PATH}")
        return pd.DataFrame()
    except Exception as e:
        print(f"⚠️ Error loading test data: {e}")
        return pd.DataFrame()

def load_web_scrape_data():
    """Load web scraped data for sentiment analysis"""
    try:
        df = pd.read_csv(config.WEB_SCRAPE_PATH)
        print(f"✅ Web scrape data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"⚠️ Web scrape data not found at {config.WEB_SCRAPE_PATH}")
        return pd.DataFrame()
    except Exception as e:
        print(f"⚠️ Error loading web scrape data: {e}")
        return pd.DataFrame()

def prepare_correlation_matrices(combined_data):
    """Prepare correlation matrices for visualization"""
    try:
        returns_cols = ['NSE_Return', 'DJI_Return', 'IXIC_Return', 'HSI_Return', 'N225_Return', 'GDAXI_Return']
        
        # Matrix A: 6-year daily returns correlation
        corr_A = combined_data[returns_cols].corr()
        
        # Matrix B: 2024 daily returns correlation
        combined_data_2024 = combined_data[combined_data['Year'] == 2024]
        corr_B = combined_data_2024[returns_cols].corr()
        
        print(f"✅ Correlation matrices prepared: A={corr_A.shape}, B={corr_B.shape}")
        return corr_A, corr_B
    except Exception as e:
        print(f"⚠️ Error preparing correlation matrices: {e}")
        return None, None

def prepare_summary_stats(combined_data):
    """Prepare summary statistics for global indices"""
    try:
        global_indices = [
            'NSE_Return', 'DJI_Return', 'IXIC_Return',
            'HSI_Return', 'N225_Return', 'GDAXI_Return', 'VIX_Return'
        ]
        
        summary = combined_data.groupby('Nifty_Open_Dir')[global_indices].agg(['mean', 'median', 'std'])
        print(f"✅ Summary statistics prepared: shape {summary.shape}")
        return summary
    except Exception as e:
        print(f"⚠️ Error preparing summary statistics: {e}")
        return None

# Pre-load all data on module import
print("📚 Loading all required data...")
combined_data = load_combined_data()
train_data = load_training_data()
test_data = load_test_data()
web_scrape_data = load_web_scrape_data()

if not combined_data.empty:
    corr_A, corr_B = prepare_correlation_matrices(combined_data)
    summary_stats = prepare_summary_stats(combined_data)
else:
    corr_A = corr_B = summary_stats = None

print("✅ Data loading complete!\n")
