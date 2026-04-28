import cv2
import numpy as np
import os

# ── CONFIGURACIÓN ──────────────────────────────────────────
CARPETA_CON_ARROZ  = "conArroz"
CARPETA_SIN_ARROZ  = "sinArroz"
ARCHIVO_SALIDA     = "dataset.csv"
UMBRAL             = 200  # pixel >= umbral → 1 (blanco), < umbral → 0 (objeto)
# ───────────────────────────────────────────────────────────

def imagen_a_vector(ruta, etiqueta):
    img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"  No se pudo leer: {ruta}")
        return None
    
    # Convertir a matriz de 1s y 0s según el umbral
    binaria = (img >= UMBRAL).astype(int)
    
    # Aplanar a vector fila y agregar etiqueta al final
    vector = binaria.flatten().tolist()
    vector.append(etiqueta)
    return vector

def procesar_carpeta(carpeta, etiqueta):
    vectores = []
    extensiones = ('.jpg', '.jpeg', '.png', '.webp')
    archivos = [f for f in os.listdir(carpeta) if f.lower().endswith(extensiones)]
    
    print(f"\nProcesando '{carpeta}' ({len(archivos)} imágenes, etiqueta={etiqueta})")
    
    for i, nombre in enumerate(archivos, 1):
        ruta = os.path.join(carpeta, nombre)
        print(f"  [{i}/{len(archivos)}] {nombre}")
        vector = imagen_a_vector(ruta, etiqueta)
        if vector is not None:
            vectores.append(vector)
    
    return vectores

# ── PROCESAMIENTO ───────────────────────────────────────────
todos = []
todos += procesar_carpeta(CARPETA_CON_ARROZ, etiqueta=1)
todos += procesar_carpeta(CARPETA_SIN_ARROZ, etiqueta=0)

# ── GUARDAR CSV ─────────────────────────────────────────────
with open(ARCHIVO_SALIDA, 'w') as f:
    for vector in todos:
        linea = ",".join(map(str, vector))
        f.write(linea + "\n")

print(f"\n Listo! {len(todos)} imágenes procesadas.")
print(f"📄 Archivo guardado: {ARCHIVO_SALIDA}")
print(f"📐 Dimensiones: {len(todos)} filas × {len(todos[0])} columnas")
print(f"   (128×128 píxeles = 16384 columnas + 1 etiqueta = 16385 columnas)")
