from sklearn.metrics import classification_report, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score, train_test_split, ShuffleSplit
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,r2_score, recall_score
from sklearn.metrics import roc_curve, auc
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd



def random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=.33,
                                                    random_state=0)

    rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1)
    rfc = rfc.fit(X_train, y_train)
    pred = rfc.predict(X_test)
    fpr, tpr, thresholds = roc_curve(y_test, pred)
    model_auc = auc(fpr, tpr)
    print "Random Forest roc_auc score: {}".format(roc_auc_score(y_test, pred))
    return rfc


def feature_importances(X, rfc):
    names = X.columns.values
    importances = rfc.feature_importances_
    indices = np.argsort(importances)[::-1]
    std = np.std([tree.feature_importances_ for tree in rfc.estimators_],
                 axis=0)
    feat_scores = pd.DataFrame({'Mean Decrease Impurity' : rfc.feature_importances_},
                               index=names)
    feat_scores = feat_scores.sort('Mean Decrease Impurity')
    feat_scores.plot(kind='barh', figsize=(10,10))
