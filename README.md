<!-- markdownlint-disable MD033 -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=header&text=FavManager%20Pro&fontSize=60&fontAlignY=35&desc=GenZ%20Edition&descAlignY=55"/>
</p>

<div align="center">

| <img src="https://cdn.simpleicons.org/visualstudiocode/007ACC" width="24"/> VS Code | <img src="https://cdn.simpleicons.org/pyinstaller/2D0359" width="24"/> PyInstaller |
|---|---|
| **Code & Chill** | **Build & Share** |

</div>

---

## 🚀 Objectif
Créer **ton propre EXE** depuis **VS Code** en **5 minutes** → tu pourras filer le `.exe` à tes potes *sans qu’ils installent Python*.

---

## ⚡ Étapes ultra-stylées

| # | Action | Screenshot |
|---|---|---|
| 1 | **Télécharge le code** | [⬇️ Télécharger ZIP](https://github.com/Scripteur95/FavManager-Pro/archive/refs/heads/main.zip) ou `git clone https://github.com/Scripteur95/FavManager-Pro.git` |
| 2 | **Ouvre dans VS Code** | `Ctrl + K  Ctrl + O` → sélectionne le dossier |
| 3 | **Installe l’extension Python** | Extensions → installe « Python » (Microsoft) |
| 4 | **Ouvre le terminal** | `` Ctrl + ` `` ou `Terminal > New Terminal` |
| 5 | **Installe PyInstaller** | ```bash<br>pip install pyinstaller``` |
| 6 | **Build l’EXE** | Colle cette commande :<br>```bash<br>python -m PyInstaller --onefile --windowed --name="FavManager_Ultra_GenZ" favmanager.py``` |
| 7 | **Récupère l’EXE** | Le fichier se trouve dans `dist/FavManager_Ultra_GenZ.exe` |
| 8 | **Partage** | Envoie `FavManager_Ultra_GenZ.exe` à tes potes → ils double-cliquent et c’est parti |

---

## 🎮 Ce que tu obtiens
- **Interface GenZ** (Neon, Dark, Pastel)  
- **Portable** : l’exe fait **≈ 11 Mo**  
- **Zero install** pour tes amis

---

## 🛠️ Problèmes ? Fix rapide
| Erreur | Solution |
|---|---|
| `pyinstaller` introuvable | `pip install pyinstaller --upgrade` |
| `tkinter` manquant | Windows : `winget install python-tk` / macOS : `brew install python-tk` / Linux : `sudo apt install python3-tk` |
| EXE trop gros | Ajoute `--exclude-module matplotlib` ou autres modules non utilisés |

---

## 📸 Aperçu build
<p align="center">
  <img src="https://raw.githubusercontent.com/Scripteur95/FavManager-Pro/main/assets/vscode_build.gif" width="600"/>
</p>

---

## 📦 Bonus – `.vscode/launch.json` (debug rapide)
Crée le fichier `.vscode/launch.json` :
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: favmanager",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/favmanager.py",
      "console": "integratedTerminal"
    }
  ]
}
## 📂 Récupère ton EXE

```text
dist/
└── FavManager_Ultra_GenZ.exe   ← 11 Mo de pur bonheur
## 📤 Partage & Enjoy

Glisse-dépose **ton EXE** sur le bureau de tes potes ou envoie-le par Discord.  
Un double-clic → l’interface **GenZ** s’ouvre, **aucune installation requise**.

---

## ✅ Ce que tu obtiens

| Feature | Description |
|---|---|
| **EXE 11 Mo ultra-portable** | Tient sur une clé USB ou s’envoie par Discord |
| **Interface GenZ** | 3 thèmes : Neon, Dark, Pastel |
| **Gestion multi-type** | WEB, GAMES, APPS, DOSSIERS |
| **Import / Export** | Bookmarks Chrome ou Firefox en un clic |

---

## 🛠️ Fixes rapides

| Bug | Fix |
|---|---|
| `tkinter` manquant | Installe `python-tk` pour ton OS |
| EXE trop gros | Ajoute `--exclude-module matplotlib` à la commande |

---

## 📣 Shout-out

Build ton EXE → **star** le repo → partage à tes potes → deviens une légende.

⭐ **Enjoy la v1.0.0 buildée par toi-même !**

