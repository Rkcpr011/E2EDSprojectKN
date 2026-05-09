import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            # Step 1: Data Ingestion
            logging.info(">>> Stage 1: Data Ingestion Started <<<")
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info(">>> Stage 1: Data Ingestion Completed <<<")

            # Step 2: Data Transformation
            logging.info(">>> Stage 2: Data Transformation Started <<<")
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_transormation(
                train_data_path, test_data_path
            )
            logging.info(">>> Stage 2: Data Transformation Completed <<<")

            # Step 3: Model Training
            logging.info(">>> Stage 3: Model Training Started <<<")
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f">>> Stage 3: Model Training Completed | Best R2 Score: {r2_score} <<<")

            return r2_score

        except Exception as e:
            raise CustomException(e, sys)
