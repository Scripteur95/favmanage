# 🎯 FavManager Pro

![FavManager Pro Banner](https://via.placeholder.com/800x200/1e1e2e/cdd6f4?text=FavManager+Pro)

**FavManager Pro** est une application de gestion de favoris conçue pour les utilisateurs de la génération Z. Elle permet d'ajouter, de gérer et d'ouvrir facilement vos favoris, qu'il s'agisse de sites web, de jeux, de dossiers ou d'applications.

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|---------------|-------------|
| **Ajout de favoris** | Ajoutez des favoris de différents types (sites web, jeux, dossiers, applications). |
| **Recherche et filtrage** | Recherchez et filtrez vos favoris pour un accès rapide. |
| **Interface utilisateur moderne** | Une interface intuitive et stylée pour une expérience utilisateur optimale. |
| **Gestion facile** | Ouvrez, éditez ou supprimez vos favoris directement depuis l'application. |

---

## 🛠 Installation

### Prérequis

- Python 3.8 ou supérieur
- Visual Studio Code (pour le développement)

### Étapes d'installation

1. **Télécharger le projet** :
   - Téléchargez le fichier ZIP du projet depuis la [page des releases](https://github.com/Scripteur95/favmanage/releases).
   - Extrayez le fichier ZIP dans un répertoire de votre choix.

2. **Installer Visual Studio Code** :
   - Téléchargez et installez [Visual Studio Code](https://code.visualstudio.com/).

3. **Installer l'extension Python** :
   - Ouvrez Visual Studio Code.
   - Allez dans les extensions (`Ctrl+Shift+X`) et installez l'extension `Python` de Microsoft.

4. **Ouvrir le projet dans VS Code** :
   - Ouvrez le dossier du projet dans VS Code (`File > Open Folder`).

5. **Installer les dépendances** :
   - Ouvrez un terminal dans VS Code (`Ctrl+Shift+P` puis tapez `Terminal`).
   - Exécutez la commande suivante pour installer les dépendances nécessaires :

     ```bash
     pip install -r requirements.txt
     ```

6. **Lancer l'application** :
   - Dans le terminal, exécutez la commande suivante :

     ```bash
     python favmanage.py
     ```

---

## 🚀 Utilisation

1. **Ajouter un favori** :
   - Remplissez les champs `NOM DU FAVORI` et `URL / CHEMIN`.
   - Sélectionnez le type de favori.
   - Cliquez sur `AJOUTER LE FAVORI`.

2. **Rechercher un favori** :
   - Utilisez la barre de recherche pour filtrer les favoris.

3. **Ouvrir un favori** :
   - Sélectionnez un favori dans la liste et cliquez sur `OUVRIR`.

---

## 📦 Création d'un exécutable

Pour créer un exécutable de l'application, vous pouvez utiliser `PyInstaller` :

1. **Installer PyInstaller** :

   ```bash
   pip install pyinstaller
2 **Créer l'exécutable** :

```bash
pyinstaller --onefile --windowed --name="FavManager_Ultra_GenZ" favmanage.py
```

3. **Trouver l'exécutable** :
L'exécutable sera généré dans le dossier dist.

4. ***commande pour les addon python***:

```
pip install customtkinter Pillow requests
``` 
   
🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

Vous pouvez copier ce texte et l'intégrer dans votre fichier README.md. Cela aidera à structurer et à mettre en forme les informations de manière claire et lisible.


© 2025 FavManager Pro. Tous droits réservés.
