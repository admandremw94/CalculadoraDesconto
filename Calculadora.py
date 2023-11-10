import tkinter as tk

janela = tk.Tk()
janela.title('Calculadora de desconto')
janela.geometry("300x110")

# Ajuste automatico da coluna e linha
janela.rowconfigure([0, 1, 3], weight=1)
janela.columnconfigure([0, 1, 3], weight=1)

def apenas_numeros(event):
    entrada = event.widget.get()
    entrada = entrada.replace(',', '.')  # Substitui vírgulas por pontos
    if not entrada.replace('.', '', 1).isdigit():
        event.widget.delete(0, tk.END)  # Limpa o campo se houver caracteres inválidos

val_real = tk.Label(text='Valor real:', fg='#1C1C1C', padx=5, pady=7)
val_real.grid(row=0, column=0, sticky='NSEW')

caixa1 = tk.Entry()
caixa1.grid(row=0, column=1, padx=5, pady=7)
caixa1.bind('<KeyRelease>', apenas_numeros)

val_desc = tk.Label(text='Valor com desconto:', fg='#1C1C1C', padx=5, pady=7)
val_desc.grid(row=1, column=0)

caixa2 = tk.Entry()
caixa2.grid(row=1, column=1, padx=5, pady=7)
caixa2.bind('<KeyRelease>', apenas_numeros)

def calcular_desconto():
    val_inicial = float(caixa1.get().replace(',', '.'))
    val_venda = float(caixa2.get().replace(',', '.'))
    diferenca = val_venda - val_inicial
    percentual = (diferenca / val_inicial) * 100
    percentual = abs(percentual)
    calculo["text"] = "{:.2f}%".format(percentual)

def on_enter(event):
    calcular_desconto()

botao = tk.Button(janela, text='Calcular', bg='#D3D3D3', fg='#1C1C1C', width=10, command=calcular_desconto)
botao.grid(row=2, column=0, padx=5, pady=7)

calculo = tk.Label(janela, text='Resposta')
calculo.grid(row=2, column=1, padx=5, pady=7)


janela.bind("<Return>", on_enter)

janela.mainloop()

# pyinstaller --onefile --noconsole --icon=icone.ico calculadora.py
