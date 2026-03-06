# Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- Git (for version control)
- Virtual environment (venv, conda, etc.)

## Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/stock-market-dashboard.git
cd stock-market-dashboard
```

### 2. Create Virtual Environment
```bash
# Using Python venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare Data Files
Ensure your CSV data files are in the `data/` directory:
- `combined_data.csv` - Main dataset
- `train_df.csv` - Training data
- `test_df.csv` - Test data
- `web_scrape.csv` - Web scraped sentiment data

### 5. Run the Application
```bash
python app.py
```

The application will start at `http://localhost:8050`

## Configuration

Edit `config.py` to customize:
- Data file paths
- Model paths
- Dash host and port
- Debug mode
- Application title

## Deploying to Render

### 1. Prepare Your Repository
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Create Render Web Service
1. Go to https://render.com
2. Create a new "Web Service"
3. Connect your GitHub repository
4. Select the stock-market-dashboard repository
5. Configure deployment:
   - **Name**: stock-market-dashboard
   - **Environment**: Python 3.11
   - **Region**: Choose closest to your users
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
   - **Plan**: Free (for testing) or paid (for production)

### 3. Set Environment Variables
In Render dashboard:
1. Go to your service settings
2. Add environment variables:
   - `DASH_PORT=8050` (Render assigns port automatically)
   - `DEBUG_MODE=False`
   - Any other custom variables

### 4. Deploy
Click "Create Web Service" - Render will automatically build and deploy

## Project Structure

```
stock-market-dashboard/
├── app.py                          # Main Dash application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── Procfile                        # Render deployment config
├── render.yaml                     # Alternative Render config
├── .gitignore                      # Git ignore rules
├── .env.example                    # Environment template
├── README.md                       # Full documentation
├── QUICKSTART.md                   # This file
│
├── src/
│   ├── callbacks/                  # Callback functions
│   ├── layouts/                    # UI layouts
│   ├── components/                 # Reusable components
│   └── utils/                      # Utility functions
│
├── data/                           # Data files
│   ├── combined_data.csv
│   ├── train_df.csv
│   ├── test_df.csv
│   └── web_scrape.csv
│
├── models/                         # Pre-trained models
│   ├── blr_model.pkl
│   ├── gn_model.pkl
│   ├── dt_model.pkl
│   └── rf_model.pkl
│
└── notebooks/                      # Original notebooks
    └── final_Stock_git_ready_copy.ipynb
```

## Features Overview

### 📊 EDA Charts
- Global Indices Time Series
- Rolling Volatility
- Box Plot Analysis
- Correlation Matrices
- Heatmaps

### 🎯 Model Performance
- Binary Logistic Regression
- Gaussian Naive Bayes
- Decision Tree
- Random Forest
- Confusion Matrices
- ROC Curves
- Feature Importance

### 💬 Sentiment Analysis
- VADER Analysis
- FinBERT Analysis
- WordCloud
- Web Scrape Integration

## Troubleshooting

### Issue: Data files not found
**Solution**: Ensure CSV files are in the `data/` directory and match the paths in `config.py`

### Issue: FinBERT model too large
**Solution**: The FinBERT model (~500MB) is downloaded on first use. For Render, consider preloading during build or using VADER only.

### Issue: Application won't start
**Solution**: Check requirements.txt versions are compatible. Try:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## Support & Contribution

For issues and questions:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Fork and submit pull requests

## License

MIT License - See LICENSE file

## Contact

Created with ❤️ for stock market analytics
