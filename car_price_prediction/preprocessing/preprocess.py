import pandas as pd
import numpy as np

def preprocess_data(df, model_features):
    """
    Apply preprocessing steps to the input DataFrame.
    Ensure output matches the model's expected features.
    """

    # Lowercase column names for consistency
    df.columns = df.columns.str.lower()

    # Convert Turbo from "Yes"/"No" to binary (1/0)
    if "turbo" in df.columns:
        df["turbo"] = df["turbo"].apply(lambda x: 1 if str(x).lower() == "yes" else 0)

    # List of models to be one-hot encoded (all lowercase)
    selected_models = ['prius', 'sonata', 'camry', 'elantra', 'e 350', 'santa fe', 'fit', 'h1', 
                       'tucson', 'x5', 'aqua', 'cruze', 'fusion', 'optima', 'gx 460', 'transit', 
                       'highlander', 'ml 350', 'jetta', 'actyon', 'civic', 'rexton']
    
    # Standardize "model" column (convert to lowercase for consistency)
    if "model" in df.columns:
        df["model"] = df["model"].str.lower().str.strip()  # Convert to lowercase and remove extra spaces
        
        # Replace models not in the selected list with "other"
        df["model"] = df["model"].apply(lambda x: x if x in selected_models else "other")

    # One-hot encoding for selected models (including "other")
    df = pd.get_dummies(df, columns=["model"], drop_first=True)

    # One-hot encoding for other categorical variables (excluding "model", which is already processed)
    categorical_cols = df.select_dtypes(include=["object"]).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Ensure the order of columns matches the model's expected features
    for col in model_features:
        if col not in df:
            df[col] = 0  # Add missing columns as zero (for unseen categories)
    
    df = df[model_features]  # Reorder to match model input

    return df

def transform_input_data(data, model_features):
    """
    Convert input dictionary to DataFrame and apply preprocessing.
    """
    df = pd.DataFrame([data])
    return preprocess_data(df, model_features)
