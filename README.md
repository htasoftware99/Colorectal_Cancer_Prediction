# Colorectal Cancer Prediction

This project is a machine learning application that predicts the likelihood of colorectal cancer based on user-provided data. It includes a web interface for user interaction, a data processing pipeline, model training, and an MLOps pipeline for orchestration.

## Project Structure

```
/
├── artifacts/                # Stores model and data artifacts
├── kubeflow_pipeline/        # Contains the Kubeflow pipeline definition
├── mlruns/                   # Directory for MLflow experiment tracking
├── notebook/                 # Jupyter notebooks for exploration and analysis
├── src/                      # Source code for the project
│   ├── data_processing.py    # Scripts for data cleaning and preprocessing
│   ├── model_training.py     # Scripts for training the machine learning model
│   └── ...
├── static/                   # Static files for the web application (CSS, JS)
├── templates/                # HTML templates for the web interface
├── app.py                    # Main Flask application file
├── Dockerfile                # Dockerfile for containerizing the application
├── requirements.txt          # Python dependencies
└── setup.py                  # Setup script for the project
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Colorectal_Cancer_Prediction
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## Kubeflow Pipeline

The `kubeflow_pipeline/mlops_pipeline.py` file defines the MLOps pipeline for this project. This pipeline automates the machine learning workflow, including data processing, model training, and evaluation.
