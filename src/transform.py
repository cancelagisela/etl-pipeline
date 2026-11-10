import pandas as pd

def transform_data(df):
    print("Iniciando transformación y limpieza de datos...")
    
    # Normalizar nombres de columnas (minúsculas y sin espacios)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Eliminar registros duplicados
    initial_rows = df.shape[0]
    df = df.drop_duplicates()
    print(f"Duplicados eliminados: {initial_rows - df.shape[0]}")
    
    # Gestionar valores nulos
    df = df.dropna(how='all')
    
    print(f"Datos transformados. Filas resultantes: {df.shape[0]}")
    return df
