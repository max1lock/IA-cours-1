# TP 1 - Implémentation d’une Pipeline simple



## Structure du Projet

- `main.py`

- `src/image_processor.py`

- `dataset/`

- `input_images/`



## Fonctionnalités

- **Redimensionnement** : Chaque image est redimensionnée en gardant son ratio original
- **Padding** : Un padding est ajouté pour obtenir une image carrée, avec une couleur unie `(114, 114, 144)`
- **Stockage des images traitées** : Les images traitées sont stockées dans `dataset/`

## Utilisation

1. Placer les images dans le dossier `input_images`
2. Installer les dépendances avec `pip install -r requirements.txt`
3. Exécutez le script via `main.py`
