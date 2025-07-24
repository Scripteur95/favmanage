import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser
import os
import subprocess
import json
from datetime import datetime

class FavManagerPro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎯 FAVMANAGER PRO - GEN Z EDITION")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1e1e2e')
        
        # Style configuration
        self.setup_styles()
        
        # Data storage
        self.favorites_file = "favoris.json"
        self.favorites = self.load_favorites()
        
        # Create UI
        self.create_ui()
        self.update_stats()
        
    def setup_styles(self):
        """Configure les styles pour l'interface"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configuration des couleurs modernes sombres
        style.configure('Title.TLabel', 
                       background='#1e1e2e', 
                       foreground='#cdd6f4', 
                       font=('Segoe UI', 24, 'bold'))
        
        style.configure('Subtitle.TLabel', 
                       background='#1e1e2e', 
                       foreground='#89b4fa', 
                       font=('Segoe UI', 12))
        
        style.configure('Section.TLabel', 
                       background='#1e1e2e', 
                       foreground='#f38ba8', 
                       font=('Segoe UI', 14, 'bold'))
        
        style.configure('Custom.TFrame', 
                       background='#1e1e2e', 
                       relief='flat', 
                       borderwidth=0)
        
        style.configure('Green.TButton', 
                       background='#a6e3a1', 
                       foreground='#1e1e2e', 
                       font=('Segoe UI', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        
        style.configure('Red.TButton', 
                       background='#f38ba8', 
                       foreground='#1e1e2e', 
                       font=('Segoe UI', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        
        style.configure('Orange.TButton', 
                       background='#fab387', 
                       foreground='#1e1e2e', 
                       font=('Segoe UI', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        
    def create_ui(self):
        """Crée l'interface utilisateur"""
        # Header
        header_frame = ttk.Frame(self.root, style='Custom.TFrame')
        header_frame.pack(pady=20, padx=20, fill='x')
        
        title_label = ttk.Label(header_frame, text="🎯 FAVMANAGER PRO", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, text="< GEN Z EDITION - ULTRA STYLE >", style='Subtitle.TLabel')
        subtitle_label.pack()
        
        # Stats Frame
        self.create_stats_frame()
        
        # Main Content Frame
        main_frame = ttk.Frame(self.root, style='Custom.TFrame')
        main_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Left side - Add favorite
        left_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        self.create_add_section(left_frame)
        
        # Right side - Favorites list
        right_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        self.create_favorites_section(right_frame)
        
    def create_stats_frame(self):
        """Crée la barre de statistiques"""
        stats_frame = ttk.Frame(self.root, style='Custom.TFrame')
        stats_frame.pack(pady=10, padx=20, fill='x')
        
        # Stats labels
        self.stats_labels = {}
        stats_data = [
            ('TOTAL', 'total_count'),
            ('WEB', 'web_count'),
            ('GAMES', 'game_count'),
            ('FOLDERS', 'folder_count'),
            ('APPS', 'app_count')
        ]
        
        for i, (label, key) in enumerate(stats_data):
            stat_frame = ttk.Frame(stats_frame, style='Custom.TFrame')
            stat_frame.pack(side='left', padx=20, pady=10)
            
            count_label = ttk.Label(stat_frame, text="0", 
                                   font=('Segoe UI', 20, 'bold'),
                                   background='#1e1e2e', foreground='#cdd6f4')
            count_label.pack()
            
            label_text = ttk.Label(stat_frame, text=label,
                                  font=('Segoe UI', 10),
                                  background='#1e1e2e', foreground='#89b4fa')
            label_text.pack()
            
            self.stats_labels[key] = count_label
            
    def create_add_section(self, parent):
        """Crée la section d'ajout de favoris"""
        # Title
        title = ttk.Label(parent, text="➕ AJOUTER UN NOUVEAU FAVORI", style='Section.TLabel')
        title.pack(pady=10)
        
        # Name entry
        name_frame = ttk.Frame(parent, style='Custom.TFrame')
        name_frame.pack(fill='x', pady=5)
        
        ttk.Label(name_frame, text="🏷️ NOM DU FAVORI:", 
                 background='#1e1e2e', foreground='#cdd6f4',
                 font=('Segoe UI', 10, 'bold')).pack(anchor='w')
        
        self.name_entry = tk.Entry(name_frame, bg='#313244', fg='#cdd6f4', 
                                  font=('Segoe UI', 10), insertbackground='#cdd6f4',
                                  relief='flat', bd=5)
        self.name_entry.pack(fill='x', pady=5)
        
        # URL entry
        url_frame = ttk.Frame(parent, style='Custom.TFrame')
        url_frame.pack(fill='x', pady=5)
        
        ttk.Label(url_frame, text="🔗 URL / CHEMIN:", 
                 background='#1e1e2e', foreground='#cdd6f4',
                 font=('Segoe UI', 10, 'bold')).pack(anchor='w')
        
        url_input_frame = ttk.Frame(url_frame, style='Custom.TFrame')
        url_input_frame.pack(fill='x', pady=5)
        
        self.url_entry = tk.Entry(url_input_frame, bg='#313244', fg='#cdd6f4', 
                                 font=('Segoe UI', 10), insertbackground='#cdd6f4',
                                 relief='flat', bd=5)
        self.url_entry.pack(side='left', fill='x', expand=True)
        
        browse_btn = ttk.Button(url_input_frame, text="📁 BROWSE", 
                               command=self.browse_file, style='Orange.TButton')
        browse_btn.pack(side='right', padx=(10, 0))
        
        # Type selection
        type_frame = ttk.Frame(parent, style='Custom.TFrame')
        type_frame.pack(fill='x', pady=10)
        
        ttk.Label(type_frame, text="📂 TYPE DE FAVORI:", 
                 background='#1e1e2e', foreground='#cdd6f4',
                 font=('Segoe UI', 10, 'bold')).pack(anchor='w')
        
        self.fav_type = tk.StringVar(value="web")
        
        types = [
            ("🌐 SITE WEB", "web"),
            ("🎮 JEU/GAME", "game"),
            ("📁 DOSSIER", "folder"),
            ("📱 APPLICATION", "app")
        ]
        
        radio_frame = ttk.Frame(type_frame, style='Custom.TFrame')
        radio_frame.pack(fill='x', pady=5)
        
        for text, value in types:
            rb = tk.Radiobutton(radio_frame, text=text, variable=self.fav_type, 
                               value=value, bg='#1e1e2e', fg='#cdd6f4',
                               selectcolor='#313244', activebackground='#1e1e2e',
                               font=('Segoe UI', 9), relief='flat')
            rb.pack(anchor='w')
        
        # Buttons
        btn_frame = ttk.Frame(parent, style='Custom.TFrame')
        btn_frame.pack(fill='x', pady=20)
        
        add_btn = ttk.Button(btn_frame, text="➕ AJOUTER LE FAVORI", 
                            command=self.add_favorite, style='Green.TButton')
        add_btn.pack(side='left', padx=5)
        
        clear_btn = ttk.Button(btn_frame, text="🗑️ VIDER", 
                              command=self.clear_form, style='Orange.TButton')
        clear_btn.pack(side='left', padx=5)
        
    def create_favorites_section(self, parent):
        """Crée la section de liste des favoris"""
        # Title
        title = ttk.Label(parent, text="⭐ MES FAVORIS", style='Section.TLabel')
        title.pack(pady=10)
        
        # Search
        search_frame = ttk.Frame(parent, style='Custom.TFrame')
        search_frame.pack(fill='x', pady=5)
        
        self.search_entry = tk.Entry(search_frame, bg='#313244', fg='#cdd6f4', 
                                    font=('Segoe UI', 10), insertbackground='#cdd6f4',
                                    relief='flat', bd=5)
        self.search_entry.pack(fill='x')
        self.search_entry.bind('<KeyRelease>', self.search_favorites)
        self.search_entry.insert(0, "🔍 Rechercher dans tes favoris...")
        self.search_entry.bind('<FocusIn>', self.clear_search_placeholder)
        
        # Favorites list
        list_frame = ttk.Frame(parent, style='Custom.TFrame')
        list_frame.pack(fill='both', expand=True, pady=10)
        
        # Scrollable listbox
        self.favorites_listbox = tk.Listbox(list_frame, bg='#313244', fg='#cdd6f4',
                                           font=('Segoe UI', 10), selectbackground='#89b4fa',
                                           selectforeground='#1e1e2e', relief='flat', bd=0)
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.favorites_listbox.yview)
        self.favorites_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.favorites_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Action buttons
        action_frame = ttk.Frame(parent, style='Custom.TFrame')
        action_frame.pack(fill='x', pady=10)
        
        open_btn = ttk.Button(action_frame, text="🚀 OUVRIR", 
                             command=self.open_favorite, style='Green.TButton')
        open_btn.pack(side='left', padx=5)
        
        edit_btn = ttk.Button(action_frame, text="✏️ ÉDITER", 
                             command=self.edit_favorite, style='Orange.TButton')
        edit_btn.pack(side='left', padx=5)
        
        delete_btn = ttk.Button(action_frame, text="🗑️ SUPPRIMER", 
                               command=self.delete_favorite, style='Red.TButton')
        delete_btn.pack(side='left', padx=5)
        
    def load_favorites(self):
        """Charge les favoris depuis le fichier JSON"""
        try:
            if os.path.exists(self.favorites_file):
                with open(self.favorites_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except:
            return []
    
    def save_favorites(self):
        """Sauvegarde les favoris dans le fichier JSON"""
        try:
            with open(self.favorites_file, 'w', encoding='utf-8') as f:
                json.dump(self.favorites, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde: {e}")
    
    def add_favorite(self):
        """Ajoute un nouveau favori"""
        name = self.name_entry.get().strip()
        url = self.url_entry.get().strip()
        fav_type = self.fav_type.get()
        
        if not name or not url:
            messagebox.showwarning("⚠️ Attention", "Veuillez remplir tous les champs !")
            return
        
        favorite = {
            'id': len(self.favorites) + 1,
            'name': name,
            'url': url,
            'type': fav_type,
            'date_added': datetime.now().isoformat()
        }
        
        self.favorites.append(favorite)
        self.save_favorites()
        self.update_favorites_list()
        self.update_stats()
        self.clear_form()
        
        messagebox.showinfo("✅ Succès", f"Favori '{name}' ajouté avec succès !")
    
    def clear_form(self):
        """Vide le formulaire"""
        self.name_entry.delete(0, tk.END)
        self.url_entry.delete(0, tk.END)
        self.fav_type.set("web")
    
    def browse_file(self):
        """Ouvre un dialog pour choisir un fichier"""
        file_path = filedialog.askopenfilename(
            title="Choisir un fichier",
            filetypes=[
                ("Tous les fichiers", "*.*"),
                ("Exécutables", "*.exe"),
                ("Applications", "*.app"),
            ]
        )
        if file_path:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, file_path)
    
    def update_favorites_list(self):
        """Met à jour la liste des favoris"""
        self.favorites_listbox.delete(0, tk.END)
        
        type_emojis = {
            'web': '🌐',
            'game': '🎮',
            'folder': '📁',
            'app': '📱'
        }
        
        for fav in self.favorites:
            emoji = type_emojis.get(fav['type'], '❓')
            display_text = f"{emoji} {fav['name']} - {fav['type'].upper()}"
            self.favorites_listbox.insert(tk.END, display_text)
    
    def update_stats(self):
        """Met à jour les statistiques"""
        stats = {
            'total_count': len(self.favorites),
            'web_count': len([f for f in self.favorites if f['type'] == 'web']),
            'game_count': len([f for f in self.favorites if f['type'] == 'game']),
            'folder_count': len([f for f in self.favorites if f['type'] == 'folder']),
            'app_count': len([f for f in self.favorites if f['type'] == 'app']),
        }
        
        for key, value in stats.items():
            if key in self.stats_labels:
                self.stats_labels[key].config(text=str(value))
    
    def clear_search_placeholder(self, event):
        """Efface le placeholder de recherche"""
        if self.search_entry.get() == "🔍 Rechercher dans tes favoris...":
            self.search_entry.delete(0, tk.END)
    
    def search_favorites(self, event):
        """Recherche dans les favoris"""
        search_term = self.search_entry.get().lower()
        if search_term == "🔍 rechercher dans tes favoris...":
            search_term = ""
        
        self.favorites_listbox.delete(0, tk.END)
        
        type_emojis = {
            'web': '🌐',
            'game': '🎮',
            'folder': '📁',
            'app': '📱'
        }
        
        for fav in self.favorites:
            if (search_term in fav['name'].lower() or 
                search_term in fav['url'].lower() or 
                search_term in fav['type'].lower()):
                emoji = type_emojis.get(fav['type'], '❓')
                display_text = f"{emoji} {fav['name']} - {fav['type'].upper()}"
                self.favorites_listbox.insert(tk.END, display_text)
    
    def open_favorite(self):
        """Ouvre le favori sélectionné"""
        selection = self.favorites_listbox.curselection()
        if not selection:
            messagebox.showwarning("⚠️ Attention", "Veuillez sélectionner un favori !")
            return
        
        index = selection[0]
        # Ajuster l'index si une recherche est active
        search_term = self.search_entry.get().lower()
        if search_term and search_term != "🔍 rechercher dans tes favoris...":
            # Trouver l'index réel du favori
            visible_favs = [fav for fav in self.favorites if 
                           search_term in fav['name'].lower() or 
                           search_term in fav['url'].lower() or 
                           search_term in fav['type'].lower()]
            if index < len(visible_favs):
                favorite = visible_favs[index]
            else:
                return
        else:
            if index < len(self.favorites):
                favorite = self.favorites[index]
            else:
                return
        
        try:
            if favorite['type'] == 'web':
                webbrowser.open(favorite['url'])
                messagebox.showinfo("🚀 Succès", f"Site web ouvert: {favorite['name']}")
            elif favorite['type'] == 'folder':
                if os.name == 'nt':  # Windows
                    os.startfile(favorite['url'])
                    messagebox.showinfo("🚀 Succès", f"Dossier ouvert: {favorite['name']}")
                else:  # Mac/Linux
                    subprocess.run(['open' if os.name == 'posix' else 'xdg-open', favorite['url']])
                    messagebox.showinfo("🚀 Succès", f"Dossier ouvert: {favorite['name']}")
            else:  # app or game
                if os.name == 'nt':  # Windows
                    if favorite['url'].endswith('.exe'):
                        subprocess.Popen([favorite['url']], shell=False)
                    else:
                        os.startfile(favorite['url'])
                    messagebox.showinfo("🚀 Succès", f"Application lancée: {favorite['name']}")
                else:
                    subprocess.Popen([favorite['url']])
                    messagebox.showinfo("🚀 Succès", f"Application lancée: {favorite['name']}")
            
        except FileNotFoundError:
            messagebox.showerror("❌ Erreur", f"Fichier non trouvé: {favorite['url']}")
        except PermissionError:
            messagebox.showerror("❌ Erreur", f"Permission refusée pour: {favorite['name']}")
        except Exception as e:
            messagebox.showerror("❌ Erreur", f"Impossible d'ouvrir '{favorite['name']}': {str(e)}")
    
    def edit_favorite(self):
        """Édite le favori sélectionné"""
        selection = self.favorites_listbox.curselection()
        if not selection:
            messagebox.showwarning("⚠️ Attention", "Veuillez sélectionner un favori !")
            return
        
        index = selection[0]
        if index >= len(self.favorites):
            return
        
        favorite = self.favorites[index]
        
        # Fenêtre d'édition simple
        new_name = tk.simpledialog.askstring("Éditer", f"Nouveau nom:", initialvalue=favorite['name'])
        if new_name:
            new_url = tk.simpledialog.askstring("Éditer", f"Nouvelle URL:", initialvalue=favorite['url'])
            if new_url:
                favorite['name'] = new_name.strip()
                favorite['url'] = new_url.strip()
                self.save_favorites()
                self.update_favorites_list()
                messagebox.showinfo("✅ Succès", "Favori modifié !")
    
    def delete_favorite(self):
        """Supprime le favori sélectionné"""
        selection = self.favorites_listbox.curselection()
        if not selection:
            messagebox.showwarning("⚠️ Attention", "Veuillez sélectionner un favori !")
            return
        
        index = selection[0]
        if index >= len(self.favorites):
            return
        
        favorite = self.favorites[index]
        
        if messagebox.askyesno("Confirmer", f"Supprimer '{favorite['name']}' ?"):
            self.favorites.pop(index)
            self.save_favorites()
            self.update_favorites_list()
            self.update_stats()
            messagebox.showinfo("🗑️ Supprimé", "Favori supprimé !")
    
    def run(self):
        """Lance l'application"""
        self.update_favorites_list()
        messagebox.showinfo("🎯 Bienvenue", "FavManager Pro chargé !")
        self.root.mainloop()

if __name__ == "__main__":
    # Import pour les dialogs
    import tkinter.simpledialog
    
    app = FavManagerPro()
    app.run()
