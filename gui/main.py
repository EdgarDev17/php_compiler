import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Lexer import UsoLexer
from Parser import UsoParser


def open_file():
    """ Abrir archivo """
    filepath = askopenfilename(
        filetypes=[("PHP FILES", "*.php"), ("All Files", "*.*")]
    )

    global php_file
    php_file = filepath

    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")


def save_file():
    """ Guardar Archivo """
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    global php_file

    php_file = filepath
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")


def buildingLexer(path):
    lexer = UsoLexer(path)
    lexer.buildLexer()
    lexer_data = lexer.getTokenAnalized()

    row_pos = 2

    for data in lexer_data:
        token_data = tk.Label(frame_text, text=data, padx=25, pady=10, bg="#ffffff")
        token_data.grid(row=row_pos, column=2, sticky='news')
        row_pos += 1


def buildingParser(path):
    parser = UsoParser(path)
    parser.buildParser()
    result = parser.get_result()
    error = parser.get_error()

    if error is not '':
        tk.Label(frame_text, text=result, bg="#ffffff").grid(row=1, column=2)
    elif result is not '':
        tk.Label(frame_text, text=error, bg="#ffffff").grid(row=1, column=2)
    else:
        tk.Label(frame_text, text='').grid(row=1, column=2)


def clear_frame():
    for widgets in frame_text.winfo_children():
        widgets.destroy()


def run_file():
    buildingLexer(php_file)
    buildingParser(php_file)


# Configuracion iniciales de la ventana
window = tk.Tk()
window.title("Editor PHP")
window.wm_geometry('700x700')
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=0.1, padx=10, pady=10)

# Configuracion y estilos de los botones
btn_open = tk.Button(fr_buttons, text="Abrir", bg='#ffffff', fg='#000000', padx=25, pady=5, bd=0.1, command=open_file)
btn_save = tk.Button(fr_buttons, text="Guardar", bg='#ffffff', fg='#000000', padx=25, pady=5, bd=0.1, command=save_file)
btn_run = tk.Button(fr_buttons, text="Correr", bg='#22c55e', fg='#ffffff', padx=25, pady=5, bd=0.1, command=run_file)
btn_clean = tk.Button(fr_buttons, text="Limpiar", bg='#ef4444', fg='#ffffff', padx=25, pady=5, bd=0.1, command=clear_frame)

# Posicion de cada boton en el GRID
btn_open.grid(row=0, column=0, padx=5, pady=10)
btn_save.grid(row=1, column=0, padx=5, pady=10)
btn_run.grid(row=2, column=0, padx=5, pady=10)
btn_clean.grid(row=3, column=0, padx=5, pady=10)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Frame principal
compiler_container = tk.Frame(window, height=750, width=1000, pady=50, padx=50)
compiler_container.grid(row=2, column=1, columnspan=2, sticky='nw')
compiler_container.grid_rowconfigure(0, weight=1)
compiler_container.grid_columnconfigure(0, weight=1)
compiler_container.grid_propagate(False)

# Creando el canva
canva = tk.Canvas(compiler_container, bg='#ffffff', width=700, height=350)
canva.grid(row=0, column=0, sticky='news')

# Creando el scroll Y
verticalScroll = tk.Scrollbar(canva, orient='vertical', command=canva.yview)
verticalScroll.grid(row=1, column=3, sticky='ns')
canva.configure(yscrollcommand=verticalScroll.set)

# Frame que contiene los mensajes del compilador
frame_text = tk.Frame(canva, bg="#ffffff")
canva.create_window((0, 0), window=frame_text, anchor='nw')
canva.config(scrollregion=canva.bbox("all"))

window.mainloop()
