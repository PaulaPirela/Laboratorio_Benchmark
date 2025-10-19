import os
import pandas as pd

def combinar_archivos_en_dataframe(ruta_carpeta, separador=','):
    """
    Lee todos los archivos de una carpeta y los combina en un único DataFrame.

    Args:
        ruta_carpeta (str): La ruta del directorio que contiene los archivos.
        separador (str): El delimitador de los archivos CSV (ej: ',' o ';').

    Returns:
        pandas.DataFrame: Un DataFrame que contiene los datos de todos los archivos.
    """
    
    # 1. Lista para almacenar cada DataFrame
    lista_dataframes = []
    
    # 2. Iterar sobre todos los archivos de la carpeta
    for nombre_archivo in os.listdir(ruta_carpeta):
        
        # 3. Construir la ruta completa al archivo
        ruta_completa_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        
        # 4. Procesar solo archivos (evitar subdirectorios) y filtrar por extensión (ej. .csv)
        if os.path.isfile(ruta_completa_archivo) and nombre_archivo.endswith('.csv'):
            print(f"Leyendo archivo: {nombre_archivo}...")
            
            try:
                # 5. Leer el archivo y crear un DataFrame temporal
                df_temporal = pd.read_csv(ruta_completa_archivo, sep=separador)
                
                # Opcional: Agregar una columna para identificar el archivo de origen
                df_temporal['Archivo_Fuente'] = nombre_archivo
                
                # 6. Agregar el DataFrame a la lista
                lista_dataframes.append(df_temporal)
                
            except Exception as e:
                print(f"Error al leer {nombre_archivo}: {e}")
                
    # 7. Concatenar todos los DataFrames de la lista en uno solo
    if lista_dataframes:
        df_final = pd.concat(lista_dataframes, ignore_index=True)
        print("\n¡Combinación de archivos completada con éxito!")
        return df_final
    else:
        print("\nNo se encontraron archivos .csv para combinar.")
        return pd.DataFrame()

# --- USO DEL CÓDIGO ---

# Define la ruta de la carpeta donde están tus archivos
RUTA_DE_LOS_ARCHIVOS = 'C:/Ruta/A/Mi/Carpeta/De/Datos' 
# Si los archivos son delimitados por punto y coma, cambia el separador a ';'
SEPARADOR_CSV = ',' 

# Llamar a la función
df_combinado = combinar_archivos_en_dataframe(RUTA_DE_LOS_ARCHIVOS, SEPARADOR_CSV)

# Mostrar las primeras filas del DataFrame resultante
print("-" * 50)
print("DataFrame Final (Primeras 5 filas):")
print(df_combinado.head())

# Mostrar información sobre el DataFrame
print("-" * 50)
df_combinado.info()