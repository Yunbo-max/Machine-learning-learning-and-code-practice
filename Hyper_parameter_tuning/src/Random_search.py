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
        "n_estimators":np.arange(100,1500,100),
        "max_depth": np.arange(1,20),
        "criterion":["gini","entropy"]
    }

    model = model_selection.RandomizedSearchCV(
        estimator=classifier,
        param_distributions=param_grid,
        n_iter=10,
        scoring = "accuracy",
        verbose=10,
        n_jobs=1,
        cv=5
    )

    model.fit(X,y)
    print(model.best_score_)
    print(model.best_estimator_.get_params())


#     0.8895
# {'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'entropy', 'max_depth': 19, 'max_features': 'sqrt', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 600, 'n_jobs': -1, 'oob_score': False, 'random_state': None, 'verbose': 0, 'warm_start': False}
# (Basic) yunbo@dhcp-10-249-103-66 Machine-learning-learning-and-code-practice % 