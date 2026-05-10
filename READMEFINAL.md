# 🎓 Student Math Score Predictor

An end-to-end machine learning project that predicts a student's math score based on demographic and academic features. Built with a modular pipeline architecture, experiment tracking, and deployed on Azure App Service.

---

## 🔗 Quick Links

- **Live Demo:** [student-score-predictor on Azure](https://student-score-predictor-hhhxh3ctghc5b7cq.southindia-01.azurewebsites.net)
- **Experiment Tracking:** [DagsHub MLflow Dashboard](https://dagshub.com/rakeshcpr011/E2EDSprojectKN)

---

## 📌 Problem Statement

Given a student's background information — gender, ethnicity, parental education, lunch type, test preparation course, reading score, and writing score — predict their **math score**.

---

## 📂 Project Structure

```
E2EDSprojectKN/
├── src/mlproject/
│   ├── components/
│   │   ├── data_ingestion.py         # Load and split raw data
│   │   ├── data_transformation.py    # Preprocessing pipeline
│   │   └── model_tranier.py          # Train, evaluate, log to MLflow
│   ├── pipelines/
│   │   ├── training_pipeline.py      # End-to-end training orchestration
│   │   └── prediction_pipeline.py    # Load model and predict
│   ├── exception.py                  # Custom exception handling
│   ├── logger.py                     # Logging setup
│   └── utils.py                      # Helper functions
├── artifacts/                        # Saved model and preprocessor
├── notebook/                         # EDA and experimentation
├── templates/
│   ├── index.html                    # Landing page
│   └── home.html                     # Prediction form
├── app.py                            # Training pipeline runner
├── application.py                    # Flask web application
└── requirements.txt
```

---

## 🧠 Features Used

| Feature | Type |
|---|---|
| Gender | Categorical |
| Race / Ethnicity | Categorical |
| Parental Level of Education | Categorical |
| Lunch | Categorical |
| Test Preparation Course | Categorical |
| Reading Score | Numerical |
| Writing Score | Numerical |

**Target:** `math_score` (Regression)

---

## ⚙️ ML Pipeline

```
Raw Data
   │
   ▼
Data Ingestion       → Train / Test split
   │
   ▼
Data Transformation  → StandardScaler (numerical)
                     → OneHotEncoder (categorical)
   │
   ▼
Model Training       → 7 models evaluated with GridSearchCV
   │                   Linear Regression, Decision Tree,
   │                   Random Forest, Gradient Boosting,
   │                   XGBoost, CatBoost, AdaBoost
   ▼
Best Model Selected  → Logged to MLflow / DagsHub
   │
   ▼
artifacts/model.pkl + preprocessor.pkl saved
```

---

## 📊 Experiment Tracking

All experiments are tracked using **MLflow** with **DagsHub** as the remote backend.

- Parameters, metrics, and models logged per run
- Best model auto-registered in MLflow Model Registry
- Experiments visible at: [DagsHub Dashboard](https://dagshub.com/rakeshcpr011/E2EDSprojectKN)

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rkcpr011/E2EDSprojectKN.git
cd E2EDSprojectKN
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file in the project root:

```
DAGSHUB_USER_TOKEN=your_dagshub_token_here
```

### 4. Run training pipeline

```bash
python app.py
```

### 5. Start Flask app

```bash
python application.py
```

Open browser at `http://localhost:5000`

---

## ☁️ Deployment

Deployed on **Azure App Service** via GitHub Actions CI/CD.

```
Push to main branch
       │
       ▼
GitHub Actions triggered
       │
       ▼
Azure App Service builds and deploys automatically
       │
       ▼
Live at Azure URL ✅
```

**Stack:**
- Runtime: Python 3.11
- Server: Gunicorn
- Platform: Azure App Service (Linux)
- CI/CD: GitHub Actions

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| ML Libraries | Scikit-learn, XGBoost, CatBoost |
| Web Framework | Flask |
| Experiment Tracking | MLflow + DagsHub |
| Deployment | Azure App Service |
| CI/CD | GitHub Actions |
| Version Control | Git + GitHub |

---

## 👤 Author

**Rakesh Kumar**  
SDE2 at CGI | Masters in AI/ML  
[GitHub](https://github.com/Rkcpr011) · [DagsHub](https://dagshub.com/rakeshcpr011)
