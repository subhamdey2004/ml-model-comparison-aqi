🌫 Comparative Analysis of Supervised Machine Learning Techniques for AQI Prediction .

Overview :-

-> Air pollution is a critical environmental challenge affecting public health, climate systems, and urban sustainability. Accurate     prediction of the Air Quality Index (AQI) enables proactive decision-making and risk mitigation.

-> This project presents a comprehensive comparative analysis of multiple supervised machine learning algorithms for AQI prediction. The system evaluates model performance, analyzes feature importance, and deploys a web-based dashboard for real-time prediction and visualization .

-> The project demonstrates how machine learning can be applied to environmental data analytics and intelligent forecasting systems.

Problem Statement :-

Traditional AQI monitoring systems primarily provide descriptive statistics rather than predictive insights. There is a need for:

- Data-driven AQI prediction models
- Comparative evaluation of supervised ML techniques
- Interactive visualization tools for environmental analysis

This project aims to address these challenges through predictive modeling and comparative analysis.

Methodology :-

The workflow consists of the following stages:

1. Data Preprocessing
   - Handling missing values
   - Feature selection
   - Data normalization

2. Feature Engineering
   - Selection of pollutant-based predictors
   - Removal of irrelevant features

3. Model Training
   - Multiple supervised learning models trained

4. Model Evaluation
   - RMSE comparison
   - Performance analysis

5. Deployment
   - Flask-based interactive dashboard

Dataset Features :-

The AQI prediction is based on pollutant concentration parameters:

- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3

Target Variable :-

- AQI (Air Quality Index)

Machine Learning Models Compared :-

- Random Forest Regressor
- Gradient Boosting Regressor
- Linear Regression
- Decision Tree Regressor

Evaluation Metrics :-

- Root Mean Squared Error (RMSE)
- Model performance comparison
- Feature importance analysis

System Architecture :-

              Data Input
                 ↓
             Preprocessing
                 ↓
            Model Training
                 ↓
           Model Evaluation
                 ↓
        Best Model Selection
                 ↓
       Flask Web Application
                 ↓
    Real-time AQI Prediction + Visualization


Technology Stack :-

Frontend --

- HTML
- CSS (Glass UI Design)
- Bootstrap
- Chart.js

Backend --

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib

Machine Learning :-

- Supervised Regression Algorithms

Features :-

- Interactive AQI prediction dashboard
- Comparative model analysis
- Feature importance visualization
- Real-time prediction interface
- Modern glassmorphism UI design

Installation & Setup :-

To set up the project locally:

# Create Virtual Environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Clone the project
git clone https://github.com/subhamdey2004/ml-model-comparison-aqi.git

# Install dependencies
pip install requirements.txt

# Run Application
python app.py

Results :-

-> The comparative analysis demonstrates differences in prediction accuracy among supervised learning techniques. Ensemble models such as Random Forest and Gradient Boosting show improved performance due to their ability to capture nonlinear relationships between pollutants and AQI.

-> Feature importance analysis indicates that PM2.5 and PM10 are significant predictors of AQI levels.

Future Improvements :-

- Deep learning model integration
- Real-time AQI API data
- Geographic visualization using maps
- Time-series forecasting
- Model explainability (SHAP/LIME)

Developer :-

Subham Dey
Email- dey.subham200414@gmail.com

License :-

This project is licensed under the MIT License - see LICENSE file for details.



