# RAG chatbot 

## Install dependencies

1. Follow the instructions for ollama installation from their official repository: https://github.com/ollama/ollama. We installed llama 3.2 model in this project. 


2. Now run this command to install dependenies in the `requirements.txt` file. 

```python
pip install -r requirements.txt
```

## Create database

Create the Chroma DB.

```python
python3 populate_database.py
```

## Query the database

Query the Chroma DB.

```python
python3 query_data.py "What is the goal of monopoly?"
```
