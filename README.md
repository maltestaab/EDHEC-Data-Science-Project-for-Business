# EDHEC-Data-Science-Project-for-Business
## Car Price Prediction API and Web Application

## Introduction
This project focuses on building a machine learning model for car price prediction using real-world data from Kaggle. The goal is to develop a system that can take user-input features and return an estimated car price, following a structured workflow from data preprocessing to model deployment. The initial phase involved data exploration, handling missing values, and addressing categorical and numerical features to ensure consistency and usability. The dataset was examined for missing values, with features such as Levy being dropped due to excessive missing data, while other categorical variables were cleaned and standardized by converting all text to lowercase. We also removed redundant identifiers such as the ID column. Features such as mileage and engine volume, originally stored as strings, were transformed into numerical values, and an additional binary column was created to indicate whether a car had a turbo feature.

## Metric of Performance
Since our target variable is continuous, we used regression-appropriate performance metrics to evaluate model accuracy. We initially considered multiple metrics, including Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), and Mean Squared Error (MSE), before selecting MSE and R² score as our primary metrics. The choice of MSE was motivated by its ability to penalize larger errors more heavily, making it particularly useful for tree-based models such as XGBoost. The R² score was chosen to provide an interpretable measure of how well our models explained the variance in car prices.

## Dataset Preprocessing
We applied extensive preprocessing to ensure data quality before training the model. First, missing values were identified and handled, with the Levy column being dropped due to excessive null entries. String-based categorical variables were converted to lowercase for uniformity, and unique or problematic features, such as ID, were removed. The Mileage column, initially stored as a string with units (e.g., "186005 km"), was cleaned and converted into an integer format. The Engine Volume column was similarly transformed into a numerical feature, and a new binary column was created to indicate the presence of a turbo engine.
One of the most challenging preprocessing steps involved encoding the Model column, which contained over 1,500 distinct values. Instead of creating thousands of dummy variables, we applied a frequency-based encoding approach, retaining only the most frequent models while grouping the remaining 50% into a single "other" category. Additional preprocessing included handling outliers in the target variable by removing extreme price values beyond $25 million, which could distort model predictions. Since the price distribution was highly skewed, we applied a log transformation to stabilize variance and improve model performance.

## Models

### Baseline Models
To establish a performance benchmark, we implemented two baseline models. The first was a simple linear regression model applied to a scaled version of the feature set, capturing linear relationships between features and car prices. The second baseline assigned the mean target value to every observation, representing the lowest level of predictive capability that our machine learning models needed to surpass.

### Tree-Based Models
We then explored tree-based models, which are well-suited for capturing nonlinear relationships in structured data. We started with a basic Decision Tree Regressor but found it prone to overfitting. To mitigate this, we introduced a Random Forest model, which aggregates multiple decision trees to reduce variance. Further improvements were achieved by testing Gradient Boosting Regressor and XGBoost, which refine predictions sequentially by learning from previous errors. Among these, XGBoost demonstrated superior performance due to its built-in regularization and optimization features.

### Neural Network Model
Finally, we experimented with a deep learning approach, implementing a neural network with six fully connected hidden layers. To prevent overfitting, we applied Batch Normalization and Dropout layers while using ReLU activation functions to introduce non-linearity. The model was trained using the Adam optimizer with a carefully tuned learning rate, and early stopping was employed to optimize generalization.

### Fine-Tuning Hyperparameters
After identifying XGBoost as the best-performing model, we fine-tuned its hyperparameters using GridSearchCV. To further optimize performance, we leveraged Optuna, an automated hyperparameter tuning framework that efficiently searches the parameter space using adaptive sampling techniques. This approach yielded the best hyperparameters: max_depth=23, learning_rate=0.0298, n_estimators=511, subsample=0.8278, reg_alpha=0.0070, and reg_lambda=7.6564. The optimized model achieved an MAE of 4,540.64 and an R² score of 0.73, demonstrating strong predictive capabilities. The model is saved using an ubj file. It was first tried using Pickle, but the Render RAM limit stopped that from working. Afterwards JSON was tried, but the JSON model file was too large for GitHub (over 100 MB). Consequently ubj was chosen as a good in-between.

## Deployment
The deployment pipeline integrates FastAPI, Streamlit, and Render to provide a fully functional web-based prediction service. FastAPI serves as the backend API, handling incoming requests, validating user input, and preprocessing data before passing it to the trained model. The preprocessing function ensures that categorical variables are one-hot encoded, unknown car models are mapped to an "other" category, and numerical features are structured to match the model’s expected format. This ensures that new input data is processed identically to the training data. The model then generates predictions, which are transformed back from log scale to provide realistic price estimates.

## Frontend Interface
The frontend, developed using Streamlit, offers an interactive interface where users can input car specifications such as manufacturer, model, production year, mileage, and other attributes. Upon submission, the input data is sent to the FastAPI backend, which processes the request and returns a price prediction. The frontend is designed for usability, featuring a structured layout and interactive components that allow users to experiment with different configurations.

## Links
GitHub (incl. Notebook, Preprocessing Package, Main.py, ubj File, streamlit_app.py: https://github.com/maltestaab/EDHEC-Data-Science-Project-for-Business
Streamlit: https://edhec-data-science-project-for-business.onrender.com/
FastAPI: https://edhec-data-science-project-for-business-1.onrender.com/

## Conclusion
This project successfully integrates machine learning with modern web technologies to deliver an efficient and accessible car price prediction tool. FastAPI ensures fast and reliable backend processing, while Streamlit provides an interactive and user-friendly interface. Render enables seamless cloud deployment, making the application widely accessible. Future improvements may include expanding the dataset with additional vehicle attributes, refining feature engineering techniques, and implementing an automated model retraining system to continuously improve prediction accuracy. The project demonstrates the effectiveness of combining advanced machine learning techniques with scalable web applications, making it a valuable tool for real-world price estimation tasks.

