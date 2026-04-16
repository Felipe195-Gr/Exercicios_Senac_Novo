def metas_vendas(total_venda):
    meta1 = 1000
    meta2 = 5000

    if total_venda < meta1:
        texto =  "Metas não atigida"
    elif total_venda < meta2:
        texto =  "Meta 1 atingida"
    else: 
        texto =  "Meta 2 atingida"
    return texto

total_venda = float(input("Digite o total de vendas: "))
resultado = str(metas_vendas(total_venda))
print(resultado)