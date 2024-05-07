#Estado onde nasceu: Entre com o estado da pessoa e imprima as mensagens: carioca,
# paulista, mineiro, baiano, cearense, outros estados

titulo = "Estado onde nasceu"
print(f'{titulo:^30}')

estado = input("Digite o estado onde nasceu: ").upper()

if estado in ("SP", "SAO PAULO", "SÃO PAULO"):
    print('Paulista')
elif estado == "RJ":
    print('Carioca')
else:
    print('Outros estados')


