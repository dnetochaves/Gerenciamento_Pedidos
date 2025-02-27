from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada

cliente = Cliente("João", "Rua A")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
# print(f"Nome: {cliente.nome}, Endereço: {cliente.endereco}")
#print(f"Item: {item_um.nome}, Preço: {item_um.preco}")
itens = [item_um, item_dois]
pedido_retirada = PedidoRetirada(cliente, itens)

print(f"Total do pedido: {pedido_retirada.calcular_total():.2f}")