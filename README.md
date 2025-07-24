# 🌟 FavManage 🌟

Bienvenue sur **FavManage** ! Une application géniale pour gérer vos favoris de manière efficace et intuitive.

---

## 📋 Table des matières

- [📌 Prérequis](#-prérequis)
- [🛠 Installation](#-installation)
- [🚀 Utilisation](#-utilisation)
- [📦 Création d'un exécutable](#-création-dun-exécutable)
- [🤝 Contribution](#-contribution)
- [🆘 Support](#-support)
- [📜 Licence](#-licence)

---

## 📌 Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre système :

- [Python 3.11](https://www.python.org/downloads/) 🐍
- pip (généralement inclus avec Python)

---

## 🛠 Installation

### 1. Cloner le dépôt

Ouvrez votre terminal et exécutez les commandes suivantes :

```bash
git clone https://github.com/Scripteur95/favmanage.git
cd favmanage
```

### 2. Installer les dépendances

Assurez-vous que vous avez ajouté Python à votre PATH pendant l'installation. Ensuite, installez les dépendances nécessaires en utilisant pip :

```bash
pip install -r requirements.txt
```

Si vous rencontrez des problèmes avec `pip`, utilisez le chemin complet vers l'exécutable Python :

```bash
C:\Users\Utilisateur\AppData\Local\Programs\Python\Python313\python.exe -m pip install -r requirements.txt
```

---

## 🚀 Utilisation

Pour lancer l'application, utilisez la commande suivante :

```bash
python favmanager.py
```

### Fonctionnalités

- Ajouter des favoris
- Supprimer des favoris
- Organiser les favoris par catégories
- Rechercher des favoris

---

## 📦 Création d'un exécutable

Pour créer un exécutable de l'application, vous pouvez utiliser PyInstaller :

### 1. Installer PyInstaller

```bash
pip install pyinstaller
```

### 2. Créer l'exécutable

Utilisez PyInstaller pour créer un exécutable. Assurez-vous que le répertoire des scripts Python est dans votre PATH, ou utilisez le chemin complet :

```bash
pyinstaller --onefile favmanager.py
```

Si `pyinstaller` n'est pas reconnu, utilisez le chemin complet :

```bash
C:\Users\Utilisateur\AppData\Local\Programs\Python\Python313\Scripts\pyinstaller.exe --onefile favmanager.py
```

### 3. Trouver l'exécutable

Une fois la commande terminée, vous trouverez l'exécutable dans le répertoire `dist`. Vous pouvez copier ce fichier sur votre bureau pour un accès facile.

---

## 🤝 Contribution
Les contributions sont ce qui fait de la communauté open source un endroit incroyable pour apprendre, inspirer et créer. Toute contribution que vous faites est **grandement appréciée**. 

1. Fork le projet
2. Créez votre branche de fonctionnalités (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

---

## 🆘 Support

Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à ouvrir une issue sur le dépôt GitHub. Nous sommes là pour vous aider ! 🤝

---

## 📜 Licence

Distribué sous la licence MIT. Voir `LICENCE` pour plus d'informations.
