# generate_dashboard.py
import pandas as pd
from catboost import CatBoostClassifier
import joblib
from explainerdashboard import ClassifierExplainer

if __name__ == "__main__":
    # Загрузка данных и модели из volumes
    model_path = "/app/models/trained_model.cbm"
    data_path = "/app/data/preprocessed_data.csv"

    model = CatBoostClassifier()
    model.load_model(model_path)

    df = pd.read_csv(data_path)
    X = df.drop(columns=["Revenue"])
    y = df["Revenue"]

    explainer = ClassifierExplainer(model, X, y)

    joblib.dump(explainer, "explainer.joblib")
  