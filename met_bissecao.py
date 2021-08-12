import math


def f(x):
    # Solve the equation
    y = 3*x - math.cos(x) # Escreva aqui a função
    return y
    
    
a0 = 0 # Intervalo inicial
b0 = 1 # Intervalo final
erro = 0.01 # 𝜀 > 0 (precisão);

if f(a0) * f(b0) < 0:
    stop = False
    x0 = (a0 +b0)/2
    i = 0
    while stop == False:
        
        if f(a0) * f(x0) < 0:
            a0 = a0
            b0 = x0
            
        else:
            a0 = x0
            b0 = b0
            
        x1 = (a0 +b0)/2
        
        if abs(x1 - x0) < erro:
            stop = True
            print(f'x = {x1}, com iterations = {i+2} e erro relativo menor que 𝜀 = {erro}')
            
        else:
            x0 = x1
            i += 1
    