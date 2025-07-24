# README.txt – FavManager Pro GenZ Edition
# ======================================

# 1. Télécharge le projet
Option A – ZIP rapide :
curl -L https://github.com/Scripteur95/favmanage/archive/refs/heads/main.zip -o favmanager.zip
unzip favmanager.zip && cd favmanager-main

Option B – Git clone :
git clone https://github.com/Scripteur95/favmanage.git
cd favmanage

# 2. Installer Visual Studio Code
#    → https://code.visualstudio.com
#    → installe l’extension « Python » (Microsoft)

# 3. Ouvrir le projet dans VS Code
code .                 # ouvre VS Code avec le dossier courant
# Si code n’est pas reconnu : File > Open Folder

# 4. Sélectionner l’interpréteur Python
Ctrl + Shift + P → Python: Select Interpreter → choisis Python 3.8+

# 5. Lancer l’app en mode dev
F5  ou  clic droit sur favmanager.py → Run Python File in Terminal

# 6. Compiler ton propre EXE
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="FavManager_Ultra_GenZ" favmanager.py
# L’EXE sort ici : dist/FavManager_Ultra_GenZ.exe

# ✅ Ce que tu obtiens
# • EXE 11 Mo ultra-portable : clé USB ou Discord
# • Interface GenZ : 3 thèmes (Neon, Dark, Pastel)
# • Gestion multi-type : WEB, GAMES, APPS, DOSSIERS
# • Import / Export : Bookmarks Chrome ou Firefox en 1 clic

# 🛠️ Fixes rapides
# • tkinter manquant : Windows → winget install python-tk
#                        macOS → brew install python-tk
#                        Linux → sudo apt install python3-tk
# • EXE trop gros : ajoute --exclude-module matplotlib à la commande PyInstaller

# 📤 Partage & Enjoy
# Glisse-dépose dist/FavManager_Ultra_GenZ.exe sur le bureau ou envoie-le par Discord.
# Double-clic → interface GenZ → aucune installation requise.

# 📣 Shout-out
# Build ton EXE → star le repo → partage à tes potes → deviens une légende.
# ⭐ Enjoy la v1.0.0 buildée par toi-même !


# ─────────────────────────────────────────
# release.txt – Fichier Release v1.0.0
# ─────────────────────────────────────────
# 📦 Release v1.0.0 – GenZ Edition – 24/07/2025
# VS Code & PyInstaller powered

# 🚀 Assets
# Windows EXE   : https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager_Ultra_GenZ.exe
# macOS ZIP     : https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager-Pro-macOS.zip
# Linux AppImage: https://github.com/Scripteur95/favmanage/releases/latest/download/FavManager-Pro-Linux.AppImage

# ⚡ Build ton EXE
# pip install pyinstaller
# python -m PyInstaller --onefile --windowed --name="FavManager_Ultra_GenZ" favmanager.py
# → dist/FavManager_Ultra_GenZ.exe

# ✅ Features
# • Interface GenZ : 3 thèmes (Neon, Dark, Pastel)
# • Multi-type : WEB, GAMES, APPS, DOSSIERS
# • Import/Export : Bookmarks Chrome / Firefox

# 📣 Shout-out
# Build → star → share → become a legend.
# ⭐ Enjoy the v1.0.0 you built yourself!
