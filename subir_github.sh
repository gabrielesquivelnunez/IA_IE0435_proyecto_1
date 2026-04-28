#!/bin/bash
# ═══════════════════════════════════════════════════════════════
#  Script para inicializar y subir el repositorio a GitHub
#  Estudiante: Gabriel Esquivel Núñez — C22799
# ═══════════════════════════════════════════════════════════════

# ── CONFIGURACIÓN — editar antes de correr ──────────────────────
GITHUB_USER="gabriel.esquivelnunez"          # ← Cambia esto
REPO_NAME="IA_IE0435_proyecto_1"   # ← Nombre del repo en GitHub
# ────────────────────────────────────────────────────────────────

echo "════════════════════════════════════════════"
echo "  Inicializando repositorio Git"
echo "════════════════════════════════════════════"

git init
git add .
git commit -m "Proyecto 1 IA: preprocesamiento de imágenes y dataset

- Scripts de recorte, binarización y vectorización (OpenCV)
- README, DATASET.md y MODEL_CARD.md
- requirements.txt y LICENSE"

echo ""
echo "════════════════════════════════════════════"
echo "  Conectando con GitHub"
echo "════════════════════════════════════════════"
echo ""
echo "👉 Antes de continuar, crea el repositorio vacío en:"
echo "   https://github.com/new"
echo "   Nombre sugerido: $REPO_NAME"
echo "   (Sin README, sin .gitignore — ya los tenemos)"
echo ""
read -p "¿Ya creaste el repositorio en GitHub? (s/n): " confirm
if [[ "$confirm" != "s" && "$confirm" != "S" ]]; then
    echo "Crea el repositorio primero y vuelve a correr este script."
    exit 1
fi

git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"
git branch -M main
git push -u origin main

echo ""
echo "✅ ¡Listo! Tu repositorio está en:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
