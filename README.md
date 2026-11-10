# Pipeline ETL en Python

Pipeline de datos modularizado para la extracción, transformación y carga (ETL) del dataset del Titanic, optimizado para almacenar los resultados en formato Parquet.

## 📂 Estructura del Proyecto

```text
etl-pipeline/
│
├── src/
│   ├── __init__.py
│   ├── extract.py      # Carga del dataset desde una URL
│   ├── transform.py    # Limpieza (duplicados, nulos y normalización)
│   └── load.py         # Exportación a formato Parquet
│
├── data/
│   └── processed/      # Archivos de salida procesados
│
├── main.py             # Script principal que ejecuta el flujo completo
├── requirements.txt    # Dependencias del proyecto
└── README.md

## 📊 Dataset y Transformaciones

Utiliza el dataset público del Titanic, aplicando las siguientes etapas:

Extracción: Lectura del archivo CSV original.

Transformación: Normalización de nombres de columnas, eliminación de duplicados y gestión de valores nulos.

Carga: Guardado del DataFrame limpio en un archivo .parquet.

## ⚙️ Instrucciones de Uso

-Instalar las dependencias necesarias:
pip install -r requirements.txt

-Ejecutar el pipeline:
python main.py
```
