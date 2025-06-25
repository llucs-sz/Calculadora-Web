import tkinter as tk

def clicar(botao):
    texto_atual = display.get()
    display.delete(0, tk.END)
    display.insert(0, texto_atual + botao)

def limpar():
    display.delete(0, tk.END)

def calcular():
    expressao = display.get()
    try:
        resultado = eval(expressao)
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora GUI")

display = tk.Entry(janela, width=16, font=("Arial", 24), bd=4, relief="ridge", justify='right')
display.grid(row=0, column=0, columnspan=4)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+'
]

row = 1
col = 0
for botao in botoes:
    action = lambda x=botao: clicar(x) if x != 'C' else limpar()
    tk.Button(janela, text=botao, width=4, height=2, font=("Arial", 18), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(janela, text='=', width=10, height=2, font=("Arial", 18), command=calcular).grid(row=row, column=0, columnspan=4)

janela.mainloop()
