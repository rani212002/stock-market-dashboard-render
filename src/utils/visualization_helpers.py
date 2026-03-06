"""
Visualization helper functions for creating charts
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from PIL import Image
import io
import base64
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_wordcloud_image(text_data, max_words=200):
    """
    Create a WordCloud visualization from text data
    
    Args:
        text_data (str or list): Text or list of texts to analyze
        max_words (int): Maximum number of words to display
    
    Returns:
        str: Base64 encoded image
    """
    try:
        if isinstance(text_data, list):
            text_data = ' '.join(str(t) for t in text_data)
        
        if not text_data or len(text_data.strip()) == 0:
            return None
        
        # Create WordCloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis',
            max_words=max_words
        ).generate(text_data)
        
        # Convert to image
        img_buffer = io.BytesIO()
        wordcloud.to_image().save(img_buffer, format='PNG')
        img_buffer.seek(0)
        img_b64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        
        return f'data:image/png;base64,{img_b64}'
    except Exception as e:
        print(f"⚠️ Error creating WordCloud: {e}")
        return None

def create_heatmap(df, value_col, agg='median', title=None):
    """
    Create a heatmap for a single metric
    
    Args:
        df (pd.DataFrame): Input dataframe
        value_col (str): Column to aggregate
        agg (str): Aggregation method ('median' or 'mean')
        title (str): Chart title
    
    Returns:
        go.Figure: Plotly figure
    """
    try:
        if agg == 'median':
            pivot = df.pivot_table(index='Year', columns='Quarter', values=value_col, aggfunc='median')
            title = title or f"Median {value_col}"
        else:
            pivot = df.pivot_table(index='Year', columns='Quarter', values=value_col, aggfunc='mean')
            title = title or f"Mean {value_col}"
        
        z = pivot.to_numpy()
        text = np.where(np.isfinite(z), np.round(z, 2).astype(str), "")
        
        fig = go.Figure(
            data=go.Heatmap(
                z=z,
                x=pivot.columns.astype(str),
                y=pivot.index.astype(str),
                colorscale="RdBu",
                zmid=0,
                text=text,
                texttemplate="%{text}",
                hovertemplate="Year=%{y}<br>Quarter=%{x}<br>Value=%{z:.4f}<extra></extra>",
                colorbar=dict(title="Value"),
            )
        )
        
        fig.update_layout(
            title=title,
            xaxis_title="Quarter",
            yaxis_title="Year",
            height=520,
            margin=dict(l=60, r=30, t=70, b=60)
        )
        
        return fig
    except Exception as e:
        print(f"⚠️ Error creating heatmap: {e}")
        return go.Figure()

def create_correlation_heatmap(corr_df, title="Correlation Matrix"):
    """
    Create correlation matrix heatmap
    
    Args:
        corr_df (pd.DataFrame): Correlation matrix
        title (str): Chart title
    
    Returns:
        go.Figure: Plotly figure
    """
    try:
        z = corr_df.to_numpy()
        labels = corr_df.columns.tolist()
        text = np.round(z, 2).astype(str)
        
        fig = go.Figure(
            data=go.Heatmap(
                z=z,
                x=labels,
                y=labels,
                colorscale="RdBu",
                zmin=-1,
                zmax=1,
                zmid=0,
                text=text,
                texttemplate="%{text}",
                hovertemplate="X=%{x}<br>Y=%{y}<br>Corr=%{z:.4f}<extra></extra>",
                colorbar=dict(title="Corr"),
            )
        )
        
        fig.update_layout(
            title=title,
            xaxis_title="Index",
            yaxis_title="Index",
            height=520,
            margin=dict(l=70, r=30, t=70, b=70),
        )
        
        return fig
    except Exception as e:
        print(f"⚠️ Error creating correlation heatmap: {e}")
        return go.Figure()

def create_bar_chart(df, x_col, y_col, color_col=None, title=None, **kwargs):
    """
    Create a bar chart
    
    Args:
        df (pd.DataFrame): Input dataframe
        x_col (str): X-axis column
        y_col (str): Y-axis column
        color_col (str): Optional color column
        title (str): Chart title
    
    Returns:
        go.Figure: Plotly figure
    """
    try:
        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            color=color_col,
            title=title or f"{y_col} by {x_col}",
            **kwargs
        )
        return fig
    except Exception as e:
        print(f"⚠️ Error creating bar chart: {e}")
        return go.Figure()

def create_box_plot(df, x_col, y_col, title=None):
    """
    Create a box plot
    
    Args:
        df (pd.DataFrame): Input dataframe
        x_col (str): X-axis column (grouping)
        y_col (str): Y-axis column (values)
        title (str): Chart title
    
    Returns:
        go.Figure: Plotly figure
    """
    try:
        fig = px.box(
            df,
            x=x_col,
            y=y_col,
            points='outliers',
            title=title or f"Distribution of {y_col} by {x_col}"
        )
        fig.update_layout(
            height=500,
            template='plotly_white',
            xaxis_title=x_col,
            yaxis_title=y_col
        )
        return fig
    except Exception as e:
        print(f"⚠️ Error creating box plot: {e}")
        return go.Figure()

print("✅ Visualization utilities loaded successfully")
