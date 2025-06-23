# # Dicionário com os valores de desconto
# descontos = {
#     "DESCONTO10": 0.10,
#     "DESCONTO20": 0.20,
#     "SEM_DESCONTO": 0.00
# }

# # Entrada do usuário
# preco = float(input("Digite o valor do preço: ").strip())
# cupom = input("Digite o valor do cupom de desconto: ").strip()

# # TODO: Aplique o desconto se o cupom for válido:
# if cupom in descontos:
#     desconto = descontos[cupom]
#     preco_desconto = preco * (1- desconto)
#     print(f"O preço do produto sera de {preco_desconto:.2f}")
# else:
#     print("Cupom invalido")    


# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
if " " in email:
    print("Email invalido")
elif email.startswith("@") or email.endswith("@"):
    print("Email invalido")
else:
    print("Email valido")    