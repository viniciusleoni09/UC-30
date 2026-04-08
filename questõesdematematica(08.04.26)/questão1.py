P = int(input())  
D = int(input())  
B = int(input())  

pontos = P * 1 + D * 2 + B * 3

if pontos >= 150:
    print('B')
elif pontos >= 120:
    print('D')
elif pontos >= 100:
    print('P')
else:
    print('N')
 