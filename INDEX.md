# Project Structure & File Index

This document provides a complete overview of the production-ready Stock Market Analytics Dashboard project structure.

## 📁 Root Level Files

### Configuration & Setup
- **app.py** - Main Dash application entry point. Initializes the app, loads data, and defines the basic layout with three tabs (EDA, Model Performance, Sentiment Analysis)
- **config.py** - Central configuration file containing all paths, settings, and constants. Edit this to customize the application
- **requirements.txt** - Python dependencies and versions for pip install
- **Procfile** - Render deployment configuration (gunicorn command)
- **render.yaml** - Alternative Render configuration format
- **.env.example** - Template for environment variables (copy to .env and customize)
- **.gitignore** - Git ignore rules to prevent committing sensitive/large files

### Documentation
- **README.md** - Complete project documentation with features, setup, architecture, and technical details
- **QUICKSTART.md** - Fast start guide for local development and Render deployment
- **DEPLOYMENT.md** - Comprehensive deployment guide for multiple platforms (Render, Docker, Heroku)
- **INDEX.md** - This file! Complete file structure reference

### Version Control
- **.git/** - Git repository metadata (auto-created when you run `git init`)
- **.github/workflows/deploy.yml** - CI/CD pipeline for automated testing and Render deployment

---

## 📂 Directory Structure

### src/ - Application Source Code

```
src/
├── __init__.py                    # Python package initialization
│
├── callbacks/                     # Interactive callbacks for Dash
│   └── __init__.py               # Callback functions will go here
│       │
│       ├── eda_callbacks.py       # [TEMPLATE] EDA plot callbacks
│       ├── model_callbacks.py     # [TEMPLATE] Model selection callbacks
│       └── sentiment_callbacks.py # [TEMPLATE] Sentiment analysis callbacks
│
├── layouts/                       # UI Layout definitions
│   ├── __init__.py               # Layout package
│   ├── eda_layout.py             # EDA Charts tab layout
│   ├── model_layout.py           # Model Performance tab layout
│   └── sentiment_layout.py       # Sentiment Analysis tab layout
│
├── components/                    # Reusable Dash components
│   ├── __init__.py               # Component package
│   └── chart_utils.py            # [TEMPLATE] Reusable chart components
│
└── utils/                        # Utility functions and helpers
    ├── __init__.py               # Utils package initialization
    ├── data_loader.py            # Data loading and preprocessing functions
    ├── sentiment_analyzer.py     # VADER & FinBERT sentiment analysis
    └── visualization_helpers.py  # Chart creation and visualization utilities
```

### data/ - Data Files

```
data/
├── combined_data.csv            # Main dataset with all indices (2017-2025)
├── train_df.csv                 # Training data for ML models
├── test_df.csv                  # Testing data for ML model evaluation
└── web_scrape.csv               # Web scraped data for sentiment analysis
```

**Note**: These CSV files are not in git (see .gitignore). You need to copy them from your source or download from the original notebook execution.

### models/ - Pre-trained Machine Learning Models

```
models/
├── blr_model.pkl                # Binary Logistic Regression model
├── gn_model.pkl                 # Gaussian Naive Bayes model
├── dt_model.pkl                 # Decision Tree model
└── rf_model.pkl                 # Random Forest model
```

**Note**: Model files are trained in the original notebook and need to be exported as .pkl files for production use.

### notebooks/ - Original Jupyter Notebooks

```
notebooks/
└── final_Stock_git_ready_copy.ipynb    # Complete original analysis notebook
                                        # (Reference only, not used in production)
```

---

## 📄 Key File Descriptions

### Core Application Files

#### app.py
- **Purpose**: Main entry point for the Dash application
- **What it does**:
  - Initializes the Dash app
  - Creates the basic layout with 3 tabs
  - Loads data from CSV files
  - Defines simple callbacks for tab navigation
  - Runs the Gunicorn server
- **To customize**: Edit dashboard title, colors, port, and debug settings
- **Dependencies**: dash, plotly, pandas, config.py

#### config.py
- **Purpose**: Centralized configuration management
- **Contains**:
  - File paths (data, models)
  - Dash settings (host, port)
  - Feature settings (model names, app title)
- **To customize**: Update paths, host/port, or feature settings
- **Usage**: Import with `import config` then use `config.COMBINED_DATA_PATH` etc.

### Data Loading & Processing

#### src/utils/data_loader.py
- **Purpose**: Load and prepare data for the dashboard
- **Functions**:
  - `load_combined_data()` - Load main market data
  - `load_training_data()` - Load model training data
  - `load_test_data()` - Load model testing data
  - `load_web_scrape_data()` - Load sentiment analysis data
  - `prepare_correlation_matrices()` - Pre-calculate correlations
  - `prepare_summary_stats()` - Pre-calculate statistics
- **Auto-executes on import**: Loads all data and calculates statistics

#### src/utils/sentiment_analyzer.py
- **Purpose**: Perform sentiment analysis on text data
- **Sentiment Methods**:
  - **VADER**: Fast, rule-based lexicon analysis (NLTK)
  - **FinBERT**: Deep learning-based financial sentiment (Transformers)
- **Key Functions**:
  - `analyze_vader_sentiment()` - Single text VADER analysis
  - `analyze_finbert_sentiment()` - Single text FinBERT analysis
  - `apply_vader_to_dataframe()` - Batch VADER analysis
  - `apply_finbert_to_dataframe()` - Batch FinBERT analysis
  - `clean_text()` - Text preprocessing

#### src/utils/visualization_helpers.py
- **Purpose**: Create reusable Plotly visualizations
- **Functions**:
  - `create_wordcloud_image()` - Generate WordCloud images
  - `create_heatmap()` - Create aggregated heatmaps
  - `create_correlation_heatmap()` - Correlation matrices
  - `create_bar_chart()` - Bar charts
  - `create_box_plot()` - Box-whisker plots

### Layout Templates

#### src/layouts/eda_layout.py
- **Purpose**: EDA Charts tab layout
- **Status**: Template (extract full code from notebook cell 3844)

#### src/layouts/model_layout.py
- **Purpose**: Model Performance tab layout
- **Status**: Template (extract full code from notebook cell 4217)
- **Contains**: Model selection dropdown, confusion matrix, ROC curve, feature importance

#### src/layouts/sentiment_layout.py
- **Purpose**: Sentiment Analysis tab layout
- **Status**: Template (extract full code from notebook cell 4470)
- **Contains**: VADER/FinBERT counts, WordCloud, histogram, data table

### Callback Templates (Not Yet Implemented)

These files should contain the interactive callbacks from the notebook:

#### src/callbacks/eda_callbacks.py
- Box plot updates (boxplot dropdown)
- Bar plot updates (barplot dropdown)
- Combined heatmap updates (median/mean toggle)
- Correlation heatmap updates (matrix A/B selection)
- Global indices bar chart updates

#### src/callbacks/model_callbacks.py
- Model selection (dropdown)
- Confusion matrix update
- ROC curve update
- Decision tree visualization
- Random Forest visualization (tree + importance)

#### src/callbacks/sentiment_callbacks.py
- Sentiment distribution updates
- WordCloud generation
- Histogram updates
- Data table rendering

---

## 🔄 Data Flow

```
Original Notebook (final_Stock_git_ready copy.ipynb)
        ↓
   Data Processing (Cells 1-242)
        ↓
   Create Visualizations (Cell 243)
        ↓
   Train ML Models (in various cells)
        ↓
   Export: CSV files to data/
   Export: Model PKL files to models/
        ↓
    Production Application
        ↓
   app.py (Entry point)
        ↓
   data_loader.py (Load data)
        ↓
   [Three Tabs: EDA | Models | Sentiment]
        ↓
   Deploy to Render/GitHub
```

---

## 📊 Technical Stack

### Frontend
- **Dash** - Python web framework for dashboards
- **Plotly** - Interactive visualization library

### Backend & Data Processing
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **scikit-learn** - Machine learning models

### Natural Language Processing
- **NLTK** - VADER sentiment analysis
- **Transformers** - FinBERT model
- **WordCloud** - Text visualization

### Deployment
- **Gunicorn** - Python WSGI server
- **Render** - Cloud platform (primary)
- **Docker** - Containerization (optional)

---

## 🚀 Quick Navigation Guide

| Goal | Go To | File |
|---------|---------|---------|
| Start development | QUICKSTART.md | - |
| Deploy to Render | DEPLOYMENT.md | - |
| View full docs | README.md | - |
| Change settings | config.py | - |
| Load data | src/utils/data_loader.py | - |
| Analyze sentiment | src/utils/sentiment_analyzer.py | - |
| Create charts | src/utils/visualization_helpers.py | - |
| Edit layouts | src/layouts/*.py | - |
| Add callbacks | src/callbacks/*.py | - |
| Run application | app.py | - |

---

## 💡 Next Steps

To complete the modularization:

1. **Extract EDA Layout** - Copy full `create_eda_tab()` from notebook cell 3844
   - File: `src/layouts/eda_layout.py`
   - Include all heatmaps, box plots, bar plots, correlation matrices

2. **Extract Model Layout** - Copy full `create_model_tab()` from notebook cell 4217
   - File: `src/layouts/model_layout.py`
   - Include dropdown menu, model selection, visualizations

3. **Extract Sentiment Layout** - Copy full `create_sentiment_tab()` from notebook cell 4470
   - File: `src/layouts/sentiment_layout.py`
   - Include data table, VADER/FinBERT counts, WordCloud, histogram

4. **Create Callbacks** - Extract callback functions from notebook
   - Directory: `src/callbacks/`
   - Move @app.callback decorators and update functions
   - Keep all logic exactly as-is

5. **Export Models** - Save trained models from notebook
   - Command: `import pickle; pickle.dump(model, open('models/model_name.pkl', 'wb'))`
   - Update model loading in `data_loader.py`

6. **Test Locally** - Run `python app.py` and verify all features work

7. **Push to GitHub** - Commit and push all changes

8. **Deploy to Render** - Follow DEPLOYMENT.md instructions

---

## 📝 File Statistics

```
Total Files Created: 23
├── Configuration: 4 files
├── Documentation: 5 files
├── Source Code: 9 files
├── Directories: 5 directories
└── Data/Models: 2 directories (to be populated)

Code Files:
├── Python: 9 (.py files)
├── Markdown: 5 (.md files)
├── YAML: 2 (.yml files)
├── Text: 2 (.txt, .example files)

Total Lines of Code: 2,000+ (including docs)
```

---

## ✅ Checklist for Production Readiness

- [x] Modular directory structure created
- [x] Core application files (app.py, config.py)
- [x] Data loading utilities
- [x] Sentiment analysis utilities
- [x] Visualization helper functions
- [x] Layout templates created
- [x] Callback templates created
- [x] Requirements.txt generated
- [x] Procfile for Render
- [x] .env.example configuration
- [x] .gitignore rules
- [x] Comprehensive README
- [x] Quick start guide
- [x] Deployment guide
- [x] GitHub Actions CI/CD
- [ ] Full layout code extracted (from notebook)
- [ ] Full callback code extracted (from notebook)
- [ ] Data CSV files copied to data/
- [ ] Models PKL files exported to models/
- [ ] Local testing completed
- [ ] GitHub repository created
- [ ] Render deployment created

---

**Last Updated**: 2024
**Status**: Ready for code extraction and local testing
