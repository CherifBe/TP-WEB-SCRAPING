# Scraper des Personnages de Genshin Impact

Ce projet est une application basée sur FastAPI qui extrait les données des personnages depuis le site Fandom de Genshin Impact et les fournit via une API. Les données sont également sauvegardées dans un fichier CSV pour une utilisation ultérieure.

## Fonctionnalités

- Extraction des données des personnages de Genshin Impact, notamment :
  - URL de l'icône
  - Nom
  - Qualité
  - Élément
  - Arme
  - Région
  - Type de modèle
- Sauvegarde des données extraites dans un fichier CSV (`genshin_characters.csv`).
- Fourniture d'un point d'accès API pour récupérer les données des personnages au format JSON.
- Middleware CORS permettant les requêtes cross-origin (par exemple, pour une utilisation avec un frontend).

## Pourquoi Nous Avons Choisi Requests + BeautifulSoup pour le Scraping

Nous avons choisi Requests et BeautifulSoup pour le scraping web car :

- **Requests** : Fournit un moyen simple et fiable d'effectuer des requêtes HTTP, de gérer les réponses et de traiter les erreurs.
- **BeautifulSoup** : Offre des outils puissants et intuitifs pour analyser et naviguer dans le HTML, facilitant l'extraction des données nécessaires depuis les pages web.
- Ces bibliothèques sont légères, bien documentées et largement utilisées, ce qui les rend idéales pour construire une solution de scraping robuste et maintenable.

## Analyse du Site

- Le site semble majoritairement basé sur HTML statique, ce qui signifie que les données sont probablement visibles directement dans le code source (sans nécessiter de rendu JavaScript).
- Les pages sont bien structurées, typiques des wikis (tableaux, listes, etc.).

## Recommandation d'Outils

Étant donné que le site ne semble pas nécessiter de rendu JavaScript complexe, voici mes recommandations :

### BeautifulSoup + Requests (Meilleur Choix pour ce Cas)

**Pourquoi :**

- Le site semble statique et bien structuré.
- BeautifulSoup excelle dans l'extraction d'informations d'HTML statique.

**Avantages :**

- Simple à configurer.
- Parfait pour extraire des tableaux ou des listes structurées, comme les données des personnages de Genshin Impact.

## Prérequis

- Python 3.8+
- `requests`
- `beautifulsoup4`
- `fastapi`
- `uvicorn`

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application :

   ```bash
   uvicorn main:app --reload
   ```

4. Ouvrez votre navigateur et accédez à :

   - Documentation de l'API : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Point d'accès API : [http://127.0.0.1:8000/genshin_characters](http://127.0.0.1:8000/genshin_characters)

## Utilisation

### Extraction des Données

La fonctionnalité d'extraction est gérée par la fonction `scrape_genshin_characters_to_csv`. Elle :

1. Récupère les données des personnages Genshin Impact depuis l'URL spécifiée.
2. Extrait les informations pertinentes de la page web.
3. Enregistre les données dans un fichier CSV (`genshin_characters.csv`).

Par défaut, l'URL utilisée est :

```
https://genshin-impact.fandom.com/wiki/Characters
```

### Point d'Accès API

Le point d'accès `/genshin_characters` fournit les données des personnages depuis le fichier CSV au format JSON. Si le fichier CSV est introuvable, le point d'accès renvoie une erreur 404 avec un message approprié.

## Configuration

Le middleware CORS est configuré pour autoriser les requêtes provenant de :

```
http://localhost:3000
```

Vous pouvez modifier cette configuration dans la section `app.add_middleware` du code si nécessaire.

## Sortie CSV

Les données extraites sont enregistrées dans un fichier CSV (`genshin_characters.csv`) avec les colonnes suivantes :

- URL de l'icône
- Nom
- Qualité
- Élément
- Arme
- Région
- Type de modèle

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des issues ou à soumettre des pull requests pour améliorer ce projet.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.
