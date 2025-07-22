from sklearn.ensemble import IsolationForest
import pandas as pd

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.01)
    def fit(self, X: pd.DataFrame):
        self.model.fit(X)
    def predict(self, X: pd.DataFrame):
        return self.model.predict(X)