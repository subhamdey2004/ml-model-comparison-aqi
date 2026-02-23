from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def get_models():

    models = {
        "random_forest": RandomForestRegressor(),
        "gradient_boosting": GradientBoostingRegressor(),
        "linear_regression": LinearRegression(),
        "decision_tree": DecisionTreeRegressor(),
    }
    return models
