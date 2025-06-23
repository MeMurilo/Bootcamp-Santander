class Pedido:
  def __init__(self):
    self.itens = []

  def adicionar_item(self, preco):
    self.itens.append(preco)

  def calcular_total(self):
    return sum(self.itens)

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco_str = entrada.rsplit(" ", 1)
    preco = float(preco_str)
    pedido.adicionar_item(preco)

valor_total = pedido.calcular_total()

print(f"Valor total: {valor_total:.2f}")