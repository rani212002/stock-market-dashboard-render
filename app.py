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
import plotly.express as px
import pandas as pd

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

try:
    train_df = pd.read_csv(config.TRAIN_DATA_PATH) if config.TRAIN_DATA_PATH.exists() else pd.DataFrame()
except Exception as e:
    print(f"⚠️ Warning loading train_df: {e}")
    train_df = pd.DataFrame()

try:
    test_df = pd.read_csv(config.TEST_DATA_PATH) if config.TEST_DATA_PATH.exists() else pd.DataFrame()
except Exception as e:
    print(f"⚠️ Warning loading test_df: {e}")
    test_df = pd.DataFrame()

try:
    web_scrape_df = pd.read_csv(config.WEB_SCRAPE_PATH) if config.WEB_SCRAPE_PATH.exists() else pd.DataFrame()
except Exception as e:
    print(f"⚠️ Warning loading web_scrape: {e}")
    web_scrape_df = pd.DataFrame()

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
        if combined_data.empty:
            return html.Div([
                html.H2("Exploratory Data Analysis (EDA) Charts", style={'textAlign': 'center'}),
                html.P("No combined_data.csv found in data/", style={'textAlign': 'center', 'color': 'crimson'})
            ], style={'padding': '20px'})

        return_cols = [
            col for col in [
                'NSE_Return', 'DJI_Return', 'IXIC_Return', 'HSI_Return',
                'N225_Return', 'GDAXI_Return', 'VIX_Return'
            ] if col in combined_data.columns
        ]

        fig_returns = go.Figure()
        for col in return_cols[:4]:
            fig_returns.add_trace(go.Scatter(
                x=combined_data.index,
                y=combined_data[col],
                mode='lines',
                name=col.replace('_Return', '')
            ))
        fig_returns.update_layout(
            title='Market Returns Trend (Top 4 Indices)',
            xaxis_title='Index',
            yaxis_title='Return',
            template='plotly_white',
            height=420
        )

        box_col = return_cols[0] if return_cols else None
        fig_box = px.box(combined_data, y=box_col, title=f'Distribution: {box_col}') if box_col else go.Figure()
        fig_box.update_layout(template='plotly_white', height=420)

        return html.Div([
            html.H2("Exploratory Data Analysis (EDA) Charts", style={'textAlign': 'center'}),
            html.P(
                f"Rows: {combined_data.shape[0]} | Columns: {combined_data.shape[1]}",
                style={'textAlign': 'center', 'marginBottom': '14px'}
            ),
            dcc.Graph(figure=fig_returns),
            dcc.Graph(figure=fig_box)
        ], style={'padding': '20px'})
    return html.P("Select EDA Charts tab", style={'textAlign': 'center', 'padding': '20px'})

@dash_app.callback(
    dash.dependencies.Output('model-content', 'children'),
    dash.dependencies.Input('tabs', 'value')
)
def display_models(tab):
    if tab == 'tab-2':
        target_candidates = ['Target', 'target', 'label', 'Label', 'y']
        target_col = next((c for c in target_candidates if c in train_df.columns), None)

        if target_col:
            class_counts = train_df[target_col].value_counts().sort_index().reset_index()
            class_counts.columns = ['class', 'count']
            fig_target = px.bar(
                class_counts,
                x='class',
                y='count',
                title=f'Train Target Distribution ({target_col})',
                template='plotly_white'
            )
        else:
            fig_target = go.Figure()
            fig_target.update_layout(
                title='Target Distribution unavailable (target column not found)',
                template='plotly_white',
                height=380
            )

        return html.Div([
            html.H2("Model Performance", style={'textAlign': 'center'}),
            html.P(
                f"Train rows: {train_df.shape[0]} | Test rows: {test_df.shape[0]}",
                style={'textAlign': 'center', 'fontSize': 14}
            ),
            html.Ul([
                html.Li("Binary Logistic Regression (AUC: 0.7051)", style={'fontSize': 14}),
                html.Li("Gaussian Naive Bayes (AUC: 0.7033)", style={'fontSize': 14}),
                html.Li("Decision Tree (AUC: 0.6198)", style={'fontSize': 14}),
                html.Li("Random Forest (AUC: 0.6452)", style={'fontSize': 14}),
            ], style={'textAlign': 'center', 'maxWidth': '400px', 'margin': '0 auto'})
            ,
            dcc.Graph(figure=fig_target)
        ], style={'padding': '20px'})
    return html.P("Select Model Performance tab", style={'textAlign': 'center', 'padding': '20px'})

@dash_app.callback(
    dash.dependencies.Output('sentiment-content', 'children'),
    dash.dependencies.Input('tabs', 'value')
)
def display_sentiment(tab):
    if tab == 'tab-3':
        sentiment_col = next((c for c in ['Sentiment', 'sentiment', 'vader_sentiment', 'finbert_sentiment'] if c in web_scrape_df.columns), None)

        if sentiment_col:
            sent_counts = web_scrape_df[sentiment_col].astype(str).value_counts().reset_index()
            sent_counts.columns = ['sentiment', 'count']
            fig_sent = px.pie(
                sent_counts,
                names='sentiment',
                values='count',
                title=f'Sentiment Breakdown ({sentiment_col})'
            )
            fig_sent.update_layout(template='plotly_white', height=420)
        else:
            fig_sent = go.Figure()
            fig_sent.update_layout(
                title='Sentiment chart unavailable (sentiment column not found)',
                template='plotly_white',
                height=420
            )

        return html.Div([
            html.H2("Sentiment Analysis", style={'textAlign': 'center'}),
            html.P(
                f"Web-scrape rows: {web_scrape_df.shape[0]}",
                style={'textAlign': 'center', 'fontSize': 14}
            ),
            html.Ul([
                html.Li("VADER Sentiment Analysis", style={'fontSize': 14}),
                html.Li("FinBERT Sentiment Analysis", style={'fontSize': 14}),
                html.Li("Web Scrape Data Integration", style={'fontSize': 14}),
                html.Li("WordCloud Visualization", style={'fontSize': 14}),
            ], style={'textAlign': 'center', 'maxWidth': '400px', 'margin': '0 auto'})
            ,
            dcc.Graph(figure=fig_sent)
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
