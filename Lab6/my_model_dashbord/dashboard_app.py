# dashboard_app.py
import os
import joblib
from explainerdashboard import ExplainerDashboard

if __name__ == '__main__':
    explainer_path = "explainer.joblib"
    if not os.path.exists(explainer_path):
        raise FileNotFoundError(f"Файл {explainer_path} не найден. Убедитесь, что generate_dashboard.py выполнился успешно.")

    explainer = joblib.load(explainer_path)
    db = ExplainerDashboard(explainer, title="Online Shoppers Revenue Prediction")
    db.run(host='0.0.0.0', port=9050, use_waitress=True)