"""
Sentiment Analysis layout components
NOTE: This file is a template. The actual layout from the notebook
should be extracted and modularized here.
"""

from dash import dcc, html, dash_table as dt
import plotly.graph_objects as go

def create_sentiment_tab():
    """Create Sentiment Analysis tab layout"""
    return html.Div([
        html.H2("Sentiment Analysis Charts", 
                style={'textAlign': 'center', 'marginBottom': 30}),
        
        html.Div([
            html.Div([
                html.H4("Sentiment Analysis Methods:", style={'textAlign': 'center'}),
                html.Ul([
                    html.Li("📊 VADER Sentiment Analysis", style={'fontSize': 14}),
                    html.Li("🤖 FinBERT Sentiment Analysis", style={'fontSize': 14}),
                    html.Li("☁️ WordCloud Visualization", style={'fontSize': 14}),
                    html.Li("📈 Web Scrape Data Integration", style={'fontSize': 14}),
                ], style={'maxWidth': '500px', 'margin': '0 auto'})
            ], style={'padding': '20px', 'backgroundColor': '#f8f9fa', 
                      'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
        ])
    ])
