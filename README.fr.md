Scraper des personnages Genshin avec FastAPI
Ce projet propose une API FastAPI qui :

Scrape la page du wiki Genshin Impact afin d’obtenir des données sur les personnages.
Enregistre ces données dans un fichier CSV.
Expose ces données via un endpoint JSON.
Table des matières
Aperçu du projet
Structure du projet
Prérequis
Installation
Utilisation
1. Exécuter le script de scraping
2. Lancer le serveur FastAPI
3. Accéder aux données
Personnalisation
Contribution
Licence
Aperçu du projet
Le projet :

Scrape la page Personnages Genshin Impact sur le wiki Fandom.
Récupère une liste de personnages (icône, nom, rareté, élément, arme, région et type de modèle).
Stocke les données dans un fichier CSV nommé par défaut genshin_characters.csv.
Expose un endpoint /genshin_characters qui renvoie le contenu du CSV sous forme de JSON.
Technologies :

requests + BeautifulSoup pour le scraping.
CSV pour sauvegarder les données.
FastAPI pour créer l’API.
CORS (middleware) pour autoriser des requêtes depuis un domaine spécifique (ici http://localhost:3000).
Structure du projet
bash
Copy
.
├── main.py                  # Script principal (scraping + API FastAPI)
├── genshin_characters.csv   # Fichier CSV généré (si le scraping a fonctionné)
├── requirements.txt         # (Optionnel) Liste des dépendances Python
├── README.md                # Fichier de documentation (ce document)
└── ...
Prérequis
Python 3.7+ (ou version plus récente).
pip (souvent inclus avec Python).
Dépendances majeures :

requests (pour les requêtes HTTP)
beautifulsoup4 (pour analyser le HTML)
fastapi (pour créer l’API)
uvicorn (pour exécuter l’API)
csv (bibliothèque standard Python, aucune installation supplémentaire requise)
Si vous disposez d’un fichier requirements.txt, vous pouvez installer les dépendances via :

bash
Copy
pip install -r requirements.txt
Sinon, installez-les une par une :

bash
Copy
pip install requests beautifulsoup4 fastapi uvicorn
Installation
Cloner ou télécharger ce dépôt sur votre machine.

Installer les dépendances (voir ci-dessus).

(Optionnel) Créer un environnement virtuel et l’activer, afin de ne pas polluer votre installation globale Python. Exemple :

bash
Copy
python -m venv venv
source venv/bin/activate    # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
Utilisation
1. Exécuter le script de scraping
Le fichier main.py contient la logique de scraping ainsi que la définition de l’API. Pour lancer le scraping et créer/mettre à jour le fichier genshin_characters.csv, exécutez :

bash
Copy
python main.py
Ce script :

Envoie une requête GET à la page Genshin Characters Wiki.
Cherche le tableau HTML (<table class="article-table sortable alternating-colors-table">).
Extrait chaque ligne (icône, nom, rareté, élément, arme, région, type de modèle).
Stocke ces données dans le fichier CSV genshin_characters.csv.
2. Lancer le serveur FastAPI
Une fois le scraping terminé, vous pouvez démarrer le serveur FastAPI qui se trouve également dans main.py. Utilisez uvicorn :

bash
Copy
uvicorn main:app --reload
Remarque : Si votre fichier Python a un autre nom ou si la variable FastAPI s’appelle différemment, adaptez la commande (ex. uvicorn autre_fichier:app --reload).

Par défaut, uvicorn écoute sur http://127.0.0.1:8000.
3. Accéder aux données
Accédez à l’endpoint :

bash
Copy
GET /genshin_characters
Rendez-vous sur http://127.0.0.1:8000/genshin_characters.

Si le CSV genshin_characters.csv existe, vous obtiendrez un JSON similaire à :
json
Copy
{
  "characters": [
    {
      "Icon": "...",
      "Name": "Amber",
      "Quality": "4-Star",
      "Element": "Pyro",
      "Weapon": "Bow",
      "Region": "Mondstadt",
      "Model Type": "Medium Female"
    },
    ...
  ]
}
Si le CSV est introuvable (vous n’avez pas encore fait le scraping ou il y a eu une erreur), un message d’erreur 404 sera retourné au format JSON.
Personnalisation
Nom du fichier CSV : Modifiez la variable output_file dans le script main.py si vous souhaitez un autre nom de fichier.

Configuration CORS :
Vous pouvez changer l’origine autorisée dans la section :

python
Copy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    ...
)
Ajoutez ou remplacez par les adresses dont vous avez besoin (ex. "http://votre-site.com").

Sélecteurs HTML :
Si la structure du wiki change, vous devrez adapter la recherche du tableau, des colonnes, etc. Exemple :

python
Copy
table = soup.find("table", class_="article-table sortable alternating-colors-table")
Gestion d’erreurs :
Le script affiche un message si le tableau n’est pas trouvé ou si une requête échoue. Vous pouvez personnaliser ces messages ou ajouter des logs plus détaillés.

Contribution
Fork le dépôt.
Créez une branche dédiée à votre fonctionnalité ou correction.
Commitez vos modifications.
Ouvrez une pull request vers la branche principale.
Toute proposition d’amélioration est la bienvenue (optimisations, meilleure gestion des erreurs, support d’autres tableaux, etc.).

Licence
Le projet est distribué sous licence MIT (ou toute autre licence de votre choix). Consultez le fichier LICENSE (s’il existe) pour plus de détails.