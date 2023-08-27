import os, sys
import pandas  as pd
import numpy as np

from src.utils import load_object
from src.exception import CustomException



class PredictPipeline:
    
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifact","model_trainer.pkl")
            preprocessor_path=os.path.join('artifact','preprocessor.pkl')
            
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == '__main__':
    
    p = PredictPipeline()
        
    df = pd.read_csv("artifact/test.csv")
    x = df.iloc[1]
    
    output = p.predict(x)
    print(output)
    