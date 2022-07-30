import pandas as pd
from AI_METHODOLY.src.app.inference import predictions
from AI_METHODOLY.src.app.train_model import build_model

from pathlib import Path

DATA_DIR = Path(r'../../data/external/')
df_master= pd.read_excel(DATA_DIR/"Employee_Perfomance.xls",index_col='EmpNumber')

def main(data):
    evalaute=build_model(data)
    predict=predictions(data)
    return evalaute , predict

if __name__ == "__main__":
    main(df_master)