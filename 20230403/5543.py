buger = []
drink = []

sang = int(input())
buger.append(sang)
jung = int(input())
buger.append(jung)
ha = int(input())
buger.append(ha)

cola = int(input())
drink.append(cola)
cider = int(input())
drink.append(cider)

print(min(buger) + min(drink) - 50)
