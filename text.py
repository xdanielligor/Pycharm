# Lista de comidas e seus preços
menu = {
    1: ("Hambúrguer", 15.90),
    2: ("Pizza", 29.90),
    3: ("Refrigerante", 5.50),
    4: ("Batata Frita", 10.00),
    5: ("Sorvete", 7.90)
}

# Lista para armazenar o pedido do usuário
pedido = []

# Exibindo o menu
print("----- MENU DO RESTAURANTE -----")
for codigo, (comida, preco) in menu.items():
    print(f"{codigo}. {comida} - R$ {preco:.2f}")

# Loop para o usuário escolher os itens
while True:
    escolha = input("\nDigite o número do item que deseja (ou 'sair' para finalizar o pedido): ").strip()

    if escolha.lower() == "sair":
        break
    elif escolha.isdigit() and int(escolha) in menu:
        pedido.append(menu[int(escolha)])
        print(f"{menu[int(escolha)][0]} adicionado ao pedido.")
    else:
        print("Opção inválida. Tente novamente.")

# Mostrando o pedido final
if pedido:
    print("\n----- PEDIDO FINAL -----")
    total = 0
    for item, preco in pedido:
        print(f"{item} - R$ {preco:.2f}")
        total += preco
    print(f"TOTAL: R$ {total:.2f}")
else:
    print("\nVocê não escolheu nenhum item.")
