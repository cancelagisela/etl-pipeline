# Pipeline de Ingesta y Limpieza (ETL)

Este proyecto implementa un pipeline de datos modularizado para la extracción, transformación y almacenamiento eficiente de un dataset en formato Parquet.

## Estructura del Repositorio
- `main.py`: Script principal que ejecuta el flujo completo del pipeline.
- `src/`: Contiene los módulos lógicos (`extract.py`, `transform.py`, `load.py`).
- `data/processed/`: Almacena el archivo final procesado.

## Requisitos e Instalación
Instala las dependencias ejecutando:
```bash
pip install -r requirements.txt
