import pandas as pd 
import numpy as np
from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection


if __name__ == "__main__":
    df = pd.read_csv("/Users/yunbo/Documents/GitHub/Machine-learning-learning-and-code-practice/Hyper_parameter_tuning/input/train.csv")
    X = df.drop("price_range",axis=1).values
    y = df.price_range.values
    
    classifier = ensemble.RandomForestClassifier(n_jobs=-1)
    param_grid={
        "n_estimators":[100,200,300,400],
        "max_depth": [1,3,5,7],
        "criterion":["gini","entropy"]
    }

    model = model_selection.GridSearchCV(
        estimator=classifier,
        param_grid=param_grid,
        scoring = "accuracy",
        verbose=10,
        n_jobs=1,
        cv=5
    )

    model.fit(X,y)
    print(model.best_score_)
    print(model.best_estimator_.get_params())


#     0.8674999999999999
# {'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'entropy', 'max_depth': 7, 'max_features': 'sqrt', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 300, 'n_jobs': -1, 'oob_score': False, 'random_state': None, 'verbose': 0, 'warm_start': False}