"""
Pedro Esteban
22-0209
Refinando código
Estaremos publicando un codigo de Github el cual sera refinado.
"""


def costs_list():
    archivo2 = open('gift_costs.txt', 'r')
    gift_costs = list(archivo2)
    gift_costs = [int(c) for c in gift_costs]  # convierte los strings a int
    archivo2.close()  # cerrar el archivo después de usarlo y no ser necesario
    return gift_costs


def total(gift_costs):
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost  # los costos menores a 1000 no se le agrega impuesto

    return total_price


def main():
    print(total(costs_list()))
    # llama a los dos funciones y luego imprime el resultado

if __name__ == '__main__':
    main()