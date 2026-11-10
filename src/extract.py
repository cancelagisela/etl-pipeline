import pandas as pd

def extract_data(url):
    print("Iniciando extracción de datos...")
    df = pd.read_csv(url)
    print(f"Datos extraídos correctamente. Filas originales: {df.shape[0]}")
    return df
