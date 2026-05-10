# test_prediction.py  only for testing no use in project
from src.mlproject.pipelines.prediction_pipeline import PredictPipeline, CustomData

# Ek sample student ka data
data = CustomData(
    gender="female",
    race_ethnicity="group B",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=72,
    writing_score=74
)

# DataFrame banao
df = data.get_data_as_dataframe()
print("Input DataFrame:")
print(df)

# Predict karo
pipeline = PredictPipeline()
result = pipeline.predict(df)
print(f"\nPredicted Math Score: {result[0]:.2f}")