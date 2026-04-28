# Proyecto 1: Clasificación de Contaminaciones en Línea de Producción (IA)

**Curso:** IE0435 - Inteligencia Artificial  
**Estudiante:** Gabriel Esquivel Núñez  
**Carné:** C22799  
**Universidad de Costa Rica**

---

## Descripción

Este repositorio contiene el dataset y el código necesario para el preprocesamiento de imágenes orientado a la clasificación de contaminaciones en líneas de producción simuladas. El sistema utiliza técnicas de visión artificial para identificar **granos de arroz** (contaminación positiva) versus otros elementos u objetos (contaminación negativa).

---

## Estructura del Proyecto

```
proyecto1-ia/
├── data/
│   └── processed/          # Imágenes procesadas (binarizadas, 128×128 px)
├── scripts/
│   ├── procesar_imagenes_paso1.py   # Recorte, escala de grises y redimensionado
│   └── procesar_imagenes_paso2.py   # Binarización y generación del CSV
├── reports/                # Informe final del proyecto
├── dataset_gabriel_esquivel.csv     # Dataset final (16,384 píxeles + etiqueta por muestra)
├── DATASET.md
├── MODEL_CARD.md
├── requirements.txt
└── README.md
```

---

## Procedimiento Técnico

### Paso 1 – Recorte y normalización (`procesar_imagenes_paso1.py`)

Coloca tus fotos en una carpeta llamada `fotos/` y ejecuta:

```bash
python scripts/procesar_imagenes_paso1.py
```

- Detecta automáticamente el contorno de la hoja blanca y la recorta.
- Convierte la imagen a escala de grises.
- Redimensiona a **128×128 píxeles** con interpolación INTER_AREA.
- Guarda las imágenes resultantes en `data/processed/`.

### Paso 2 – Binarización y vectorización (`procesar_imagenes_paso2.py`)

Organiza las imágenes procesadas en dos carpetas:

```
conArroz/   ← imágenes con granos de arroz (etiqueta = 1)
sinArroz/   ← imágenes sin granos de arroz (etiqueta = 0)
```

Luego ejecuta:

```bash
python scripts/procesar_imagenes_paso2.py
```

- Aplica umbral de binarización (`pixel >= 200 → 1`, resto `→ 0`).
- Aplana la matriz 128×128 a un vector fila de **16,384 valores**.
- Agrega la etiqueta (`1` = arroz, `0` = no arroz) como última columna.
- Genera `dataset_gabriel_esquivel.csv`.

---

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

---

## Autor

**Gabriel Esquivel Núñez** — C22799  
Estudiante de Ingeniería Eléctrica  
Universidad de Costa Rica
