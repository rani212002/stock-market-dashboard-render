"""
Model Performance layout components
NOTE: This file is a template. The actual layout from the notebook
should be extracted and modularized here.
"""

from dash import dcc, html
import plotly.graph_objects as go

def create_model_tab():
    """Create Model Performance tab layout"""
    return html.Div([
        html.H2("Model Performance", 
                style={'textAlign': 'center', 'marginBottom': 30}),
        
        html.Div([
            html.Div([
                html.H4("Available Models:", style={'textAlign': 'center'}),
                html.Ul([
                    html.Li("📊 Binary Logistic Regression (AUC: 0.7051)", style={'fontSize': 14}),
                    html.Li("📊 Gaussian Naive Bayes (AUC: 0.7033)", style={'fontSize': 14}),
                    html.Li("🌳 Decision Tree (AUC: 0.6198)", style={'fontSize': 14}),
                    html.Li("🌲 Random Forest (AUC: 0.6452)", style={'fontSize': 14}),
                ], style={'maxWidth': '500px', 'margin': '0 auto'})
            ], style={'padding': '20px', 'backgroundColor': '#f8f9fa', 
                      'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
        ])
    ])
