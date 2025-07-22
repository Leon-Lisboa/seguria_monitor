from fastapi import APIRouter
from api.anomaly_detector import AnomalyDetector
from api.alerts import send_email_alert, send_whatsapp_alert
import pandas as pd

router = APIRouter()
detector = AnomalyDetector()
detector.fit(pd.DataFrame([[0.1, 0.2, 0.3, 0.4]]))  # modelo treinado inicial

@router.post("/monitor")
async def monitor(data: dict):
    df = pd.DataFrame([data])
    pred = detector.predict(df)[0]
    if pred == -1:
        msg = f"⚠️ Anomalia detectada: {data}"
        send_email_alert("Anomalia Detecção", msg)
        send_whatsapp_alert(msg)
    return {"status": "ok", "anomaly": pred == -1}