from decimal import Decimal

qtd_teste = input("Quantidade de casos teste: ")

for i in range( int(qtd_teste) ):

	amount = 0
	produto_preco_dict = {}
	produto_qtd_dict   = {}

	qtd_produto_feira = input("Quantidade de produtos disponíveis na feira: ")

	for j in range( int(qtd_produto_feira) ):

		produto_preco = input("Produto e preço: ").split()
		produto_preco_dict.setdefault(produto_preco[0], float(produto_preco[1]))

	qtd_produto_desejado = input("Quantidade de produtos desejada: ")

	for k in range( int(qtd_produto_desejado) ):
		
		produto_qtd = input("Produto e respectiva quantidade desejada: ").split()
		produto_qtd_dict.setdefault(produto_qtd[0], int(produto_qtd[1]))

	for x in produto_qtd_dict.keys():
		for y in produto_preco_dict.keys():

			if x == y:
				amount = amount + produto_preco_dict.get(x)*produto_qtd_dict.get(x)


	print("R$", round(Decimal(amount),2))




