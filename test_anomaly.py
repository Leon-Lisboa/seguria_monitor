from api.anomaly_detector import AnomalyDetector
import pandas as pd

def test_anomaly_detection():
    detector = AnomalyDetector()
    normal_data = pd.DataFrame([[0.1, 0.2, 0.3, 0.4]])
    detector.fit(normal_data)
    pred = detector.predict(normal_data)
    assert pred[0] == 1