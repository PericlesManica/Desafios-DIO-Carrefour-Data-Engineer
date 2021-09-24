nota = int(input())

if 0 <= nota < 1:
    print('E')
elif 0 < nota <= 35:
    print('D')
elif 35 < nota <= 60:
    print('C')
elif 60 < nota <= 85:
    print('B')
elif 85 < nota <= 100:
    print('A')
