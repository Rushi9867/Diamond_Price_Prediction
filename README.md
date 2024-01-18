# diamond Price Prediction 

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



### STEP 0 - DVC
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