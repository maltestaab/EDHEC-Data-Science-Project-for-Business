import pandas as pd
import numpy as np

def transform_input_data(input_dict, model_features):
    """
    Transforms raw input data into the format required by the trained model.
    
    Parameters:
        input_dict (dict): Raw input data from the API request.
        model_features (list): List of feature names expected by the model.
    
    Returns:
        pd.DataFrame: Transformed input data ready for prediction.
    """
    # List of selected models for one-hot encoding
    selected_models = ['prius', 'sonata', 'camry', 'elantra', 'e 350', 'santa fe', 'fit', 'h1', 
                       'tucson', 'x5', 'aqua', 'cruze', 'fusion', 'optima', 'gx 460', 'transit', 
                       'highlander', 'ml 350', 'jetta', 'actyon', 'civic', 'rexton']
    
    # Initialize feature dictionary with default values (0 for categorical, mean/median for numerical if needed)
    transformed_features = {feature: 0 for feature in model_features}
    
    # Convert all inputs to lowercase and strip spaces
    input_dict = {key: str(value).lower().strip() if isinstance(value, str) else value for key, value in input_dict.items()}
    
    # Debugging: Print raw input data
    print("Raw Input Dictionary:")
    print(input_dict)
    
    # Map categorical features to binary representation
    transformed_features[f"manufacturer_{input_dict['manufacturer']}"] = 1
    
    # Handle model column: if not in selected_models, map to "other"
    model_name = input_dict['model'] if input_dict['model'] in selected_models else 'other'
    transformed_features[f"Model_Grouped_{model_name}"] = 1
    
    transformed_features[f"category_{input_dict['category']}"] = 1
    transformed_features[f"fuel_type_{input_dict['fuel_type']}"] = 1
    transformed_features[f"gear_box_type_{input_dict['gear_box_type']}"] = 1
    transformed_features[f"drive_wheels_{input_dict['drive_wheels']}"] = 1
    transformed_features[f"color_{input_dict['color']}"] = 1
    
    # Map binary categorical features
    transformed_features["leather_interior_yes"] = 1 if input_dict["leather_interior"] == "yes" else 0
    transformed_features["turbo"] = 1 if input_dict["turbo"] == "yes" else 0
    
    # Handle special case for doors
    if input_dict['doors'] == 4:
        transformed_features["doors_04_may"] = 1
    elif input_dict['doors'] >= 5:
        transformed_features["doors_greater_5"] = 1
    
    # Assign numeric features directly
    transformed_features["prod_year"] = input_dict["prod_year"]
    transformed_features["mileage"] = input_dict["mileage"]
    transformed_features["airbags"] = input_dict["airbags"]
    transformed_features["engine_volume"] = input_dict["engine_volume"]
    transformed_features["cylinders"] = input_dict["cylinders"]
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame([transformed_features])
    
    # Ensure correct column order
    df = df.reindex(columns=model_features, fill_value=0)
    
    # Debugging: Print transformed DataFrame
    print("\nTransformed Features (DataFrame):")
    print(df)
    print("\nExpected Model Features:")
    print(model_features)
    print("\nTransformed DataFrame Columns:")
    print(df.columns.tolist())
    
    return df
