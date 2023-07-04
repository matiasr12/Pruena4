import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        self.resizable(False, False)

        self.configure(bg="lightblue")
        frame = tk.Frame(self, pady=10, bg="lightblue")
        frame.pack()

        self.username_label = tk.Label(frame, text="Usuario:", bg="lightblue")
        self.username_label.grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(frame, text="Contraseña:", bg="lightblue")
        self.password_label.grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.terms_var = tk.BooleanVar()
        self.terms_check = tk.Checkbutton(frame, text="Acepto los Términos y Condiciones de Uso", variable=self.terms_var, bg="lightblue")
        self.terms_check.grid(row=2, columnspan=2)

        self.login_button = tk.Button(frame, text="Iniciar sesión", command=self.login)
        self.login_button.grid(row=3, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        terms_accepted = self.terms_var.get()

        if username == "matias" and password == "21" and terms_accepted:
            self.destroy()  
            root = tk.Tk()
            ventana = Ventana(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas o Términos y Condiciones no aceptados")





class Ventana(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1460, height=700)
        self.master = master
        self.pack()
        self.create_widgets()
        self.data = []  
        self.modify_mode = False  
        self.selected_index = None  
        self.selected_item_index = None 

    def fNuevo(self):
        id_productos = self.txtId_productos.get()
        descripcion = self.txtDescripcion.get()
        tipo = self.txtTipo.get()
        id_editorial = self.txtId_Editorial.get()
        bodega = self.txtBodega.get()
        ubicacion = self.txtUbicaion.get()
        bodega_de_origen = self.txtBodega_De_Origen.get()
        autor = self.txtAutor.get()
        editorial = self.txtEditorial.get()
        bodega_de_destino = self.txtBodega_De_Destino.get()
        fecha = self.txtFecha.get()
        usuario = self.txtUsuario.get()

        if id_productos and descripcion and tipo and id_editorial and bodega and ubicacion and bodega_de_origen and autor and editorial and bodega_de_destino and fecha and usuario:
            self.data.append((id_productos, descripcion, tipo, id_editorial, bodega, ubicacion, bodega_de_origen, autor, editorial, bodega_de_destino, fecha, usuario))
            self.update_table()
            self.clear_entries()
        else:
          messagebox.showerror("Error", "Tiene que Rellenar los todos los datos")


    def fEliminar(self):
        index = self.selected_item_index
        if index is not None and 0 <= index < len(self.data):
            del self.data[index]
            self.update_table()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Seleccione un dato para eliminar")

    def update_table(self):
        self.grid.delete(*self.grid.get_children())
        for index, item in enumerate(self.data, start=1):
         self.grid.insert("", tk.END, text=str(index), values=item)
    
    def clear_entries(self):
        self.txtId_productos.delete(0, tk.END)
        self.txtDescripcion.delete(0, tk.END)
        self.txtTipo.delete(0, tk.END)
        self.txtId_Editorial.delete(0, tk.END)
        self.txtBodega.delete(0, tk.END)
        self.txtUbicaion.delete(0, tk.END)
        self.txtBodega_De_Origen.delete(0, tk.END)
        self.txtAutor.delete(0, tk.END)
        self.txtEditorial.delete(0, tk.END)
        self.txtBodega_De_Destino.delete(0, tk.END)
        self.txtFecha.delete(0, tk.END)
        self.txtUsuario.delete(0, tk.END)




    def clear_input_fields(self):
        self.txtId_productos.delete(0, tk.END)
        self.txtDescripcion.delete(0, tk.END)
        self.txtTipo.delete(0, tk.END)
        self.txtId_Editorial.delete(0, tk.END)
        self.txtBodega.delete(0, tk.END)
        self.txtUbicaion.delete(0, tk.END)
        self.txtBodega_De_Origen.delete(0, tk.END)
        self.txtAutor.delete(0, tk.END)
        self.txtEditorial.delete(0, tk.END)
        self.txtBodega_De_Destino.delete(0, tk.END)
        self.txtFecha.delete(0, tk.END)
        self.txtUsuario.delete(0, tk.END)

    def fModificar(self):
        datos = self.grid.selection()
        if datos:
            item_id = datos[0]
            values = self.grid.item(item_id)["values"]
            self.selected_index = int(item_id[1:]) - 1

            # Mostrar los valores actuales en los campos de entrada
            self.txtId_productos.delete(0, tk.END)
            self.txtId_productos.insert(tk.END, values[0])
            self.txtDescripcion.delete(0, tk.END)
            self.txtDescripcion.insert(tk.END, values[1])
            self.txtTipo.delete(0, tk.END)
            self.txtTipo.insert(tk.END, values[2])
            self.txtId_Editorial.delete(0, tk.END)
            self.txtId_Editorial.insert(tk.END, values[3])
            self.txtBodega.delete(0, tk.END)
            self.txtBodega.insert(tk.END, values[4])
            self.txtUbicaion.delete(0, tk.END)
            self.txtUbicaion.insert(tk.END, values[5])
            self.txtBodega_De_Origen.delete(0, tk.END)
            self.txtBodega_De_Origen.insert(tk.END, values[6])
            self.txtAutor.delete(0, tk.END)
            self.txtAutor.insert(tk.END, values[7])
            self.txtEditorial.delete(0, tk.END)
            self.txtEditorial.insert(tk.END, values[8])
            self.txtBodega_De_Destino.delete(0, tk.END)
            self.txtBodega_De_Destino.insert(tk.END, values[9])
            self.txtFecha.delete(0, tk.END)
            self.txtFecha.insert(tk.END, values[10])
            self.txtUsuario.delete(0, tk.END)
            self.txtUsuario.insert(tk.END, values[11])

            self.btnModificar.config(text="Confirmar", command=self.confirm_modification)
        else:
            messagebox.showerror("Error","Seleccione una fila para modificar")

    def fGuardar(self):
      pass

    


    
    def confirm_modification(self):
        if self.selected_index < len(self.data):
            id_productos = self.txtId_productos.get()
            descripcion = self.txtDescripcion.get()
            tipo = self.txtTipo.get()
            id_editorial = self.txtId_Editorial.get()
            bodega = self.txtBodega.get()
            ubicacion = self.txtUbicaion.get()
            bodega_de_origen = self.txtBodega_De_Origen.get()
            autor = self.txtAutor.get()
            editorial = self.txtEditorial.get()
            bodega_de_destino = self.txtBodega_De_Destino.get()
            fecha = self.txtFecha.get()
            usuario = self.txtUsuario.get()

            if id_productos and descripcion and tipo and id_editorial and bodega and ubicacion and bodega_de_origen and autor and editorial and bodega_de_destino and fecha and usuario:
                self.data[self.selected_index] = (
                    id_productos, descripcion, tipo, id_editorial, bodega, ubicacion, bodega_de_origen, autor,
                    editorial, bodega_de_destino, fecha, usuario
                )
                self.update_table()
                self.clear_input_fields()
                self.btnModificar.config(text="Modificar", command=self.fModificar)
            else:
                messagebox.showerror("Complete todos los campos")
        else:
            messagebox.showerror("Índice seleccionado fuera de rango")
   
   
   
   
    def create_widgets(self):
        frame1 = tk.Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=700)

        self.btnNuevo = tk.Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)
        self.btnEliminar = tk.Button(frame1, text="Eliminar", command=self.fEliminar, bg="red", fg="white")
        self.btnEliminar.place(x=5, y=90, width=80, height=30)

        self.btnModificar = tk.Button(frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar = tk.Button(frame1, text="Eliminar", command=self.fEliminar, bg="Red", fg="white")
        self.btnEliminar.place(x=5, y=160, width=80, height=30)


        frame2 = tk.Frame(self, bg="#09EED5")
        frame2.place(x=95, y=0, width=150, height=700)

        label1 = tk.Label(frame2, text="Id_productos: ")
        label1.place(x=3, y=5)
        self.txtId_productos = tk.Entry(frame2)
        self.txtId_productos.place(x=3, y=25, width=50, height=20)

        label2 = tk.Label(frame2, text="Descripcion	: ")
        label2.place(x=3, y=55)
        self.txtDescripcion = tk.Entry(frame2)
        self.txtDescripcion.place(x=3, y=75, width=100, height=20)

        label3 = tk.Label(frame2, text="Tipo:  ")
        label3.place(x=3, y=105)
        self.txtTipo = tk.Entry(frame2)
        self.txtTipo.place(x=3, y=125, width=100, height=20)

        label4 = tk.Label(frame2, text="Id_Editorial: ")
        label4.place(x=3, y=155)
        self.txtId_Editorial = tk.Entry(frame2)
        self.txtId_Editorial.place(x=3, y=175, width=100, height=20)

        label5 = tk.Label(frame2, text="Bodega: ")
        label5.place(x=3, y=210)
        self.txtBodega = tk.Entry(frame2)
        self.txtBodega.place(x=3, y=230, width=100, height=20)

        label6 = tk.Label(frame2, text="Ubicaion: ")
        label6.place(x=3, y=250)
        self.txtUbicaion = tk.Entry(frame2)
        self.txtUbicaion.place(x=3, y=270, width=100, height=20)

        label7 = tk.Label(frame2, text="Bodega_De_Origen: ")
        label7.place(x=3, y=300)
        self.txtBodega_De_Origen = tk.Entry(frame2)
        self.txtBodega_De_Origen.place(x=3, y=320, width=100, height=20)

        label8 = tk.Label(frame2, text="Autor: ")
        label8.place(x=3, y=350)
        self.txtAutor = tk.Entry(frame2)
        self.txtAutor.place(x=3, y=370, width=100, height=20)


        label9 = tk.Label(frame2, text="Editorial: ")
        label9.place(x=3, y=400)
        self.txtEditorial = tk.Entry(frame2)
        self.txtEditorial.place(x=3, y=430, width=100, height=20)
        
        label10 = tk.Label(frame2, text="Bodega_De_Destino: ")
        label10.place(x=3, y=470)
        self.txtBodega_De_Destino = tk.Entry(frame2)
        self.txtBodega_De_Destino.place(x=3, y=490, width=100, height=20)


        
        label11 = tk.Label(frame2, text="Fecha: ")
        label11.place(x=3, y=520)
        self.txtFecha = tk.Entry(frame2)
        self.txtFecha.place(x=3, y=540, width=100, height=20)


        label12 = tk.Label(frame2, text="Usuario: ")
        label12.place(x=3, y=580)
        self.txtUsuario = tk.Entry(frame2)
        self.txtUsuario.place(x=3, y=600, width=100, height=20)




        


       

        # sistema de columnas
        self.grid = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7","col8","col9","col10","col11","col12"))

        self.grid.column("#0", width=50)
        self.grid.column("col1", width=60, anchor=tk.CENTER)
        self.grid.column("col2", width=90, anchor=tk.CENTER)
        self.grid.column("col3", width=90, anchor=tk.CENTER)
        self.grid.column("col4", width=90, anchor=tk.CENTER)
        self.grid.column("col5", width=90, anchor=tk.CENTER)
        self.grid.column("col6", width=90, anchor=tk.CENTER)
        self.grid.column("col7", width=90, anchor=tk.CENTER)
        self.grid.column("col8", width=90, anchor=tk.CENTER)
        self.grid.column("col9", width=90, anchor=tk.CENTER)
        self.grid.column("col10", width=90, anchor=tk.CENTER)
        self.grid.column("col11", width=90, anchor=tk.CENTER)
        self.grid.column("col12", width=90, anchor=tk.CENTER)

        self.grid.heading("#0", text="Id", anchor=tk.CENTER)
        self.grid.heading("col1", text="Id_productos", anchor=tk.CENTER)
        self.grid.heading("col2", text="Descripcion", anchor=tk.CENTER)
        self.grid.heading("col3", text="Tipo", anchor=tk.CENTER)
        self.grid.heading("col4", text="Id_Editorial", anchor=tk.CENTER)
        self.grid.heading("col5", text="Bodega", anchor=tk.CENTER)
        self.grid.heading("col6", text="Ubicaion", anchor=tk.CENTER)
        self.grid.heading("col7", text="Bodega_De_Origen", anchor=tk.CENTER)
        self.grid.heading("col8", text="Autor", anchor=tk.CENTER)
        self.grid.heading("col9", text="Editorial", anchor=tk.CENTER)
        self.grid.heading("col10", text="Bodega_De_Destino", anchor=tk.CENTER)
        self.grid.heading("col11", text="Fecha", anchor=tk.CENTER)
        self.grid.heading("col12", text="Usuario", anchor=tk.CENTER)

         #parte de celda de los formularios 
        self.grid.place(x=247, y=0, width=1200, height=900)



if __name__ == "__main__":
    ventna = LoginWindow()
    ventna.mainloop()