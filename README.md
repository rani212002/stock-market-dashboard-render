# Stock Market Analytics Dashboard

A comprehensive Dash-based web application for analyzing global stock market data with machine learning models and sentiment analysis.

## 📊 Features

### 1. **Exploratory Data Analysis (EDA)**
   - Global Indices Time Series Analysis
   - Rolling Volatility Visualization
   - Box Plot Distribution Analysis
   - Combined Heatmap (Median & Mean Returns)
   - Interactive Correlation Matrices
   - Global Indices vs Market Direction Analysis

### 2. **Model Performance**
   - **4 Machine Learning Models:**
     - Binary Logistic Regression (AUC: 0.7051)
     - Gaussian Naive Bayes (AUC: 0.7033)
     - Decision Tree (AUC: 0.6198)
     - Random Forest (AUC: 0.6452)
   - Interactive Model Selection Dropdown
   - Confusion Matrix Visualization
   - ROC Curve Analysis
   - Feature Importance Plots (Random Forest)
   - Decision Tree Visualization
   - Performance Metrics Table

### 3. **Sentiment Analysis**
   - **VADER Sentiment Analysis**
   - **FinBERT Sentiment Analysis**
   - Real-time Sentiment Distribution Charts
   - WordCloud Visualization
   - Sentiment Score Histogram
   - Top 10 Data Rows Table (Web Scrape Data)

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/stock-market-dashboard.git
cd stock-market-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:8050` in your browser.

### Deploy to Render

1. Push your code to GitHub
2. Connect your GitHub repository to Render
3. Create a new Web Service
4. Select Python as the runtime
5. Set the build command: `pip install -r requirements.txt`
6. Set the start command: `gunicorn app:server`
7. Deploy!

## 📁 Project Structure

```
stock-market-dashboard/
├── app.py                          # Main Dash application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render deployment config
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
│
├── src/
│   ├── __init__.py
│   ├── callbacks/                  # Callback functions
│   │   ├── __init__.py
│   │   ├── eda_callbacks.py       # EDA callbacks
│   │   ├── model_callbacks.py     # Model callbacks
│   │   └── sentiment_callbacks.py # Sentiment callbacks
│   │
│   ├── layouts/                    # UI Layouts
│   │   ├── __init__.py
│   │   ├── eda_layout.py          # EDA tab layout
│   │   ├── model_layout.py        # Model tab layout
│   │   └── sentiment_layout.py    # Sentiment tab layout
│   │
│   ├── components/                 # Reusable components
│   │   ├── __init__.py
│   │   └── chart_utils.py         # Utility functions
│   │
│   └── utils/                      # Utilities
│       ├── __init__.py
│       ├── data_loader.py         # Data loading functions
│       └── sentiment_analyzer.py  # Sentiment analysis functions
│
├── data/                           # Data files
│   ├── combined_data.csv          # Main dataset
│   ├── train_df.csv               # Training data
│   ├── test_df.csv                # Test data
│   └── web_scrape.csv             # Web scraped data
│
├── models/                         # Pre-trained models
│   ├── blr_model.pkl              # Binary Logistic Regression
│   ├── gn_model.pkl               # Gaussian Naive Bayes
│   ├── dt_model.pkl               # Decision Tree
│   └── rf_model.pkl               # Random Forest
│
└── notebooks/                      # Jupyter notebooks
    └── final_Stock_git_ready_copy.ipynb
```

## 🔧 Configuration

Edit `config.py` to customize:
- Data file paths
- Model paths
- Dash host and port
- Debug mode
- Application title

## 📚 Data Requirements

The application expects the following CSV files in the `data/` directory:
- `combined_data.csv` - Main dataset with market data
- `train_df.csv` - Training data for models
- `test_df.csv` - Testing data for models
- `web_scrape.csv` - Web scraped sentiment data

## 🤖 Machine Learning Models

All models are trained on 2.5 years of historical data:

| Model | AUC Score | Accuracy | Precision | Recall |
|-------|-----------|----------|-----------|--------|
| Binary Logistic Regression | 0.7051 | 0.67 | - | - |
| Gaussian Naive Bayes | 0.7033 | - | - | - |
| Decision Tree | 0.6198 | 0.65 | - | - |
| Random Forest | 0.6452 | 0.64 | - | - |

## 💬 Sentiment Analysis

Two sentiment analysis approaches:
1. **VADER** - Lexicon-based sentiment analysis
2. **FinBERT** - BERT-based financial sentiment model

## 🌐 Global Indices

Analyzed indices:
- NSE (National Stock Exchange)
- DJI (Dow Jones Industrial Average)
- IXIC (NASDAQ)
- HSI (Hang Seng Index)
- N225 (Nikkei 225)
- GDAXI (DAX)
- VIX (Volatility Index)

## 📝 Technical Stack

- **Frontend:** Dash, Plotly
- **Backend:** Python, Flask (Dash is built on Flask)
- **ML:** scikit-learn, statsmodels
- **NLP:** VADER, FinBERT, NLTK
- **Visualization:** Wordcloud, Matplotlib
- **Deployment:** Render, Gunicorn

## 🔐 Security Notes

- Ensure sensitive data is not committed to version control
- Use environment variables for sensitive configuration
- Keep dependencies updated

## 📞 Support

For issues and questions, please create an issue on GitHub.

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Dash team for the excellent framework
- Plotly for interactive visualizations
- scikit-learn for ML models
- Hugging Face for FinBERT model
