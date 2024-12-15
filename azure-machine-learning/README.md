# Trabalho de Conclusão da disciplina de Azure Machine Learning - UNIFOR

Criação de pipeline no Microsoft Azure com AutoML

## Configure and Install Streamlit
```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install streamlit
pip install --upgrade azure-ai-ml azure-identity
```

## Run test
```bash
python -m streamlit run unifor_model_test.py
```

## Replicate configuration
```bash
pip freeze > requirements.txt
```

## Applying configuration
```bash
pip install -r requirements.txt  
```

## Deactivate environment
```bash
deactivate
```
