import pandas as pd
import numpy as np
from catboost import CatBoostClassifier, Pool, cv
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    data = pd.read_csv('preprocessed_data.csv')

    y = data['Revenue']
    x = data.drop('Revenue', axis=1)
 
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, train_size=0.85, random_state=42, stratify=y
    )

    model = CatBoostClassifier(
        iterations=1000,
        loss_function='Logloss',
        custom_loss=['Accuracy'],
        random_seed=42,
        verbose=100
    )

    model.fit(
        x_train, y_train,
        eval_set=(x_test, y_test),
        use_best_model=True,
        plot=False
    )

    model.save_model('trained_model.cbm')