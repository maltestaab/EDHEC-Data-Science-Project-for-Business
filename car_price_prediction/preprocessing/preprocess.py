import pandas as pd
import numpy as np

def preprocess_data(df, model_features):
    """
    Apply preprocessing steps to the input DataFrame.
    Ensure output matches the model's expected features.
    """
    # Lowercase column names
    df.columns = df.columns.str.lower()

    # Convert Turbo from "Yes"/"No" to binary (1/0)
    df["turbo"] = df["turbo"].apply(lambda x: 1 if x.lower() == "yes" else 0)

    # Convert Engine volume to cubic cm
    df["engine_volume"] = df["engine_volume"] * 1000

    # Convert Cylinders to integer
    df["cylinders"] = df["cylinders"].astype(int)

    # One-hot encoding for categorical variables
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
