# DATASET.md — Descripción del Conjunto de Datos

## Cómo se recolectó

Las imágenes fueron capturadas manualmente simulando una línea de producción:

- **Superficie:** Hoja blanca como fondo neutro (simula la banda de producción).
- **Objetos:**
  - **Positivos (label=1):** Granos de arroz (contaminación a detectar).
  - **Negativos (label=0):** Aros metálicos, clips, superficie vacía u otros objetos no-arroz.
- **Total por estudiante:** 30 imágenes (15 positivas + 15 negativas).
- **Cámara:** Smartphone con cámara trasera, foco automático.

## Variaciones presentes

| Variable        | Detalle                                              |
|-----------------|------------------------------------------------------|
| Iluminación     | Luz natural y artificial, variaciones de sombras     |
| Ángulo          | Cenital (~90°) con ligeras variaciones               |
| Distancia       | Aproximadamente 20–40 cm de la superficie            |
| Cantidad arroz  | 1 a varios granos por imagen positiva                |

## Preprocesamiento aplicado

1. Detección del contorno de la hoja y recorte automático.
2. Conversión a escala de grises.
3. Redimensionado a 128×128 píxeles (interpolación INTER_AREA).
4. Binarización con umbral 200 (píxel ≥ 200 → 1, resto → 0).
5. Aplanamiento a vector fila de 16,384 valores + columna de etiqueta.

## Limitaciones

- Variaciones de iluminación pueden afectar el umbral de binarización.
- Las imágenes fueron capturadas en condiciones controladas; puede no generalizar bien a entornos industriales reales.
- El tamaño del dataset es pequeño (30 imágenes por estudiante).
- Objetos muy pequeños o parcialmente ocluidos pueden ser difíciles de distinguir.
- Dependencia del color/textura del fondo: funciona mejor con fondos blancos uniformes.

## Proceso de etiquetado

- Etiquetado manual por el estudiante recolector.
- Criterio: `label=1` si y solo si hay al menos un grano de arroz visible en la imagen.
- No se usó herramienta de anotación externa; la etiqueta se asignó directamente al nombre de carpeta.
