from tkinter import *
import tkinter as tk
from conversao import *
from bubble_sort import *
from quicksort import *
from merge_sort import *
from insertion_sort import *
from selection_sort import *
from shell_sort import *
from tkinter import messagebox
#Iniciando janela
menu_inicial = Tk()
# titulo da janela
menu_inicial.title("Algoritimo De Comparações - Chrigor Silva")
# usando png como logo
menu_inicial.call('wm', 'iconphoto', menu_inicial._w, PhotoImage(file='imagens/logo_estacio.png'))
# tamanho da tela aberta
menu_inicial.geometry("900x600")

#Imagem de fundo
ima = tk.PhotoImage(file='imagens/py_logo.png')
ima=ima.subsample(1,1)
labelima=tk.Label(image=ima)
labelima.place(x=0,y=0,relwidth=1.0,relheight=1.0)


#função para mostrar variavel 
def mostrar():
    listaint = lista.get(1.0,END)

    msg=(str_int(listaint))
    messagebox.showinfo(title="Lista Desordenada", message=msg)


Label(menu_inicial, text="Digite a lista:", foreground="#009", anchor=W, font="Arial 20" ).place(x=20, y=20, width=160, height=35)
lista = Text(menu_inicial)
lista.place(x=20, y=60, width=700, height=30)
Button(menu_inicial, text="Mostrar Lista", command=mostrar).place(x=210, y=20, width=160, height=35)
Label(menu_inicial, text="Obs.: Digitar somente números, positivos ou negativos, separando com espaço. Obrigado!", foreground="#009", anchor=W, font="Arial 10", ).place(
    x=20, y=100, width=540, height=35)

# Ver lista digitada pelo ususario
def show():
    listaint = lista.get(1.0, END)
    a=(var.get())
    msg = (str_int(listaint))
    if a == 1:
        rest = bubble_sort((msg))
        messagebox.showinfo(title="Bubble Sort",message=f"\n {rest[0]}\n Tempo de execução: {rest[1]:.4f} segundos")
    elif a == 2:
        rest = quick_sort(msg)
        messagebox.showinfo(title="Quick Sort", message=f"\n {rest[0]}\n Tempo de execução: {rest[1]:.4f} segundos")
    elif a == 3:
        rest = mergeSort(msg)
        messagebox.showinfo(title="Merge Sort", message=f"\n {rest[0]}\n Tempo de execução: {rest[1]:.4f} segundos")
    elif a == 4:
        rest = insertion_sort(msg)
        messagebox.showinfo(title="Insertion Sort", message=f"\n {rest[0]}\n Tempo de execução: {rest[1]:.4f} segundos")
    elif a == 5:
        rest = selection_sort(msg)
        messagebox.showinfo(title="Selection Sort", message=f"\n {rest[0]}\n Tempo de execução: {rest[1]:.4f} segundos")
    elif a == 6:
        rest = shell_sort(msg)
        messagebox.showinfo(title="Shell Sort", message=f"\n {rest[0]}\n Tempo de execução: {rest[1]:.4f} segundos")

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

#função de limpar all
def clearInput():
    lista.delete("1.0","end")
    insert.deselect()

#Teste futuro
def janela():
    janelas = Toplevel()
    janelas.title("Comparação Geral")
    menu_inicial.call('wm', 'iconphoto', janelas._w, PhotoImage(file='imagens/logo_estacio.png'))
    janelas.configure()
    janelas.geometry("300x250")
    janelas.resizable(False, False)
    janelas.transient(menu_inicial)
    janelas.focus_force()
    janelas.grab_set()
    listaint = lista.get(1.0, END)
    msg = (str_int(listaint))
    if len(msg) ==0:
        final = "ERRO"
        messagebox.showinfo(title="Erro", message=f"Lista vazia, favor digitar uma lista")

    elif len(msg) >0:
        bubble = bubble_sort((msg))
        quick = quick_sort(msg)
        merge = mergeSort(msg)
        insertion = insertion_sort(msg)
        selection = selection_sort(msg)
        shell = shell_sort(msg)

        final=f"\n Bubble Sort\n Tempo de execução: {bubble[1]:.4f} segundos" \
              f"\n Quick Sort\n Tempo de execução: {quick[1]:.4f} segundos" \
              f"\n Merge Sort\n Tempo de execução: {merge[1]:.4f} segundos"\
              f"\n Insertion Sort\n Tempo de execução: {insertion[1]:.4f} segundos" \
              f"\n Selection Sort\n Tempo de execução: {selection[1]:.4f} segundos"\
              f"\n Shell Sort\n Tempo de execução: {shell[1]:.4f} segundos"

    Label(janelas, text=final, foreground="#009", anchor=NW, font="Arial 10").place(x=0, y=0, width=350, height=300)


# botoes finais
mybutton = Button(menu_inicial, text="Resultado", command=show).place(x=30, y=280, width=160, height=35)

end = Button(menu_inicial, text="Sair", command=menu_inicial.destroy).place(x=370, y=280, width=160, height=35)

clear = Button(menu_inicial, text="Limpar", command=clearInput).place(x=200, y=280, width=160, height=35)

comparacao = Button(menu_inicial, text="Comparação geral", command=janela).place(x=540, y=280, width=160, height=35)

# chamando a tela inicial
menu_inicial.mainloop()
