# ML Learning Path - A Machine Learning Journey

Welcome to the **ML Learning Path** repository! This repository serves as a collection of notes and implementations of various algorithms, both classical and machine learning, studied during the journey of exploring this field.

## Description

This repository contains a collection of source code, datasets, and models related to learning and exploring various techniques in computer science and machine learning. Its purpose is to document the learning process, implement algorithms from scratch, and apply models to various types of datasets.

## Project Structure

This repository is organized into several main directories:
```bash
ML-LEARNING-PATH/
│
├── src/ # Main directory containing all source code
│ ├── classical_algorithms/ # Implementations of classical (non-ML) algorithms
│ │ ├── Hill_Climbing/
│ │ ├── job_shop_scheduling/
│ │ ├── JobShopSchedulingPSO/
│ │ └── Tsp-ACO/
│ │
│ └── ml/ # Machine Learning related implementations
│ ├── data/ # Collection of datasets used
│ │ ├── Breast Cancer.csv
│ │ ├── credircardinfo.csv
│ │ ├── Data_iris.csv
│ │ ├── data.csv
│ │ ├── DataSet_Iris.csv
│ │ ├── heart_disease.csv
│ │ └── survey_lung_cancer.csv
│ │
│ ├── models/ # Implementations/notebooks for specific ML models/techniques
│ │ ├── Breast_Cancer/
│ │ ├── CNN/
│ │ ├── Data_Survei_Lung_Cancer/
│ │ ├── Feature_Engineering/ 
│ │ ├── HierarchicalClustering/
│ │ ├── NaiveBayes_And_KNN/ 
│ │ ├── RandomForest_Clasifikasi/
│ │ └── SVM_Clasifikasi/
│ │
│ └── USIP2/
│
└── README.md 
```


## Content Overview

### 1. Classical Algorithms (`src/classical_algorithms`)

Contains implementations of classical optimization and search algorithms:

*   **Hill Climbing**: A simple local search algorithm.
*   **Job Shop Scheduling**: Scheduling algorithms for job shop environments.
*   **Job Shop Scheduling PSO**: Implementation of Particle Swarm Optimization for Job Shop Scheduling.
*   **TSP-ACO**: Implementation of Ant Colony Optimization for the Traveling Salesperson Problem.

### 2. Machine Learning (`src/ml`)

Contains code, data, and models related to machine learning:

*   **Data (`src/ml/data`)**:
    *   Breast Cancer Dataset (`Breast Cancer.csv`)
    *   Credit Card Info Dataset (`credircardinfo.csv`)
    *   Iris Dataset (`Data_iris.csv`, `DataSet_Iris.csv`)
    *   Heart Disease Dataset (`heart_disease.csv`)
    *   Lung Cancer Survey Dataset (`survey_lung_cancer.csv`)
    *   Generic dataset (`data.csv`)
*   **Models/Techniques (`src/ml/models`)**:
    *   Analysis and models for the Breast Cancer dataset.
    *   Implementation of Convolutional Neural Network (CNN).
    *   Analysis and models for the Lung Cancer Survey dataset.
    *   Feature Engineering Techniques.
    *   Implementation of Hierarchical Clustering.
    *   Implementation of Naive Bayes and K-Nearest Neighbors (KNN).
    *   Implementation of Random Forest for classification.
    *   Implementation of Support Vector Machine (SVM) for classification.
*   **USIP2 (`src/ml/USIP2`)**: Specific content possibly related to a particular task or project.

## Getting Started

To run the code in this repository, you might need a Python environment with some common libraries for data science and machine learning.

### Prerequisites

*   Python (version 3.7+ recommended)
*   Pip (package installer for Python)

### Installation (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hendrowunga/ML-Learning-Path.git
    cd ML-LEARNING-PATH
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    There might be a `requirements.txt` file in specific subfolders, or you might need to install libraries manually. Commonly used libraries include:
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn tensorflow keras 
    ```

## Usage

Navigate to the specific directory you want to run (e.g., `src/ml/models/RandomForest_Clasifikasi/`) and follow any instructions provided (if any) or run the relevant Python script or Jupyter notebook.

Example:
```bash
cd src/ml/models/SVM_Clasifikasi/
# Assuming there is a notebook file named svm_classification.ipynb
jupyter notebook svm_classification.ipynb
# or if there is a python script
python svm_script_name.py 
