import tkinter as tk; from tkinter import messagebox; from threading import Thread; from flask import Flask; import sys
app_flask = Flask(__name__); root = None
class MinguelsgoNav:
    def __init__(self, root_window):
        self.root = root_window; self.root.title("Minguelsgo Nav"); self.root.geometry("600x400"); self.root.configure(bg="#c0c0c0")
        self.login_win = tk.Toplevel(self.root); self.login_win.title("Acceso"); self.login_win.geometry("300x130"); self.login_win.configure(bg="#c0c0c0"); self.login_win.grab_set()
        tk.Label(self.login_win, text="Contraseña de Red:", bg="#c0c0c0", fg="black").pack(pady=10)
        self.pass_entry = tk.Entry(self.login_win, show="*", bd=2, relief="sunken"); self.pass_entry.pack(fill="x", padx=20); self.pass_entry.focus_set()
        tk.Button(self.login_win, text="Aceptar", bd=2, relief="raised", bg="#c0c0c0", command=self.check_login).pack(pady=10)
        self.root.withdraw()
    def check_login(self):
        if self.pass_entry.get() == "1234": self.login_win.destroy(); self.root.deiconify()
        else: messagebox.showerror("Error", "Incorrecta"); self.pass_entry.delete(0, tk.END)

def launch_nav():
    global root
    if root is None or not root.winfo_exists():
        root = tk.Tk(); app = MinguelsgoNav(root); root.mainloop()
    else: root.deiconify()

@app_flask.route('/open-nav', methods=['GET', 'POST'])
def open_nav(): launch_nav(); return "OK", 200

def run_server(): app_flask.run(port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    # Necesitas instalar flask para usar el enlace: pip install flask
    Thread(target=run_server, daemon=True).start(); launch_nav()
