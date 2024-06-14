#janela
#titulo
#campos para selecionar as moedas de origem e destino
#botão para coverter
#lista de exibição com os nomes das moedas
 
 
import customtkinter
 
#importar biblioteca que vai fazer a janea
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.geometry("400x400") 
#criar e configurar a janela
 
#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 15)) 
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 20))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font= ("", 13))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD","EUR","BRL","BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD","EUR","BRL","BTC"])

def converter_moeda():
    print("Converter Moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disoniveis = ["USD: dólar americano","EUR: euro","BRL: real brasileiro","BTC: bitcoin"]

for moeda in moedas_disoniveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

#moeda1 =customtkinter.CTkLabel(lista_moedas, text="USD: dólar americano")
#moeda2 =customtkinter.CTkLabel(lista_moedas, text="EUR: euro")
#moeda3 =customtkinter.CTkLabel(lista_moedas, text="BRL: real brasileiro")
#moeda4 =customtkinter.CTkLabel(lista_moedas, text="BTC: bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()

#colocar os elementos criados na tela
titulo.pack(padx=8, pady=8)
texto_moeda_origem.pack(padx=9, pady=9)
campo_moeda_origem.pack(padx=9, pady=9)
texto_moeda_destino.pack(padx=9, pady=9)
campo_moeda_destino.pack(padx=9, pady=9)
botao_converter.pack(padx=7, pady=7)
lista_moedas.pack(padx=9, pady=9)
#rodar janela
 
janela.mainloop()
