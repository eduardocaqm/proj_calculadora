# importanto tkinter
from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from tkinter import font

# cores

cor1 = '#fabbe7'  # rosa quase branco
cor2 = '#c8ccca'  # cinza
cor3 = '#799995'  # cinza esverdeado
cor4 = '#42f572'  # verde
cor5 = '#508570'

# Janela

janela = Tk()
janela.title('Calculadora')
janela.geometry('250x318')
janela.config(bg=cor2)

# criando frames

frame_tela = Frame(janela, width=250, height=60, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=250, height=259, bg=cor1)
frame_corpo.grid(row=1, column=0)

# variavel todos valores

todos_valores = ''


# criando funcao
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    # passando valor para tela
    valor_texto.set(todos_valores)


# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=3, padx=5, relief=FLAT, anchor="e",
                  justify=RIGHT, bg=cor2, font='Ivy 18')
app_label.place(x=0, y=0)


# Funcao limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


# Funcao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


# criando botoes

b1 = Button(frame_corpo, command=limpar_tela, text='C', width=12, height=2, bg=cor3, font='Ivy 13 bold',
            relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text='%', width=6, height=2, bg=cor3,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b2.place(x=123, y=0)
b3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text='/', width=6, height=2, bg=cor5,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b3.place(x=185, y=0)

b4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text='7', width=6, height=2, bg=cor3,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=51.8)
b5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text='8', width=6, height=2, bg=cor3,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b5.place(x=61, y=51.8)
b6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text='9', width=6, height=2, bg=cor3,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b6.place(x=123, y=51.8)
b7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text='*', width=6, height=2, bg=cor5,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b7.place(x=185, y=51.8)

b8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text='4', width=6, height=2, bg=cor3,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=103.6)
b9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text='5', width=6, height=2, bg=cor3,
            font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b9.place(x=61, y=103.6)
b10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text='6', width=6, height=2, bg=cor3,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b10.place(x=123, y=103.6)
b11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text='-', width=6, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b11.place(x=185, y=103.6)

b12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text='1', width=6, height=2, bg=cor3,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=155.4)
b13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text='2', width=6, height=2, bg=cor3,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b13.place(x=61, y=155.4)
b14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text='3', width=6, height=2, bg=cor3,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b14.place(x=123, y=155.4)
b15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text='+', width=6, height=2, bg=cor5,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b15.place(x=185, y=155.4)

b16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text='0', width=12, height=2, bg=cor3,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=207.2)
b16 = Button(frame_corpo, command=lambda: entrar_valores('.'), text='.', width=6, height=2, bg=cor3,
             font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b16.place(x=123, y=207.2)
b16 = Button(frame_corpo, command=calcular, text='=', width=6, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE)
b16.place(x=185, y=207.2)
janela.mainloop()
