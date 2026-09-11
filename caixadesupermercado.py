#caixa de supermercado
produto=input('produto: ')
preço=float(input("preço: R$"))
quantidade=int(input("Quantidade:"))

subtotal = preço * quantidade
if subtotal >=100:
    desconto = subtotal * 0.10
else: 
    desconto = 0
    total = subtotal - desconto
    print(f"Produto: {produto}")
    print(f"Subtotal: R${subtotal:.2f}")
    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Total: R${total:.2f}')
