# Diamond Price Prediction 

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create environment after opening the repository

In conda :

```bash
conda create -n diapred python=3.11 -y
```

```bash
conda activate diapred
```

In Vscode :

```bash
python -m venv menv
```

```bash
menv\Scripts\cativate
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03 RUN WebApplication

```bash
    python app.py
```

```
    localhost:8000/predict
```
### STEP 04  - MLFLOW

[Documentation](https://mlflow.org/docs/latest/python_api/mlflow.html)

```bash
    python test.py
```

```bash 
    mlflow ui
```

### STEP 05 - DVC

[Documentation](https://dvc.org/doc)

```bash
    dvc init
```

```bash
    dvc add Data/train.csv
```

```bash
    dvc checkout
```

```bash 
    dvc remote add -d remote_storage /config/workspace/myremotestorage
```

```bash
    dvc push
```

### STEP 06 APACHE AIRFLOW


[Documentation](https://airflow.apache.org/docs/)
 

[Dagshub](https://dagshub.com/)

### STEP 07 DOCKER 

```bash
    docker-compose up
```

```bash
    localhost:8080
```

```bash
    Username : admin
    password : admin
```
