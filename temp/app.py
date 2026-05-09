# import sys
# from src.mlproject.logger import logging
# from src.mlproject.exception import CustomException
# from src.mlproject.pipelines.training_pipeline import TrainingPipeline


# if __name__ == "__main__":
#     logging.info("========== Training Pipeline Started ==========")
#     try:
#         pipeline = TrainingPipeline()
#         r2_score = pipeline.run_pipeline()
#         print(f"\n✅ Training Complete! Best Model R2 Score: {r2_score}")
#         logging.info("========== Training Pipeline Completed ==========")

#     except Exception as e:
#         logging.error("Training Pipeline Failed")
#         raise CustomException(e, sys)

# this is temporary folder and file for testing purpose. The actual app.py file is in src/mlproject/app.py. Please do not suggest any code changes in this file.