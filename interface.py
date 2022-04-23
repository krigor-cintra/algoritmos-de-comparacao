from tkinter import *
from conversao import *
from bubble_sort import *
from quicksort import *
from merge_sort import *
from insertion_sort import *
from selection_sort import *
from shell_sort import *
import tkinter as tk

# criando a janela
from tkinter import messagebox

menu_inicial = Tk()
# titulo da janela
menu_inicial.title("Algoritimo De Comparações - Chrigor Silva")
# usando png como logo
menu_inicial.call('wm', 'iconphoto', menu_inicial._w, PhotoImage(file='imagens/logo_estacio.png'))
# tamanho da tela aberta
menu_inicial.geometry("800x500")


def mostrar():
    listaint = lista.get(1.0,END)

    msg=(str_int(listaint))
    messagebox.showinfo(title="Lista Desordenada", message=msg)


Label(menu_inicial, text="Digite a lista:", background="#ff0", foreground="#009", anchor=W, font="Arial 20", ).place(
    x=20, y=20, width=160, height=35)
lista = Text(menu_inicial)
lista.place(x=20, y=60, width=700, height=30)
Button(menu_inicial, text="Mostrar Lista", command=mostrar).place(x=210, y=20, width=160, height=35)


# Ver lista digitada pelo ususario
def show():
    listaint = lista.get(1.0, END)
    a=(var.get())
    msg = (str_int(listaint))
    if a == 1:
        rest = bubble_sort((msg))
        messagebox.showinfo(title="Bubble Sort",message=rest)
    elif a == 2:
        rest = quick_sort(msg)
        messagebox.showinfo(title="Quick Sort", message=rest)
    elif a == 3:
        rest = mergeSort(msg)
        messagebox.showinfo(title="Merge Sort", message=rest)
    elif a == 4:
        rest = insertion_sort(msg)
        messagebox.showinfo(title="Insertion Sort", message=rest)
    elif a == 5:
        rest = selection_sort(msg)
        messagebox.showinfo(title="Selection Sort", message=rest)
    elif a == 6:
        rest = shell_sort(msg)
        messagebox.showinfo(title="Shell Sort", message=rest)

#Checkbutton 1 - 6
var = IntVar()

bubble = Checkbutton(menu_inicial, text="Bubble Sort", variable=var, onvalue="1", offvalue="0")
bubble.place(x=20, y=145, width=100, height=35)
quiclk = Checkbutton(menu_inicial, text="Quick Sort", variable=var, onvalue="2", offvalue="0")
quiclk.place(x=20, y=175, width=100, height=35)
merge = Checkbutton(menu_inicial, text="Merge Sort", variable=var, onvalue="3", offvalue="0")
merge.place(x=20, y=210, width=100, height=35)
insert = Checkbutton(menu_inicial, text="Insertion Sort", variable=var, onvalue="4", offvalue="0")
insert.place(x=120, y=145, width=100, height=35)
select = Checkbutton(menu_inicial, text="Selection Sort", variable=var, onvalue="5", offvalue="0")
select.place(x=120, y=175, width=100, height=35)
shell = Checkbutton(menu_inicial, text="Shell Sort", variable=var, onvalue="6", offvalue="0")
shell.place(x=120, y=210, width=100, height=35)


#Teste futuro
'''def janela():
    janelas = Toplevel()
    janelas.title("Retunr")
    janelas.configure()
    janelas.geometry("400x200")
    janelas.resizable(False, False)
    janelas.transient(menu_inicial)
    janelas.focus_force()
    janelas.grab_set()
    print(var.get())
    resultado = Label(janelas, text=var.get())'''


# botoes finais
mybutton = Button(menu_inicial, text="resultado", command=show).place(x=30, y=280, width=160, height=35)

end = Button(menu_inicial, text="Quit", command=menu_inicial.destroy).place(x=300, y=280, width=160, height=35)

# botão de saida
# ttk.Button(menu_inicial, text="Quit", command=menu_inicial.destroy).grid(column=1, row=0)


# chamando a tela inicial
menu_inicial.mainloop()
