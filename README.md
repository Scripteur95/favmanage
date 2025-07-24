<!-- README.md – GenZ Edition 100 % prêt à copier/coller -->
# 🎯 FavManager Pro – GenZ Edition  
### Clone → VS Code → Run → Build EXE → Share. Zero stress.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=header&text=FavManager%20Pro&fontSize=60&fontAlignY=35&desc=GenZ%20Edition&descAlignY=55"/>
</p>

<div align="center">

[![Windows](https://img.shields.io/badge/🚀-Télécharger_Windows-00ff88?style=for-the-badge&logo=windows)](https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager_Ultra_GenZ.exe)
[![macOS](https://img.shields.io/badge/🍏-Télécharger_macOS-00ff88?style=for-the-badge&logo=apple)](https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager-Pro-macOS.zip)
[![Linux](https://img.shields.io/badge/🐧-Télécharger_Linux-00ff88?style=for-the-badge&logo=linux)](https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager-Pro-Linux.AppImage)

</div>

---

## 📥 1. Télécharger le projet
```bash
# Option ZIP rapide
curl -L https://github.com/Scripteur95/favmanage/archive/refs/heads/main.zip -o favmanager.zip
unzip favmanager.zip && cd favmanager-main

# Option Git clone
git clone https://github.com/Scripteur95/favmanage.git
cd favmanage


---

```markdown
<!-- release.md – 100 % prêt à coller -->
# 📦 Release v1.0.0 – GenZ Edition  
*24/07/2025 – VS Code powered*

## 🚀 Assets
| Plateforme | Fichier | Lien |
|---|---|---|
| **Windows** | `FavManager_Ultra_GenZ.exe` | [⬇️ Télécharger](https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager_Ultra_GenZ.exe) |
| **macOS** | `FavManager-Pro-macOS.zip` | [⬇️ Télécharger](https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager-Pro-macOS.zip) |
| **Linux** | `FavManager-Pro-Linux.AppImage` | [⬇️ Télécharger](https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager-Pro-Linux.AppImage) |

## ⚡ Build ton EXE
```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="FavManager_Ultra_GenZ" favmanager.py

## 🛠️ Étapes d’installation & utilisation

### 2. Installer Visual Studio Code
- Télécharge VS Code : [code.visualstudio.com](https://code.visualstudio.com)  
- Installe l’extension **Python** (Microsoft) depuis l’onglet Extensions.

### 3. Ouvrir le projet dans VS Code
```bash
code .                 # ouvre VS Code avec le dossier courant

## 🛠️ Suite des étapes

### Si `code` n’est pas reconnu  
Ouvre **VS Code** → `File > Open Folder`.

---

### 4. Sélectionner l’interpréteur Python  
- `Ctrl + Shift + P` → **Python: Select Interpreter**  
- Choisis l’interpréteur Python **3.8+** installé sur ta machine.

---

### 5. Lancer l’app en mode **dev**  
- `F5` ou clic droit sur `favmanager.py` → **Run Python File in Terminal**.

---

### 6. Compiler ton propre EXE (facultatif mais cool)  
Dans le terminal VS Code :
```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="FavManager_Ultra_GenZ" favmanager.py

## 📂 L’EXE sort ici
```text
dist/
└── FavManager_Ultra_GenZ.exe   ← 11 Mo de pur bonheur
## ✅ Ce que tu obtiens

| Feature | Description |
|---|---|
| **EXE 11 Mo ultra-portable** | Copie sur clé USB ou envoie par Discord |
| **Interface GenZ** | 3 thèmes : Neon, Dark, Pastel |
| **Gestion multi-type** | WEB, GAMES, APPS, DOSSIERS |
| **Import / Export** | Bookmarks Chrome ou Firefox en 1 clic |

## 🛠️ Fixes rapides

| Bug | Fix |
|---|---|
| `tkinter` manquant | Windows : `winget install python-tk` / macOS : `brew install python-tk` / Linux : `sudo apt install python3-tk` |
| EXE trop gros | Ajoute `--exclude-module matplotlib` à la commande PyInstaller |

## 📤 Partage & Enjoy

Glisse-dépose `dist/FavManager_Ultra_GenZ.exe` sur le bureau ou envoie-le par Discord.  
Double-clic → interface **GenZ** → **aucune installation requise**.

## 📣 Shout-out

Build ton EXE → **star** le repo → partage à tes potes → deviens une légende.  
⭐ **Enjoy la v1.0.0 buildée par toi-même !**

