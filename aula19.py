import tkinter as tk

def soma():
    n1 = float(input1.get())
    n2 = float(input2.get())
    soma = n1 + n2
    Result.config(text=f'{soma}')

janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('500x500')

# widgets sao elementos da interface como botoes rotulos e entradas

# Label
texto = tk.Label(janela, text= 'CALCULADORA')
texto.grid(row = 1, column = 2, pad = 15)

# Input
input1 = tk.Entry(janela)
input1.grid(row = 2, column = 2, pad = 15)

input2 = tk.Entry(janela)
input2.grid(row = 3, column = 2, pad = 15)

# Label
Result = tk.Label(janela, text = 'Resultado = ')
Result.grid(row = 4, column = 2, pad = 15)

#botao
btn = tk.Button(janela, text = 'clique aqui', command = soma)
btn.grid(row = 5, column = 2, pad = 15)
janela.mainloop()