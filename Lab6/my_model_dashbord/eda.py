import pandas as pd

if __name__ == '__main__':
    #Вставить код EDA
    # Путь к CSV-файлу — относительно текущей директории
    DATASET_PATH = "online_shoppers_intention.csv"
    df = pd.read_csv(DATASET_PATH)
    df.head()
    df['Weekend'] = df['Weekend'].map({True: 1, False: 0})
    df['Revenue'] = df['Revenue'].map({True: 1, False: 0})

    #OneHotEncodим VisitorType
    # Создаём переменные
    visitor_types_dummies = pd.get_dummies(df['VisitorType'], prefix='VisitorType').astype(int)
    # Добавляем к DataFrame
    df = pd.concat([df, visitor_types_dummies], axis=1)
    # удаляю стары столбец
    df = df.drop('VisitorType', axis=1)
    
    #OneHotEncodим Month
    # Создаём переменные
    month_dummies = pd.get_dummies(df['Month'], prefix='Month').astype(int)
    # Добавляем к DataFrame
    df = pd.concat([df, month_dummies], axis=1)
    # удаляю стары столбец
    df = df.drop('Month', axis=1)


    df.to_csv("preprocessed_data.csv", index=False)
    print(df.info())