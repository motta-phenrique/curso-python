import tkinter as tk

# Função para exibir a mensagem quando o botão for clicado
def exibir_mensagem():
    nome = entry_nome.get()
    mensagem = entry_mensagem.get()
    mensagem_final = f"Olá, {nome}!\nSua mensagem: {mensagem}"
    label_resultado.config(text=mensagem_final)

# Cria a janela principal
janela = tk.Tk('Trabalho')
janela.title("Digite seu Nome e Mensagem")

# Define as dimensões da janela
largura = 400
altura = 300
janela.geometry(f"{largura}x{altura}")

# Rótulo e campo de entrada para o nome
label_nome = tk.Label(janela, text="Digite seu Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Rótulo e campo de entrada para a mensagem
label_mensagem = tk.Label(janela, text="Digite sua Mensagem:")
label_mensagem.pack()
entry_mensagem = tk.Entry(janela)
entry_mensagem.pack()

# Botão para exibir a mensagem
botao_exibir = tk.Button(janela, text="Exibir Mensagem", command=exibir_mensagem)
botao_exibir.pack()

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Iniciar a interface gráfica
janela.mainloop()
