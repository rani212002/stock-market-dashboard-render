"""
Sentiment analysis utilities using VADER and FinBERT
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re
import os

try:
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    # Download VADER lexicon if needed
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        print("📥 Downloading VADER lexicon...")
        nltk.download('vader_lexicon')
except ImportError:
    print("⚠️ NLTK not available - VADER sentiment will be skipped")

try:
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch
    FINBERT_AVAILABLE = True
except ImportError:
    print("⚠️ Transformers not available - FinBERT sentiment will be skipped")
    FINBERT_AVAILABLE = False

# ============================================================================
# VADER SENTIMENT ANALYSIS
# ============================================================================

def analyze_vader_sentiment(text):
    """
    Analyze sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner)
    
    Args:
        text (str): Text to analyze
    
    Returns:
        dict: Sentiment scores and label
    """
    try:
        sia = SentimentIntensityAnalyzer()
        
        if not isinstance(text, str) or text.strip() == "":
            return {
                'neg': 0.0,
                'neu': 0.0,
                'pos': 0.0,
                'compound': 0.0,
                'label': 'neutral'
            }
        
        scores = sia.polarity_scores(text)
        
        # Determine label based on compound score
        compound = scores['compound']
        if compound >= 0.05:
            label = 'positive'
        elif compound <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        
        return {
            'neg': scores['neg'],
            'neu': scores['neu'],
            'pos': scores['pos'],
            'compound': scores['compound'],
            'label': label
        }
    except Exception as e:
        print(f"⚠️ Error in VADER analysis: {e}")
        return {
            'neg': 0.0,
            'neu': 0.0,
            'pos': 0.0,
            'compound': 0.0,
            'label': 'unknown'
        }

def apply_vader_to_dataframe(df, text_column='clean_text'):
    """
    Apply VADER sentiment analysis to a DataFrame column
    
    Args:
        df (pd.DataFrame): Input dataframe
        text_column (str): Column name containing text to analyze
    
    Returns:
        pd.DataFrame: DataFrame with added sentiment columns
    """
    try:
        df_copy = df.copy()
        
        # Apply VADER analysis
        vader_results = df_copy[text_column].apply(analyze_vader_sentiment).apply(pd.Series)
        
        # Add results to dataframe
        df_copy['vader_neg'] = vader_results['neg']
        df_copy['vader_neu'] = vader_results['neu']
        df_copy['vader_pos'] = vader_results['pos']
        df_copy['vader_compound'] = vader_results['compound']
        df_copy['vader_sentiment_label'] = vader_results['label']
        
        print(f"✅ VADER sentiment analysis completed for {len(df_copy)} rows")
        return df_copy
    except Exception as e:
        print(f"❌ Error applying VADER to DataFrame: {e}")
        return df

# ============================================================================
# FINBERT SENTIMENT ANALYSIS
# ============================================================================

def analyze_finbert_sentiment(text):
    """
    Analyze sentiment using FinBERT (Financial BERT)
    
    Args:
        text (str): Text to analyze
    
    Returns:
        dict: Sentiment scores and label
    """
    if not FINBERT_AVAILABLE:
        return {'label': 'unknown', 'scores': {}}
    
    try:
        tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
        model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
        
        if not isinstance(text, str) or len(text.strip()) == 0:
            return {
                'label': 'neutral',
                'negative': 0.0,
                'neutral': 1.0,
                'positive': 0.0
            }
        
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        logits = outputs.logits
        softmax_output = torch.softmax(logits, dim=1).tolist()[0]
        
        # FinBERT output order: {'negative': 0, 'neutral': 1, 'positive': 2}
        sentiment_scores = {
            'negative': softmax_output[0],
            'neutral': softmax_output[1],
            'positive': softmax_output[2]
        }
        
        # Determine label based on highest score
        max_sentiment = max(sentiment_scores, key=sentiment_scores.get)
        
        return {
            'label': max_sentiment,
            'negative': sentiment_scores['negative'],
            'neutral': sentiment_scores['neutral'],
            'positive': sentiment_scores['positive']
        }
    except Exception as e:
        print(f"⚠️ Error in FinBERT analysis: {e}")
        return {
            'label': 'unknown',
            'negative': 0.0,
            'neutral': 0.0,
            'positive': 0.0
        }

def apply_finbert_to_dataframe(df, text_column='raw_text'):
    """
    Apply FinBERT sentiment analysis to a DataFrame column
    
    Args:
        df (pd.DataFrame): Input dataframe
        text_column (str): Column name containing text to analyze
    
    Returns:
        pd.DataFrame: DataFrame with added sentiment columns
    """
    if not FINBERT_AVAILABLE:
        print("⚠️ FinBERT not available - skipping FinBERT analysis")
        return df
    
    try:
        df_copy = df.copy()
        
        # Apply FinBERT analysis
        finbert_results = df_copy[text_column].apply(analyze_finbert_sentiment).apply(pd.Series)
        
        # Add results to dataframe
        df_copy['finbert_sentiment_label'] = finbert_results['label']
        df_copy['finbert_negative'] = finbert_results['negative']
        df_copy['finbert_neutral'] = finbert_results['neutral']
        df_copy['finbert_positive'] = finbert_results['positive']
        
        print(f"✅ FinBERT sentiment analysis completed for {len(df_copy)} rows")
        return df_copy
    except Exception as e:
        print(f"❌ Error applying FinBERT to DataFrame: {e}")
        return df

# ============================================================================
# SENTIMENT ANALYSIS UTILITIES
# ============================================================================

def clean_text(text):
    """
    Clean and preprocess text for sentiment analysis
    
    Args:
        text (str): Raw text
    
    Returns:
        str: Cleaned text
    """
    if not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove special characters and extra whitespace
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text.lower()

def get_sentiment_distribution(df, sentiment_column):
    """
    Get sentiment label distribution
    
    Args:
        df (pd.DataFrame): Input dataframe
        sentiment_column (str): Column name with sentiment labels
    
    Returns:
        pd.Series: Value counts of sentiment labels
    """
    return df[sentiment_column].value_counts(dropna=False)

print("✅ Sentiment analysis utilities loaded successfully")
