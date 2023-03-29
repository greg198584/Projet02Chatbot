# Projet Chatbot Django

Ce projet est un chatbot basé sur Django qui utilise FastText pour le traitement du langage naturel et la compréhension des questions des utilisateurs.

## Prérequis

- Python 3.7+
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez le dépôt GitHub :

```bash
git clone https://github.com/greg198584/Projet02Chatbot.git
cd Projet02Chatbot
```


2. Créez un environnement virtuel et activez-le :

```bash
python3 -m venv myenv
source myenv/bin/activate # Sur macOS et Linux
myenv\Scripts\activate # Sur Windows
```


3. Installez les dépendances du projet :


```bash
pip install -r requirements.txt
```


4. Téléchargez et préparez les modèles FastText :


```bash
cd firstapp
python download_fasttext_model.py
```


5. Appliquez les migrations Django :


```bash
python manage.py migrate
```



## Lancement du projet

1. Activez l'environnement virtuel si ce n'est pas déjà fait :

```bash
source myenv/bin/activate # Sur macOS et Linux
myenv\Scripts\activate # Sur Windows
```


2. Démarrez le serveur de développement Django :

```bash
python manage.py runserver
```


3. Ouvrez votre navigateur et accédez à l'URL suivante : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Vous devriez maintenant voir le chatbot fonctionner et pouvoir interagir avec lui.

## Contribution

Si vous souhaitez contribuer au projet, veuillez créer une branche dédiée et soumettre une pull request avec vos modifications. N'oubliez pas d'inclure une description détaillée de vos changements et de mettre à jour la documentation si nécessaire.

## Licence

Ce projet est distribué sous la licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

