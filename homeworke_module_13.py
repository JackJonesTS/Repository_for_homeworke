
numbers_ticket = int(input('Input numbers of ticket: '))
list_visitors = [0]
price_for_every_visitors = []

for i in range(numbers_ticket):
    while True:
        try:
            list_visitors[i] = int(input(f'input age of {i+1} visitor: '))
            if list_visitors[i] <= 0 or list_visitors[i] >= 100:
                raise ValueError('Incorrect age, inter right age.')
                list_visitors[i] = 0
        except ValueError:
            print('Incorrect age, inter right age.')
            list_visitors[i] = 0
        finally:
            if list_visitors[i]:
                list_visitors.append(0)
                break


for i in range(len(list_visitors)-1):
    if list_visitors[i] < 18:
        price_for_every_visitors.append(0)
    if 18 <= list_visitors[i] < 25:
        price_for_every_visitors.append(990)
    if 25 <= list_visitors[i]:
        price_for_every_visitors.append(1390)

if numbers_ticket > 3:
    full_price = 0.9*sum(price_for_every_visitors)
else:
    full_price = sum(price_for_every_visitors)

print(f'all tickets price is: {full_price}')