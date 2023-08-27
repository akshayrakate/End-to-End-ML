import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split

from src.Components.data_transformation import DataTransformation
from src.Components.data_transformation import DataTransformationConfig
from model_trainer import ModelTrainer, ModelTrainerConfig


@dataclass
class DataInjestionPath:

    """ Generates paths variables for train_test_csv files
    """
    train_data_path: str = os.path.join('artifact', 'train.csv')
    test_data_path: str = os.path.join('artifact', 'test.csv')
    raw_data_path: str = os.path.join('artifact', 'raw.csv')


class DataInjestion:
    """Creates a csv files in artifact directory
    """

    def __init__(self) -> None:
        self.injestion_config = DataInjestionPath()

    def initiate_data_injestion(self):
        try:
            df = pd.read_csv("src\data\stud.csv")
            logging.info(' Read the dataset as dataframe')

            # Spliting data
            train_df, test_df = train_test_split(
                df, train_size=0.8, random_state=42, shuffle=True)

            # creating respective directories and saving files
            os.makedirs(os.path.dirname(
                self.injestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.injestion_config.raw_data_path,
                      index=False, header=True)

            os.makedirs(os.path.dirname(
                self.injestion_config.train_data_path), exist_ok=True)
            train_df.to_csv(self.injestion_config.train_data_path,
                            index=False, header=True)

            os.makedirs(os.path.dirname(
                self.injestion_config.test_data_path), exist_ok=True)
            test_df.to_csv(self.injestion_config.test_data_path,
                           index=False, header=True)

            logging.info(" Data spliting completed")

            return (
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path

            )
        except Exception as e:
            logging.info('Data spliting issue')
            raise CustomException(e, sys)


if __name__ == '__main__':

    # Initiating DataInjestion
    x = DataInjestion()
    train_data, test_data = x.initiate_data_injestion()

    # Transforming data
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data)

    # Model trainer
    trainer = ModelTrainer()
    r2_square = trainer.initiate_model_trainer(train_arr, test_arr)
    print("R2 score is = ", r2_square)
