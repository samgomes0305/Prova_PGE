número = int(input('Digite o número: '))
print(f'Tabuada do número {número}:')
for n in range(1, 11):
  print(f'{número} x {n} = {número * n}')