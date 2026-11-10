import pandas as pd
import os

def load_data(df, output_path):
    print(f"Guardando datos procesados en {output_path}...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print("Datos guardados exitosamente en formato Parquet.")
