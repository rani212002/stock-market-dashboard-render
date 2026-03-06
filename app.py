#!/usr/bin/env python3
"""
Stock Market Analytics Dashboard - Main Application Entry Point
"""

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import Dash and components
import dash
from dash import dcc, html
import plotly.graph_objects as go

# Create Dash app
dash_app = dash.Dash(__name__)

# Configure app properties
dash_app.title = "📈 Stock Market Analytics Dashboard"
server = dash_app.server  # Flask WSGI app for Gunicorn


def wsgi_app(environ, start_response):
    """Explicit WSGI callable for Gunicorn on Render."""
    return server(environ, start_response)

# Import layouts after app is created
# NOTE: Full layouts are extracted from notebook cells
# The following imports assume modularized layout files

import config

# ============================================================================
# TEMPORARY: Full app definition for initial deployment
# This will be refactored into separate layout/callback modules
# ============================================================================

# Load data
try:
    import pandas as pd
    if config.COMBINED_DATA_PATH.exists():
        combined_data = pd.read_csv(config.COMBINED_DATA_PATH)
        if 'Year' not in combined_data.columns:
            combined_data['Year'] = pd.to_datetime(combined_data.index).year
        if 'Quarter' not in combined_data.columns:
            combined_data['Quarter'] = pd.to_datetime(combined_data.index).quarter.map({1:'Q1', 2:'Q2', 3:'Q3', 4:'Q4'})
    else:
        print(f"⚠️ Data file not found at {config.COMBINED_DATA_PATH}")
        combined_data = pd.DataFrame()
except Exception as e:
    print(f"⚠️ Warning loading combined_data: {e}")
    combined_data = pd.DataFrame()

# ============================================================================
# APP LAYOUT - Basic Structure
# ============================================================================
dash_app.layout = html.Div([
    html.Div([
        html.H1("📈 Stock Market Analytics Dashboard", style={
            'textAlign': 'center', 
            'marginBottom': 10, 
            'color': '#2c3e50'
        }),
        html.P("Comprehensive analysis of 2.5 year global markets data with 4 ML models", style={
            'textAlign': 'center', 
            'color': '#7f8c8d', 
            'marginBottom': 0
        }),
        html.Hr()
    ], style={
        'padding': '20px', 
        'backgroundColor': '#ecf0f1', 
        'marginBottom': 30, 
        'borderRadius': '8px'
    }),
    
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(
            label='📊 EDA Charts',
            value='tab-1',
            children=[html.Div(id='eda-content', children=[
                html.P("Loading EDA Charts...", style={'textAlign': 'center', 'padding': '20px'})
            ], style={'padding': '20px'})],
            style={'padding': '15px', 'fontWeight': 'bold'},
            selected_style={'borderTop': '3px solid #3498db', 'backgroundColor': '#ecf0f1'}
        ),
        dcc.Tab(
            label='🎯 Model Performance',
            value='tab-2',
            children=[html.Div(id='model-content', children=[
                html.P("Loading Model Performance...", style={'textAlign': 'center', 'padding': '20px'})
            ], style={'padding': '20px'})],
            style={'padding': '15px', 'fontWeight': 'bold'},
            selected_style={'borderTop': '3px solid #3498db', 'backgroundColor': '#ecf0f1'}
        ),
        dcc.Tab(
            label='💬 Sentiment Analysis',
            value='tab-3',
            children=[html.Div(id='sentiment-content', children=[
                html.P("Loading Sentiment Analysis...", style={'textAlign': 'center', 'padding': '20px'})
            ], style={'padding': '20px'})],
            style={'padding': '15px', 'fontWeight': 'bold'},
            selected_style={'borderTop': '3px solid #3498db', 'backgroundColor': '#ecf0f1'}
        )
    ], style={'fontFamily': 'Arial', 'fontSize': 16})
], style={'padding': '20px', 'fontFamily': 'Arial', 'backgroundColor': '#f8f9fa', 'minHeight': '100vh'})

# ============================================================================
# SIMPLE CALLBACK FOR INITIAL TESTING
# ============================================================================
@dash_app.callback(
    dash.dependencies.Output('eda-content', 'children'),
    dash.dependencies.Input('tabs', 'value')
)
def display_eda(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H2("Exploratory Data Analysis (EDA) Charts", style={'textAlign': 'center'}),
            html.P("✅ Dashboard loaded successfully!", style={'textAlign': 'center', 'fontSize': 18, 'color': 'green'}),
            html.P(f"Data shape: {combined_data.shape[0]} rows", style={'textAlign': 'center'}) if not combined_data.empty else html.P("Loading data...", style={'textAlign': 'center'})
        ], style={'padding': '20px'})
    return html.P("Select EDA Charts tab", style={'textAlign': 'center', 'padding': '20px'})

@dash_app.callback(
    dash.dependencies.Output('model-content', 'children'),
    dash.dependencies.Input('tabs', 'value')
)
def display_models(tab):
    if tab == 'tab-2':
        return html.Div([
            html.H2("Model Performance", style={'textAlign': 'center'}),
            html.P("4 Machine Learning Models Available:", style={'textAlign': 'center', 'fontSize': 14}),
            html.Ul([
                html.Li("Binary Logistic Regression (AUC: 0.7051)", style={'fontSize': 14}),
                html.Li("Gaussian Naive Bayes (AUC: 0.7033)", style={'fontSize': 14}),
                html.Li("Decision Tree (AUC: 0.6198)", style={'fontSize': 14}),
                html.Li("Random Forest (AUC: 0.6452)", style={'fontSize': 14}),
            ], style={'textAlign': 'center', 'maxWidth': '400px', 'margin': '0 auto'})
        ], style={'padding': '20px'})
    return html.P("Select Model Performance tab", style={'textAlign': 'center', 'padding': '20px'})

@dash_app.callback(
    dash.dependencies.Output('sentiment-content', 'children'),
    dash.dependencies.Input('tabs', 'value')
)
def display_sentiment(tab):
    if tab == 'tab-3':
        return html.Div([
            html.H2("Sentiment Analysis", style={'textAlign': 'center'}),
            html.P("Sentiment Analysis Methods:", style={'textAlign': 'center', 'fontSize': 14}),
            html.Ul([
                html.Li("VADER Sentiment Analysis", style={'fontSize': 14}),
                html.Li("FinBERT Sentiment Analysis", style={'fontSize': 14}),
                html.Li("Web Scrape Data Integration", style={'fontSize': 14}),
                html.Li("WordCloud Visualization", style={'fontSize': 14}),
            ], style={'textAlign': 'center', 'maxWidth': '400px', 'margin': '0 auto'})
        ], style={'padding': '20px'})
    return html.P("Select Sentiment Analysis tab", style={'textAlign': 'center', 'padding': '20px'})

# ============================================================================
# RUN APPLICATION
# ============================================================================
# Expose conventional WSGI names so both `gunicorn app:app` and
# `gunicorn wsgi:application` work on hosting platforms.
application = server
app = application


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 Stock Market Analytics Dashboard Starting...")
    print("="*70)
    print(f"📊 Configuration loaded from: {config.__file__}")
    print(f"📁 Data directory: {config.DATA_DIR}")
    print(f"🤖 Models directory: {config.MODEL_DIR}")
    print(f"🌐 Access at: http://{config.DASH_HOST}:{config.DASH_PORT}")
    print("="*70 + "\n")
    
    dash_app.run_server(
        debug=config.DEBUG_MODE,
        host=config.DASH_HOST,
        port=config.DASH_PORT
    )
