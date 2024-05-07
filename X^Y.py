# X elevado a Y: Crie um algoritmo que calcule o valor de x elevado a y,
# onde x é maior que 1 e y é inteiro maior igual a 2.
# Simule a operação de exponenciação utilizando o comando FOR. Exemplo: 3 elevado a 4 = 81.
# Repita o exerício usando o WHILE

titulo = "X elevado a Y"
print(f'{titulo:^30}')

base = int(input("Entre com a base: "))
exponencial = int(input("Entre com o exponencial: "))

total = 1
i = 1
if base < 1 or exponencial < 2:
    print("A base deve ser maior que 1 e o exponencial deve ser maior que 2")
else:
    # for _ in range(exponencial):
    #     total = total * base
    # print(f'{base} elevado {exponencial} é igual a {total}')
    while i <= exponencial:
        total = total * base
        i += 1
    print(f'{base} elevado {exponencial} é igual a {total}')
