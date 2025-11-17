"""
FILE: train_and_predict.py
LOCATION: project root

Purpose:
- Load data (locations.csv)
- Preprocess
- Train RandomForest model
- Create predictions.json
"""

import json
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("data/locations.csv")  
# Required columns: id, latitude, longitude, rainfall_mm, elevation, soil_moisture, label(optional)

features = ["rainfall_mm", "soil_moisture", "elevation"]
df = df.dropna(subset=features)

X = df[features]
y = df.get("label", pd.Series([0] * len(df)))  # if no label exists, all 0

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# If labels exist, show accuracy
if "label" in df.columns:
    print("Model evaluation:")
    print(classification_report(y, model.predict(X)))

# Predict probabilities
df["risk_prob"] = model.predict_proba(X)[:, 1]
df["risk_label"] = (df["risk_prob"] >= 0.5).astype(int)

# Create JSON output
output = []
for _, row in df.iterrows():
    output.append({
        "id": int(row["id"]),
        "latitude": float(row["latitude"]),
        "longitude": float(row["longitude"]),
        "rainfall_mm": float(row["rainfall_mm"]),
        "soil_moisture": float(row["soil_moisture"]),
        "elevation": float(row["elevation"]),
        "risk_score": float(row["risk_prob"]),
        "risk_label": int(row["risk_label"]),
        "recommended_action": "Evacuate" if row["risk_prob"] >= 0.8 else "Monitor"
    })

with open("predictions.json", "w") as f:
    json.dump(output, f, indent=2)

print("Saved predictions.json")
