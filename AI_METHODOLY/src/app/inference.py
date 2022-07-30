import sys
sys.path.append('..')
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load
from AI_METHODOLY.src.app.preprocess import preprocess

from pathlib import Path
DATA_DIR = Path(r'../../data/external/')
MODEL_DIR=Path(r'../../models/')
df_master= pd.read_excel(DATA_DIR/"Employee_Perfomance.xls",index_col='EmpNumber')


def predictions(data: pd.DataFrame):
    target = data['PerformanceRating']
    train = data.drop(['PerformanceRating'], axis=1)
    processedtrain = preprocess(train, MODEL_DIR)
    x_train, x_test, y_train, y_test = train_test_split(processedtrain, target, test_size=0.2)
    k = load(MODEL_DIR / 'RFC.joblib')
    predict = k.predict(x_test)
    # print(predict)
    newdf = pd.DataFrame(predict, columns=['perfomance_rating'])
    submissiondf = newdf.rename_axis('Emp_ID').reset_index()
    print(submissiondf.head())
    return submissiondf.head()

