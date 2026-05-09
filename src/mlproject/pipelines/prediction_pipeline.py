import sys
import os
import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from src.mlproject.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            logging.info("Loading model and preprocessor from artifacts/")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            logging.info("Applying preprocessor on input features")
            data_scaled = preprocessor.transform(features)

            logging.info("Running prediction")
            predictions = model.predict(data_scaled)

            return predictions

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    """
    Maps user input (from Flask form) into a DataFrame
    that matches the training data structure exactly.
    """
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: float,
        writing_score: float,
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self) -> pd.DataFrame:
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Input converted to DataFrame successfully")
            return df

        except Exception as e:
            raise CustomException(e, sys)
