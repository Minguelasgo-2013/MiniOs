import tkinter as tk; from tkinter import messagebox; import webbrowser
class MinguelsgoNavApp:
    def __init__(self, root):
        self.root = root; self.root.title("Minguelsgo Nav - Portal Oficial"); self.root.geometry("520x500"); self.root.configure(bg="#c0c0c0")
        # --- LOGIN OBLIGATORIO CON CONTRASEÑA 1234 ---
        self.login_win = tk.Toplevel(self.root); self.login_win.title("Inicio de Sesión"); self.login_win.geometry("320x150"); self.login_win.configure(bg="#c0c0c0"); self.login_win.grab_set(); self.login_win.resizable(False, False)
        tk.Label(self.login_win, text="Minguelsgo Nav - Control de Acceso", bg="#000080", fg="white", font=("Arial", 10, "bold"), anchor="w").pack(fill="x", pady=(0, 10))
        tk.Label(self.login_win, text="Contraseña del Navegador:", bg="#c0c0c0", fg="black").pack(anchor="w", padx=15)
        self.pass_entry = tk.Entry(self.login_win, show="*", bd=2, relief="sunken"); self.pass_entry.pack(fill="x", padx=15, pady=5); self.pass_entry.focus_set()
        tk.Button(self.login_win, text="Aceptar", bd=2, relief="raised", bg="#c0c0c0", command=self.check_login).pack(anchor="e", padx=15, pady=10)
        self.login_win.bind("<Return>", lambda e: self.check_login()); self.root.withdraw()
        # --- INTERFAZ ESTILO TARJETAS WEB (SIN JUEGOS) ---
        self.top_bar = tk.Frame(self.root, bg="#000080", height=30); self.top_bar.pack(fill="x", side="top")
        tk.Label(self.top_bar, text="🌐 Minguelsgo Nav - Directorio de la Red", bg="#000080", fg="white", font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        self.main_frame = tk.Frame(self.root, bg="#fff", bd=2, relief="sunken"); self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Estructura idéntica de secciones y tarjetas para tus páginas web preferidas
        self.add_section("📂 PORTALES OFICIALES MINGUEROS")
        self.add_card("GITHUB REPOSITORY", "Accede de forma directa a tu repositorio donde tienes guardado todo el código de este sistema.", "https://github.com")
        self.add_card("MINGUELASGO GAMES PORTAL", "Enlace directo al sitio web original con todo el catálogo de software y plataformas.", "https://github.io")
        
        self.add_section("🔍 MOTORES DE BÚSQUEDA SECUNDARIOS")
        self.add_card("GOOGLE WEB", "Si necesitas salir de la red interna de Minguelsgo, usa el buscador global de Google.", "https://google.com")
        self.add_card("YOUTUBE RETRO", "Plataforma externa para la reproducción de contenido multimedia y música de la época.", "https://youtube.com")

    def check_login(self):
        if self.pass_entry.get() == "1234": self.login_win.destroy(); self.root.deiconify()
        else: messagebox.showerror("Error", "Contraseña incorrecta."); self.pass_entry.delete(0, tk.END)

    def add_section(self, title):
        tk.Label(self.main_frame, text=title, font=("Arial", 10, "bold"), bg="#fff", fg="#808080").pack(anchor="w", padx=10, pady=(15, 2))
        tk.Frame(self.main_frame, height=1, bg="#808080").pack(fill="x", padx=10, pady=(0, 10))

    def add_card(self, title, desc, url):
        card = tk.Frame(self.main_frame, bg="#f0f0f0", bd=1, relief="solid", padx=10, pady=8); card.pack(fill="x", padx=10, pady=5)
        tk.Label(card, text=title, font=("Arial", 9, "bold"), bg="#f0f0f0", fg="#000080").pack(anchor="w")
        tk.Label(card, text=desc, bg="#f0f0f0", fg="#333", font=("Arial", 8), wraplength=440, justify="left").pack(anchor="w", pady=(2, 6))
        tk.Button(card, text="ABRIR ENLACE", bd=2, relief="raised", bg="#c0c0c0", activebackground="#c0c0c0", font=("Arial", 8, "bold"), command=lambda: webbrowser.open(url)).pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk(); app = MinguelsgoNavApp(root); root.mainloop()
