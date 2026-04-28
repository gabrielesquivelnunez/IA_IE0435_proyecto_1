# MODEL_CARD.md

## Model name + version

**Clasificador de Contaminaciones en Línea de Producción v1.0**  
Proyecto 1 — IE0435 Inteligencia Artificial, I-2026

---

## Intended use

**Uso previsto:**  
Clasificación binaria de imágenes de una línea de producción simulada para detectar la presencia de granos de arroz (contaminación).

**Fuera del alcance:**  
- Imágenes de entornos industriales reales.
- Detección de múltiples tipos de contaminantes simultáneamente.
- Imágenes con fondos distintos a superficie blanca.
- Inferencia en tiempo real sobre video.

---

## Data summary

- **Recolección:** Imágenes tomadas manualmente con smartphone sobre hoja blanca.
- **Tamaño:** ~30 imágenes por estudiante (15 positivas, 15 negativas).
- **Variaciones:** Diferentes condiciones de luz, ángulos y cantidades de arroz.
- **Formato final:** Vectores de 16,384 valores binarios (128×128 px) + etiqueta.

---

## Labeling process

- Etiquetado manual por el estudiante recolector.
- `label = 1`: presencia de granos de arroz en la imagen.
- `label = 0`: ausencia de arroz (puede haber otros objetos como aros o clips).
- Sin revisión de segunda persona; posible sesgo de etiquetado individual.

---

## Metrics

Los modelos evaluados incluyen: Árbol de Decisión, Naive Bayes, KNN, SVM.

| Métrica    | Descripción                              |
|------------|------------------------------------------|
| Accuracy   | Porcentaje de clasificaciones correctas  |
| Precision  | TP / (TP + FP)                           |
| Recall     | TP / (TP + FN)                           |
| F1-Score   | Media armónica de Precision y Recall     |

**Split utilizado:** 80% entrenamiento / 20% prueba (estratificado).

---

## Ethical / safety notes

- **Sesgo por iluminación:** El modelo puede fallar bajo condiciones de luz muy diferentes a las de entrenamiento.
- **Sesgo por cámara:** Imágenes tomadas con un único dispositivo; puede no generalizar a otras cámaras.
- **Sesgo de fondo:** Entrenado solo sobre fondo blanco; sensible a cambios de superficie.

---

## Limitations

- Granos de arroz muy pequeños o fuera de foco pueden no ser detectados.
- Alta dimensionalidad del vector (16,384) puede causar sobreajuste con datasets pequeños.
- No hay data augmentation aplicada.
- El umbral de binarización (200) fue fijado manualmente y puede no ser óptimo para todas las condiciones de luz.

---

## Reproducibility

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Colocar fotos en fotos/ y ejecutar preprocesamiento
python scripts/procesar_imagenes_paso1.py
python scripts/procesar_imagenes_paso2.py

# 3. Entrenar modelo (ver notebook o script de entrenamiento)
```

**Hardware usado:** Computadora personal, CPU, sin GPU requerida.  
**SO:** Ubuntu / Linux  
**Python:** 3.10+
