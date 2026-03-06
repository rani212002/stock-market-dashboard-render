import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Data paths
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
NOTEBOOK_DIR = BASE_DIR / "notebooks"

# Data files
COMBINED_DATA_PATH = DATA_DIR / "combined_data.csv"
TRAIN_DATA_PATH = DATA_DIR / "train_df.csv"
TEST_DATA_PATH = DATA_DIR / "test_df.csv"
WEB_SCRAPE_PATH = DATA_DIR / "web_scrape.csv"

# Model paths
BLR_MODEL_PATH = MODEL_DIR / "blr_model.pkl"
GNB_MODEL_PATH = MODEL_DIR / "gn_model.pkl"
DT_MODEL_PATH = MODEL_DIR / "dt_model.pkl"
RF_MODEL_PATH = MODEL_DIR / "rf_model.pkl"

# Dash settings
DASH_HOST = os.getenv('DASH_HOST', '0.0.0.0')
DASH_PORT = int(os.getenv('DASH_PORT', 8050))
DEBUG_MODE = os.getenv('DEBUG_MODE', 'True') == 'True'

# App settings
APP_TITLE = "📈 Stock Market Analytics Dashboard"
APP_SUBTITLE = "Comprehensive analysis of 2.5 year global markets data with 4 ML models"

# Feature settings
SENTIMENT_MODELS = ['VADER', 'FinBERT']
ML_MODELS = ['Binary Logistic Regression', 'Gaussian Naive Bayes', 'Decision Tree', 'Random Forest']
