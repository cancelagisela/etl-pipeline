from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    print("=== INICIANDO PIPELINE ETL ===")
    
    # URL de un dataset CSV público de ejemplo
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    output_file = "data/processed/dataset_procesado.parquet"
    
    # 1. Extracción
    df_raw = extract_data(url)
    
    # 2. Transformación
    df_clean = transform_data(df_raw)
    
    # 3. Carga
    load_data(df_clean, output_file)
    
    print("=== PIPELINE FINALIZADO CON ÉXITO ===")

if __name__ == "__main__":
    run_pipeline()
