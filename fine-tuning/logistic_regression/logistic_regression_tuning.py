# Import required libraries
import numpy as np
import pandas as pd
import os
import time
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv('../data.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Define hyperparameter grid
param_grid = {'C': [0.01, 0.1, 1, 10, 100],
             'penalty': ['l1', 'l2']}

# Define function for cross-validation and evaluation
def eval_model(estimator, X, y):
    cv = GridSearchCV(estimator, param_grid, cv=5, scoring='accuracy')
    cv_results = cv.fit(X, y)
    best_params = cv_results.best_params_
    model = estimator(**best_params)
    model.fit(X, y)
    return cv_results, model, best_params

# Fine-tune the logistic regression model
start_time = time.time()
logreg = LogisticRegression()
cv_results, best_model, best_params = eval_model(logreg, X, y)
end_time = time.time()

print('Best parameters:', best_params)
print('Model accuracy: {:.2f}'.format(best_model.score(X, y)))
print('Fine-tuning took {:.2f} seconds'.format(end_time - start_time))

# Save results to a file
with open('logistic_regression_results.txt', 'w') as file:
    file.write('Best parameters: {}\n'.format(best_params))
    file.write('Model accuracy: {:.2f}\n'.format(best_model.score(X, y)))
    file.write('Fine-tuning took {:.2f} seconds\n'.format(end_time - start_time))

# Save model and best parameters
with open('logistic_regression_best_model.pickle', 'wb') as file:
    pickle.dump(best_model, file)

# Save hyperparameter grid
with open('logistic_regression_param_grid.pickle', 'wb') as file:
    pickle.dump(param_grid, file)
```

Finally, to execute the script from the command line, navigate to the logistic\_regression directory within the fine\_tuning directory and run:

```bash