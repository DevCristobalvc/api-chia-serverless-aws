from src.utils.loadfiles import load_data, save_data

def get_holders():
    data = load_data()
    print(data)
    return data['holders']

