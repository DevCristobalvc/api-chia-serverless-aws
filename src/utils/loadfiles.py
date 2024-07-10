# Cargar datos desde el archivo JSON
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'utils', 'data.json')

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"holders": [], "initiatives": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Guardar datos en el archivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)