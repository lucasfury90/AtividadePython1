porta = input("Digite o estado da porta (A para aberta, F para fechada): ")
janela = input("Digite o estado da janela (A para aberta, F para fechada): ")

alarme = (porta == "A") or (janela == "A")

print(f"ALARME DISPARADO - {alarme}")