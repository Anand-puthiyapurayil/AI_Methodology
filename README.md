# 📊 AI Methodology: Employee Performance Analysis

This repository showcases an **end-to-end Machine Learning project** focused on analyzing and predicting **Employee Performance** using various AI and Data Science methodologies. It integrates modern MLOps practices, model interpretability techniques, and comprehensive exploratory data analysis (EDA).

---

## 🎯 Project Objective
- Build robust Machine Learning models for predicting employee performance.
- Industrialize the model through structured data preprocessing, training, inference, and deployment.
- Integrate explainability techniques (SHAP) for transparent and interpretable ML outcomes.

---

## 📁 Project Structure
```
AI_Methodology/
├── data/
│   └── External/   # Downloaded datasets or data retrieved from Kaggle
├── notebooks/
│   ├── EDA.ipynb
│   ├── MLFLOW.ipynb
│   └── Model_Explainability.ipynb
├── scripts/
│   ├── inference.py
│   ├── main.py
│   ├── preprocess.py
│   └── train_model.py
├── Requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### **1. Clone the Repository**
```bash
git clone git@github.com:Anand-puthiyapurayil/AI_Methodology.git
cd AI_Methodology
```

### **2. Set Up the Environment**
Create a virtual environment with Python 3.10:
```bash
conda create --name "envname" python=3.10
conda activate envname
```

Install required dependencies:
```bash
pip install -r Requirements.txt
```

### **3. Data Setup**
Download the dataset from [Kaggle](https://www.kaggle.com/datasets/eshwarganta/employee-performance-analysis-inx-future-inc) and place it under:
```
data/External/
```

### **4. Run the Project**

#### **A. Exploratory Data Analysis (EDA)**
Start Jupyter Notebook:
```bash
jupyter notebook
```
Open and run `notebooks/EDA.ipynb` for detailed exploratory analysis.

#### **B. Model Training & Inference**
Run scripts in the following order:
```bash
python scripts/preprocess.py
python scripts/train_model.py
python scripts/inference.py
python scripts/main.py
```

#### **C. MLFLOW Integration**
To track experiments and manage model versions, run:
```bash
jupyter notebook
```
Open `notebooks/MLFLOW.ipynb` to log experiments, track parameters, metrics, and manage model lifecycle.

### **5. Model Explainability**
Use SHAP for interpretability and explainability:
```bash
jupyter notebook
```
Run `notebooks/Model_Explainability.ipynb` to analyze model predictions and understand feature impacts clearly.

### **6. Deactivate Environment**
After completion:
```bash
conda deactivate
```

---

## 🛠️ Tech Stack

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, SHAP, Matplotlib
- **MLOps Tools**: MLflow
- **Environments**: Jupyter Notebook, Conda

---

## 🌟 Key Features
- **Comprehensive EDA**: Gain insights from data before modeling.
- **End-to-End Pipeline**: Automates preprocessing, training, inference.
- **MLflow Integration**: Robust tracking, logging, and model management.
- **Explainability**: Transparent ML model decisions through SHAP.

---

## 🤝 Contributions
Feel free to contribute:
- Fork this repository.
- Create your branch (`git checkout -b feature/my-feature`).
- Commit changes (`git commit -m 'Added new feature'`).
- Push your changes (`git push origin feature/my-feature`).
- Create a pull request.

---

## 📞 Contact
- **Email**: [anand.nelliot@gmail.com](mailto:anand.nelliot@gmail.com)
- **LinkedIn**: [Anand Puthiyapurayil](https://www.linkedin.com/in/anand-p-/)

---

✨ Happy Modeling! ✨
