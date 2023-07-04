import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Validaciones(tk.Tk):





    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x150")
        self.resizable(False, False)
        self.configure(bg="lightblue")

        frame = tk.Frame(self, pady=10, bg="lightblue")
        frame.pack()

        self.username_label = tk.Label(frame, text="Nombre:", bg="lightblue")
        self.username_label.grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(frame, text="Contraseña:", bg="lightblue")
        self.password_label.grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(frame, text="Iniciar sesión", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        # Establecer la conexión a la base de datos MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="productos"
        )
        self.cursor = self.connection.cursor()

    def login(self):
        Nombre = self.username_entry.get()
        password = self.password_entry.get()

        # consultar la base de datos para verificar las credenciales
        query = "SELECT * FROM usuario WHERE Nombre=%s AND password=%s"
        values = (Nombre, password)
        self.cursor.execute(query, values)
        user = self.cursor.fetchone()

        if user:
            self.destroy()
            root = tk.Tk()
            ventana = Ventana(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def __del__(self):
        # Cerrar la conexión a la base de datos al cerrar la ventana
        self.cursor.close()
        self.connection.close()

class Ventana(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Ventana Principal")
        self.parent.geometry("400x200")
        self.parent.configure(bg="lightblue")

        self.label = tk.Label(self, text="¡Inicio de sesión exitoso!", bg="lightblue")
        self.label.pack(pady=50)

if __name__ == "__main__":
    login_window = Validaciones()
    login_window.mainloop()