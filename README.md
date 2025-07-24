# 🎯 FAVMANAGER PRO - GEN Z EDITION

> **L'ultime gestionnaire de favoris qui déchire tout ! 🔥**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ready%20to%20Rock-red?style=for-the-badge)](https://github.com/Scripteur95/favmanage)

---

## 🚀 QU'EST-CE QUE C'EST ?

**FavManager Pro** est THE gestionnaire de favoris ultime ! Fini de perdre tes liens, dossiers, jeux et apps dans le chaos de ton PC. Avec son style dark ultra-moderne et son interface Gen Z, tu vas kiffer organiser tes trucs préférés ! 

### ✨ LES FEATURES QUI TUENT :

- 🌐 **Sites Web** - Tes sites préférés à portée de clic
- 🎮 **Jeux/Games** - Lance tes jeux directement depuis l'app
- 📁 **Dossiers** - Accès rapide à tes dossiers importants  
- 📱 **Applications** - Tous tes logiciels favoris organisés
- 🔍 **Recherche ultra-rapide** - Trouve tout en 0.1 seconde
- 📊 **Stats en temps réel** - Parce que les chiffres c'est cool
- 🎨 **Design dark moderne** - Tes yeux vont dire merci

---

## 🛠️ INSTALLATION FACILE (ÉTAPE PAR ÉTAPE)

### 📋 **ÉTAPE 0 : Vérifier les prérequis**

Avant de commencer, assure-toi d'avoir :
- ✅ **Python 3.8+** installé ([Télécharger ici](https://python.org))
- ✅ **Visual Studio Code** ([Télécharger ici](https://code.visualstudio.com/))
- ✅ **Git** pour cloner le repo ([Télécharger ici](https://git-scm.com/))

> 💡 **Tip** : Pour vérifier si Python est installé, tape `python --version` dans ton terminal !

### 📥 **ÉTAPE 1 : Récupérer le code**

```bash
# Clone le repository (copy-paste cette ligne)
git clone https://github.com/Scripteur95/favmanage.git

# Va dans le dossier
cd favmanage
```

### 🐍 **ÉTAPE 2 : Créer l'environnement Python**

```bash
# Crée un environnement virtuel (super important !)
python -m venv favmanager_env

# Active l'environnement
# Sur Windows :
favmanager_env\Scripts\activate
# Sur Mac/Linux :
source favmanager_env/bin/activate
```

> 🎯 **Pourquoi un environnement virtuel ?** Ça évite les conflits entre tes projets Python !

### 📦 **ÉTAPE 3 : Installer les dépendances**

```bash
# Installe les bibliothèques nécessaires
pip install pyinstaller
```

> ⚡ **Note** : FavManager Pro utilise Tkinter (inclus avec Python) donc pas besoin d'autres dépendances !

### 🚀 **ÉTAPE 4 : Lancer l'application**

```bash
# Lance FavManager Pro
python favmanager.py
```

**BOOM ! 🎉 Ton FavManager Pro est lancé !**

---

## 💻 CONFIGURATION VISUAL STUDIO CODE

### 🔧 **Setup VS Code comme un boss**

1. **Ouvre VS Code** et installe ces extensions indispensables :
   - 🐍 **Python** (Microsoft) - L'extension officielle Python
   - 🔍 **Python Debugger** - Pour débugger comme un pro
   - ⚡ **Pylance** - IntelliSense ultra-rapide

2. **Ouvre ton projet** :
   ```bash
   # Depuis le dossier favmanage
   code .
   ```

3. **Configure le debugger** :
   - Appuie sur `F5`
   - Sélectionne "Python File"
   - Ton app se lance en mode debug ! 🎯

### ⌨️ **Raccourcis VS Code utiles**

- `Ctrl + F5` : Lancer sans debug
- `F5` : Lancer avec debug
- `Ctrl + Shift + P` : Palette de commandes
- `Ctrl + `` ` : Terminal intégré

---

## 📦 CRÉER UN FICHIER .EXE

### 🎯 **Méthode 1 : PyInstaller (Recommandée)**

```bash
# Assure-toi d'être dans le bon dossier
cd favmanage

# Crée l'exécutable (une seule commande magique !)
pyinstaller --onefile --windowed --name="FavManagerPro" favmanager.py

# Ton .exe sera dans le dossier dist/ !
```

**Options expliquées :**
- `--onefile` : Un seul fichier .exe (plus facile à partager)
- `--windowed` : Pas de console noire qui s'ouvre
- `--name` : Le nom de ton .exe

### 🎨 **Méthode 2 : Avec une icône custom**

```bash
# Si tu as une icône .ico
pyinstaller --onefile --windowed --icon=icon.ico --name="FavManagerPro" favmanager.py
```

### 🖥️ **Méthode 3 : Interface graphique (Auto-py-to-exe)**

```bash
# Installe l'outil graphique
pip install auto-py-to-exe

# Lance l'interface
auto-py-to-exe
```

**Configuration dans l'interface :**
1. 📁 **Script Location** : Choisis `favmanager.py`
2. ⚙️ **Onefile** : Coche "One File"
3. 🪟 **Console Window** : Sélectionne "Window Based"
4. 🎯 **Output Directory** : Laisse par défaut
5. 🚀 **Clique sur "CONVERT .PY TO .EXE"**

---

## 🎮 COMMENT UTILISER FAVMANAGER PRO ?

### 🆕 **Ajouter ton premier favori**

1. **Remplis les champs** :
   - 🏷️ **Nom** : Le nom cool de ton favori
   - 🔗 **URL/Chemin** : Le lien ou le chemin vers ton fichier
   - 📂 **Type** : Web, Jeu, Dossier ou App

2. **Clique sur "➕ AJOUTER LE FAVORI"**

3. **BOOM !** Ton favori apparaît dans la liste ! 🎉

### 🔍 **Rechercher tes favoris**

- Tape dans la barre de recherche
- La liste se filtre automatiquement
- Trouve tout en temps réel ! ⚡

### 🚀 **Ouvrir tes favoris**

1. **Sélectionne** un favori dans la liste
2. **Clique sur "🚀 OUVRIR"**
3. Ton favori se lance automatiquement !

### ✏️ **Modifier ou supprimer**

- **✏️ ÉDITER** : Modifie le nom ou l'URL
- **🗑️ SUPPRIMER** : Supprime définitivement

---

## 🎯 TYPES DE FAVORIS SUPPORTÉS

| Type | Emoji | Exemple | Action |
|------|-------|---------|--------|
| **Site Web** | 🌐 | `https://github.com` | S'ouvre dans ton navigateur |
| **Jeu/Game** | 🎮 | `C:\Games\MonJeu.exe` | Lance l'exécutable |
| **Dossier** | 📁 | `C:\Users\Documents` | Ouvre l'explorateur de fichiers |
| **Application** | 📱 | `C:\Program Files\MonApp.exe` | Lance l'application |

---

## 📁 STRUCTURE DU PROJET

```
favmanage/
├── 📄 favmanager.py          # Le code principal (ton app !)
├── 📄 favoris.json           # Tes favoris sauvegardés
├── 📄 README.md              # Ce fichier que tu lis
├── 📁 dist/                  # Ton .exe sera ici après PyInstaller
├── 📁 build/                 # Fichiers temporaires de PyInstaller
└── 📁 favmanager_env/        # Environnement virtuel Python
```

---

## 🎨 PERSONNALISATION

### 🌈 **Changer les couleurs**

Dans `favmanager.py`, trouve la fonction `setup_styles()` et modifie :

```python
# Couleurs principales (thème Catppuccin Mocha)
background_main = '#1e1e2e'    # Fond principal
foreground_main = '#cdd6f4'    # Texte principal
accent_blue = '#89b4fa'        # Bleu accent
accent_pink = '#f38ba8'        # Rose accent
accent_green = '#a6e3a1'       # Vert accent
```

### 🔤 **Changer les polices**

```python
# Police principale
font_main = ('Segoe UI', 10)
font_title = ('Segoe UI', 24, 'bold')
```

---

## 🐛 DÉPANNAGE

### ❌ **Problèmes courants**

| Problème | Solution |
|----------|----------|
| `python: command not found` | Installe Python ou ajoute-le au PATH |
| `tkinter not found` | Installe `python3-tk` sur Linux |
| L'exe ne se lance pas | Utilise `--debug` avec PyInstaller |
| Favori ne s'ouvre pas | Vérifie que le chemin existe |

### 🆘 **Besoin d'aide ?**

1. **Regarde les logs** dans VS Code
2. **Vérifie le fichier `favoris.json`**
3. **Crée une issue** sur GitHub avec le message d'erreur

---

## 🚀 GUIDE RAPIDE POUR TES POTES

**Pour installer et lancer rapidement :**

```bash
# Copy-paste ces 4 commandes dans ton terminal
git clone https://github.com/Scripteur95/favmanage.git
cd favmanage
python -m venv favmanager_env
favmanager_env\Scripts\activate  # Windows
python favmanager.py
```

**Pour créer l'exe :**

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="FavManagerPro" favmanager.py
```

**L'exe sera dans le dossier `dist/` !** 📦

---

## 🎯 PROCHAINES FEATURES

- [ ] 🌙 **Mode sombre/clair** toggle
- [ ] 🔄 **Synchronisation cloud** 
- [ ] 🏷️ **Système de tags** avancé
- [ ] 📊 **Statistiques détaillées**
- [ ] 🖼️ **Icônes personnalisées**
- [ ] 🎨 **Thèmes personnalisables**
- [ ] 📱 **Version mobile** (peut-être ?)

---

## 🤝 CONTRIBUER

Tu veux améliorer FavManager Pro ? C'est parti ! 

1. **Fork** le projet 🍴
2. **Crée** une branche (`git checkout -b feature/TaFeatureGeniale`)
3. **Commit** tes changements (`git commit -m 'Ajout feature géniale'`)
4. **Push** (`git push origin feature/TaFeatureGeniale`)
5. **Ouvre** une Pull Request 🎯

---

## 📄 LICENCE

Ce projet est sous licence MIT. Fais-en ce que tu veux, mais n'oublie pas de mentionner l'auteur ! 😉

---

## 👨‍💻 AUTEUR

**Scripteur95** - Le dev qui code avec style 😎
- 🐙 GitHub: [@Scripteur95](https://github.com/Scripteur95)
- 💌 Si tu kiffes le projet, n'hésite pas à mettre une ⭐ !

---

## 🙏 REMERCIEMENTS

- 🎨 **Design inspiré** par Catppuccin Mocha
- 🐍 **Powered by** Python & Tkinter
- ❤️ **Fait avec amour** et beaucoup de café ☕

---

> **🎯 Prêt à organiser tes favoris comme un boss ? Lance FavManager Pro et prends le contrôle de ton chaos numérique !** 

**⭐ N'oublie pas de starrer le repo si tu kiffes ! ⭐**
