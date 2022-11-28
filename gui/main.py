import tkinter as tk
from tkinter import messagebox
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

    row_pos = 1

    for data in lexer_data:
        token_data = tk.Label(window, text=data)
        token_data.grid(row=row_pos, column=1)
        row_pos += 1


def buildingParser(path):
    parser = UsoParser(path)
    parser.buildParser()
    result = parser.get_result()
    error = parser.get_error()

    if result != '':
        tk.Label(window, text=result).grid(row=1, column=2)
    elif error != '':
        tk.Label(window, text=error).grid(row=1, column=2)


def run_file():
    buildingLexer(php_file)
    buildingParser(php_file)


window = tk.Tk()
window.title("Editor PHP")
window.wm_geometry('550x550')

# window.rowconfigure(0, weight=1)
# window.columnconfigure(0, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Abrir", command=open_file)
btn_run = tk.Button(fr_buttons, text="Correr", command=run_file)
btn_save = tk.Button(fr_buttons, text="Guardar", command=save_file)

btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=1, column=0, padx=5)
btn_run.grid(row=2, column=0, padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Creando los mensajes del compilador
msg = tk.Label(window, text="Mostrando los mensajes de compiler")
msg.grid(row=1, column=1)

window.mainloop()
